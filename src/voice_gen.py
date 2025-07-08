#!/usr/bin/env python3
"""
versusMonster Voice Generator - Step 2 of 8-Component Pipeline
Transforms Script Parser JSON into individual character voice files using ElevenLabs API.

PRD-v0 Command: python voice_gen.py episode_007.json
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

try:
    from dotenv import load_dotenv
    from elevenlabs import ElevenLabs
    ELEVENLABS_AVAILABLE = True
except ImportError:
    ELEVENLABS_AVAILABLE = False
    ElevenLabs = None


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from config.json file."""
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        # Return default configuration if file doesn't exist
        return {
            "voice_generation": {
                "output_dir": "output/voices",
                "output_format": "wav_44100",
                "model": "eleven_multilingual_v2",
                "max_retries": 3,
                "retry_delay_seconds": 1.0,
                "character_voices": {
                    "THORAK": {
                        "voice_id": "JBFqnCBsd6RMkjVDRZzb",
                        "stability": 0.75,
                        "similarity": 0.85,
                        "style": 0.2
                    },
                    "ZARA": {
                        "voice_id": "21m00Tcm4TlvDq8ikWAM", 
                        "stability": 0.45,
                        "similarity": 0.75,
                        "style": 0.6
                    }
                }
            },
            "logging": {
                "default_level": "INFO",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "date_format": "%H:%M:%S",
            },
        }
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config file {config_path}: {e}")


def setup_logging(debug: bool = False, config: Dict[str, Any] = None) -> logging.Logger:
    """Set up logging configuration."""
    if config is None:
        config = {}

    logging_config = config.get("logging", {})
    level = (
        logging.DEBUG
        if debug
        else getattr(logging, logging_config.get("default_level", "INFO"))
    )

    logging.basicConfig(
        level=level,
        format=logging_config.get(
            "format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        ),
        datefmt=logging_config.get("date_format", "%H:%M:%S"),
    )
    return logging.getLogger("versusMonster.voice_gen")


def setup_elevenlabs_client(logger: logging.Logger) -> Optional[Any]:
    """Initialize ElevenLabs client with API key from environment."""
    if not ELEVENLABS_AVAILABLE:
        logger.error("ElevenLabs SDK not available. Install with: pip install elevenlabs")
        return None
    
    # Load environment variables
    load_dotenv()
    
    api_key = os.getenv('ELEVENLABS_API_KEY')
    if not api_key:
        logger.error("ELEVENLABS_API_KEY not found in environment variables")
        logger.info("Please add your ElevenLabs API key to a .env file")
        return None
    
    try:
        client = ElevenLabs(api_key=api_key)
        logger.info("✓ ElevenLabs client initialized successfully")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize ElevenLabs client: {e}")
        return None


def validate_input_file(file_path: str) -> Path:
    """Validate that the input JSON file exists and is readable."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Input path is not a file: {file_path}")

    if path.suffix.lower() != ".json":
        raise ValueError(f"Input file must be a JSON file (.json): {file_path}")

    return path


def ensure_output_directory(output_dir: str, episode_name: str) -> Path:
    """Ensure voice output directory exists for the episode."""
    episode_output_path = Path(output_dir) / episode_name
    episode_output_path.mkdir(parents=True, exist_ok=True)
    return episode_output_path


def load_script_parser_json(input_path: Path, logger: logging.Logger) -> Dict[str, Any]:
    """Load and validate Script Parser JSON output."""
    logger.info(f"Loading Script Parser JSON from: {input_path}")

    try:
        with open(input_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in input file: {e}")
        raise
    except IOError as e:
        logger.error(f"Failed to read input file: {e}")
        raise

    # Validate required structure
    if "scenes" not in data:
        raise ValueError("Input JSON missing required 'scenes' field")
    
    if "episode_metadata" not in data:
        raise ValueError("Input JSON missing required 'episode_metadata' field")

    episode_title = data.get("episode_metadata", {}).get("title", "Unknown Episode")
    scene_count = len(data["scenes"])
    
    # Count total dialogues
    total_dialogues = sum(len(scene.get("dialogues", [])) for scene in data["scenes"])
    
    logger.info(f"✓ Loaded {episode_title} with {scene_count} scenes and {total_dialogues} dialogues")
    
    return data


def extract_dialogues(scenes: List[Dict[str, Any]], logger: logging.Logger) -> List[Dict[str, Any]]:
    """Extract all dialogue entries from scenes with metadata."""
    dialogues = []
    
    for scene_idx, scene in enumerate(scenes):
        scene_id = scene.get("scene_id", f"scene_{scene_idx}")
        scene_dialogues = scene.get("dialogues", [])
        
        for dialogue_idx, dialogue in enumerate(scene_dialogues):
            # Add scene and position metadata
            dialogue_with_metadata = {
                **dialogue,
                "scene_id": scene_id,
                "scene_index": scene_idx,
                "dialogue_index": dialogue_idx,
                "global_index": len(dialogues)
            }
            dialogues.append(dialogue_with_metadata)
    
    logger.info(f"✓ Extracted {len(dialogues)} total dialogues across all scenes")
    return dialogues


def get_character_voice_settings(character: str, config: Dict[str, Any]) -> Dict[str, Any]:
    """Get voice settings for a specific character."""
    voice_config = config.get("voice_generation", {})
    character_voices = voice_config.get("character_voices", {})
    
    if character in character_voices:
        return character_voices[character]
    
    # Default to THORAK settings for unknown characters
    return character_voices.get("THORAK", {
        "voice_id": "JBFqnCBsd6RMkjVDRZzb",
        "stability": 0.75,
        "similarity": 0.85,
        "style": 0.2
    })


def apply_voice_direction_adjustments(
    base_settings: Dict[str, Any], 
    direction: Optional[str], 
    config: Dict[str, Any]
) -> Dict[str, Any]:
    """Apply voice direction adjustments to base character settings."""
    if not direction:
        return base_settings
    
    # Create a copy of base settings
    adjusted_settings = base_settings.copy()
    
    # Get direction adjustments from config
    direction_adjustments = config.get("voice_generation", {}).get("voice_direction_adjustments", {})
    
    # Normalize direction for lookup (lowercase, remove punctuation)
    direction_key = direction.lower().replace(",", "").replace(".", "").strip()
    
    # Apply adjustments if direction is found
    if direction_key in direction_adjustments:
        adjustments = direction_adjustments[direction_key]
        
        # Adjust stability (clamp between 0 and 1)
        if "stability" in adjustments:
            new_stability = adjusted_settings.get("stability", 0.5) + adjustments["stability"]
            adjusted_settings["stability"] = max(0.0, min(1.0, new_stability))
        
        # Adjust style (clamp between 0 and 1) 
        if "style" in adjustments:
            new_style = adjusted_settings.get("style", 0.5) + adjustments["style"]
            adjusted_settings["style"] = max(0.0, min(1.0, new_style))
    
    return adjusted_settings


def generate_voice_filename(
    episode_name: str, 
    scene_id: str, 
    dialogue_index: int, 
    character: str
) -> str:
    """Generate standardized filename for voice file."""
    # Format: episode_007_cold_open_001_ZARA.wav
    return f"{episode_name}_{scene_id}_{dialogue_index:03d}_{character}.wav"


def generate_voice_file(
    client: Any,
    dialogue: Dict[str, Any],
    voice_settings: Dict[str, Any],
    output_path: Path,
    filename: str,
    config: Dict[str, Any],
    logger: logging.Logger
) -> bool:
    """Generate a single voice file using ElevenLabs API."""
    if output_path.exists():
        logger.debug(f"Skipping existing file: {filename}")
        return True
    
    try:
        voice_config = config.get("voice_generation", {})
        model = voice_config.get("model", "eleven_multilingual_v2")
        output_format = voice_config.get("output_format", "wav_44100")
        max_retries = voice_config.get("max_retries", 3)
        retry_delay = voice_config.get("retry_delay_seconds", 1.0)
        
        text = dialogue["text"]
        voice_id = voice_settings["voice_id"]
        
        # Prepare voice settings for API
        api_voice_settings = {
            "stability": voice_settings.get("stability", 0.5),
            "similarity_boost": voice_settings.get("similarity", 0.75),
            "style": voice_settings.get("style", 0.5)
        }
        
        # Retry logic for API calls
        for attempt in range(max_retries):
            try:
                logger.debug(f"Generating voice for: {text[:50]}...")
                
                # Generate audio using ElevenLabs
                audio_data = client.text_to_speech.convert(
                    text=text,
                    voice_id=voice_id,
                    model_id=model,
                    output_format=output_format,
                    voice_settings=api_voice_settings
                )
                
                # Save audio to file
                with open(output_path, "wb") as audio_file:
                    for chunk in audio_data:
                        audio_file.write(chunk)
                
                logger.debug(f"✓ Generated: {filename}")
                return True
                
            except Exception as e:
                if attempt < max_retries - 1:
                    logger.warning(f"Attempt {attempt + 1} failed for {filename}: {e}")
                    time.sleep(retry_delay * (attempt + 1))  # Exponential backoff
                else:
                    logger.error(f"Failed to generate {filename} after {max_retries} attempts: {e}")
                    return False
    
    except Exception as e:
        logger.error(f"Unexpected error generating {filename}: {e}")
        return False


def process_dialogues(
    client: Any,
    dialogues: List[Dict[str, Any]],
    episode_name: str,
    output_dir: Path,
    config: Dict[str, Any],
    logger: logging.Logger
) -> Dict[str, Any]:
    """Process all dialogues and generate voice files."""
    
    logger.info(f"🎤 Step 1: Processing {len(dialogues)} dialogues...")
    
    # Track processing statistics
    stats = {
        "total_dialogues": len(dialogues),
        "successful_generations": 0,
        "failed_generations": 0,
        "skipped_existing": 0,
        "character_counts": {},
        "processing_start_time": time.time()
    }
    
    for idx, dialogue in enumerate(dialogues):
        character = dialogue["character"]
        scene_id = dialogue["scene_id"]
        dialogue_index = dialogue["dialogue_index"]
        direction = dialogue.get("direction")
        text = dialogue["text"]
        
        # Track character usage
        if character not in stats["character_counts"]:
            stats["character_counts"][character] = 0
        stats["character_counts"][character] += len(text)
        
        # Get character voice settings
        base_voice_settings = get_character_voice_settings(character, config)
        
        # Apply voice direction adjustments
        voice_settings = apply_voice_direction_adjustments(
            base_voice_settings, direction, config
        )
        
        # Generate filename and path
        filename = generate_voice_filename(episode_name, scene_id, dialogue_index, character)
        output_path = output_dir / filename
        
        # Show progress
        progress = f"({idx + 1}/{len(dialogues)})"
        direction_text = f" ({direction})" if direction else ""
        logger.info(f"  {progress} {character}{direction_text}: {text[:50]}{'...' if len(text) > 50 else ''}")
        
        # Check if file already exists
        if output_path.exists():
            stats["skipped_existing"] += 1
            logger.debug(f"Skipping existing file: {filename}")
            continue
        
        # Generate voice file
        success = generate_voice_file(
            client, dialogue, voice_settings, output_path, filename, config, logger
        )
        
        if success:
            stats["successful_generations"] += 1
        else:
            stats["failed_generations"] += 1
    
    stats["processing_end_time"] = time.time()
    stats["total_processing_time"] = stats["processing_end_time"] - stats["processing_start_time"]
    
    return stats


def generate_voice_report(
    stats: Dict[str, Any],
    episode_name: str,
    output_dir: Path,
    config: Dict[str, Any],
    logger: logging.Logger
) -> None:
    """Generate voice generation report."""
    report_path = output_dir.parent / f"{episode_name}_voice_report.txt"
    
    with open(report_path, "w", encoding="utf-8") as file:
        file.write(f"versusMonster Voice Generator - Processing Report\n")
        file.write(f"Generated: {datetime.now().isoformat()}\n")
        file.write(f"Episode: {episode_name}\n")
        file.write(f"Processing time: {stats['total_processing_time']:.2f}s\n\n")
        
        file.write(f"GENERATION SUMMARY:\n")
        file.write(f"  Total dialogues: {stats['total_dialogues']}\n")
        file.write(f"  Successfully generated: {stats['successful_generations']}\n")
        file.write(f"  Failed generations: {stats['failed_generations']}\n")
        file.write(f"  Skipped existing: {stats['skipped_existing']}\n\n")
        
        file.write(f"CHARACTER USAGE:\n")
        for character, char_count in stats['character_counts'].items():
            file.write(f"  {character}: {char_count} characters\n")
        
        if stats['failed_generations'] > 0:
            file.write(f"\nWARNINGS:\n")
            file.write(f"  {stats['failed_generations']} dialogues failed to generate\n")
            file.write(f"  Check logs for detailed error information\n")
    
    logger.info(f"✓ Voice generation report saved: {report_path}")


def main() -> int:
    """Main entry point for the voice generator."""
    start_time = time.time()

    # Load configuration
    try:
        config = load_config()
    except Exception as e:
        print(f"❌ Failed to load configuration: {e}")
        print(f"💡 Using default configuration to continue processing...")
        config = load_config()  # This will return default config on error
        print(f"✓ Default configuration loaded successfully")

    voice_config = config.get("voice_generation", {})

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Generate character voices from Script Parser JSON using ElevenLabs API",
        epilog="Example: python voice_gen.py episode_007.json",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "input_file", help="Path to the Script Parser JSON file (e.g., episode_007.json)"
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Enable debug mode with detailed logging",
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        default=voice_config.get("output_dir", "output/voices"),
        help=f"Custom output directory (default: {voice_config.get('output_dir', 'output/voices')})",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="versusMonster Voice Generator v1.0",
    )

    args = parser.parse_args()

    # Set up logging
    logger = setup_logging(args.debug, config)
    pipeline_info = config.get("pipeline", {})
    logger.info(
        f"🚀 versusMonster Voice Generator v1.0 - Step 2 of {pipeline_info.get('pipeline_total_steps', 8)}-Component Pipeline"
    )

    try:
        # Step 1: Validate input file
        logger.info(f"🔍 Step 1: Validating input file...")
        input_path = validate_input_file(args.input_file)
        logger.info(f"✓ Input file validated: {input_path}")

        # Step 2: Initialize ElevenLabs client
        logger.info(f"🎤 Step 2: Initializing ElevenLabs API client...")
        client = setup_elevenlabs_client(logger)
        if not client:
            logger.error("❌ Failed to initialize ElevenLabs client")
            return 1
        
        # Step 3: Load and process Script Parser JSON
        logger.info(f"📖 Step 3: Loading Script Parser JSON...")
        script_data = load_script_parser_json(input_path, logger)
        episode_name = script_data.get("episode_metadata", {}).get("number", input_path.stem)
        
        # Extract all dialogues
        dialogues = extract_dialogues(script_data["scenes"], logger)
        if not dialogues:
            logger.warning("No dialogues found in Script Parser JSON")
            return 1
        
        logger.info(f"✓ Script data loaded - found {len(dialogues)} dialogues")

        # Step 4: Prepare output directory
        logger.info(f"📁 Step 4: Preparing output directory...")
        output_dir = ensure_output_directory(args.output_dir, episode_name)
        logger.info(f"✓ Output directory ready: {output_dir}")

        # Step 5: Generate voice files
        logger.info(f"🎧 Step 5: Generating voice files...")
        stats = process_dialogues(client, dialogues, episode_name, output_dir, config, logger)
        
        # Generate report
        generate_voice_report(stats, episode_name, output_dir, config, logger)

        # Final status
        processing_time = time.time() - start_time
        logger.info(f"✅ Voice generation complete in {processing_time:.2f}s")
        logger.info(f"📄 Output: {output_dir}")
        logger.info(f"🎯 Status: {stats['successful_generations']}/{stats['total_dialogues']} voices generated")
        
        if stats['failed_generations'] > 0:
            logger.info(f"⚠️ {stats['failed_generations']} generations failed - check voice report")
            return 1
        else:
            logger.info(f"🎉 All voice files generated successfully!")

        return 0

    except FileNotFoundError as e:
        logger.error(f"❌ Input file not found: {e}")
        logger.info(f"💡 Please check the file path and try again")
        return 1
    except ValueError as e:
        logger.error(f"❌ Input validation error: {e}")
        logger.info(f"💡 Please ensure the file is valid Script Parser JSON")
        return 1
    except Exception as e:
        logger.error(f"❌ Unexpected error during processing: {e}")
        if args.debug:
            logger.exception("Full error details:")
        return 1


if __name__ == "__main__":
    sys.exit(main())