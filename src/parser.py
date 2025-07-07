#!/usr/bin/env python3
"""
versusMonster Script Parser - Step 1 of 8-Component Pipeline
Transforms markdown podcast scripts into structured JSON for downstream processing.

PRD-v0 Command: python parser.py episode_007.md
"""

import argparse
import json
import logging
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Tuple


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from config.json file."""
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        # Return default configuration if file doesn't exist
        return {
            "parser": {
                "version": "1.0",
                "default_output_dir": "output/json",
                "default_debug_mode": False,
                "max_processing_time_seconds": 10,
            },
            "logging": {
                "default_level": "INFO",
                "debug_level": "DEBUG",
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
    return logging.getLogger("versusMonster.parser")


def validate_input_file(file_path: str) -> Path:
    """Validate that the input file exists and is readable."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Input path is not a file: {file_path}")

    if path.suffix.lower() != ".md":
        raise ValueError(f"Input file must be a markdown file (.md): {file_path}")

    return path


def ensure_output_directory(output_dir: str, debug: bool = False) -> Path:
    """Ensure output directory exists, create if necessary."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if debug:
        debug_path = output_path / "debug"
        debug_path.mkdir(exist_ok=True)

    return output_path


def normalize_scene_id(scene_name: str) -> str:
    """Normalize scene name to create a valid scene ID."""
    # Convert to lowercase
    scene_id = scene_name.lower()
    # Replace spaces with underscores
    scene_id = scene_id.replace(" ", "_")
    # Replace ampersands with 'and'
    scene_id = scene_id.replace("&", "and")
    # Remove any remaining special characters except underscores
    scene_id = re.sub(r"[^a-z0-9_]", "", scene_id)
    # Remove duplicate underscores
    scene_id = re.sub(r"_+", "_", scene_id)
    # Strip leading/trailing underscores
    scene_id = scene_id.strip("_")

    return scene_id


def parse_dialogue_from_content(
    content: str, logger: logging.Logger
) -> List[Dict[str, Any]]:
    """Extract dialogue lines from scene content."""
    # Pattern to match dialogue: CHARACTER: (optional direction) "text"
    # Supports THORAK:, ZARA:, BOTH:, and potentially other characters
    dialogue_pattern = re.compile(
        r"^([A-Z][A-Z\s]*?):\s*(?:\(([^)]+)\))?\s*\"([^\"]+)\"", re.MULTILINE
    )

    dialogues = []
    for match in dialogue_pattern.finditer(content):
        character = match.group(1).strip()
        direction = match.group(2).strip() if match.group(2) else None
        text = match.group(3).strip()

        # Calculate character count (for cost estimation)
        character_count = len(text)

        dialogue_data = {
            "character": character,
            "direction": direction,
            "text": text,
            "character_count": character_count,
            "line_position": content[: match.start()].count("\n") + 1,
        }

        dialogues.append(dialogue_data)
        logger.debug(f"Found dialogue: {character} ({character_count} chars)")

    return dialogues


def parse_multimedia_tags_from_content(
    content: str, logger: logging.Logger
) -> Dict[str, List[Dict[str, Any]]]:
    """Extract multimedia tags from scene content."""

    # Pattern to match multimedia tags: [TYPE: identifier] optional PROMPT: "text"
    multimedia_patterns = {
        "image_tags": re.compile(
            r"^\\\[IMG:\s*([^\]]+)\\\](?:\s*PROMPT:\s*\"([^\"]+)\")?", re.MULTILINE
        ),
        "sfx_tags": re.compile(r"^\\\[SFX:\s*([^\]]+)\\\]", re.MULTILINE),
        "music_tags": re.compile(r"^\\\[MUSIC:\s*([^\]]+)\\\]", re.MULTILINE),
        "ambient_tags": re.compile(r"^\\\[AMBIENT:\s*([^\]]+)\\\]", re.MULTILINE),
        "transition_tags": re.compile(r"^\\\[TRANSITION:\s*([^\]]+)\\\]", re.MULTILINE),
    }

    multimedia_data = {
        "image_tags": [],
        "sfx_tags": [],
        "music_tags": [],
        "ambient_tags": [],
        "transition_tags": [],
    }

    # Extract image tags (can have optional PROMPT)
    for match in multimedia_patterns["image_tags"].finditer(content):
        tag_id = match.group(1).strip()
        prompt = match.group(2).strip() if match.group(2) else None
        line_position = content[: match.start()].count("\n") + 1

        image_data = {
            "tag_id": tag_id,
            "prompt": prompt,
            "line_position": line_position,
            "tag_type": "image",
        }
        multimedia_data["image_tags"].append(image_data)
        logger.debug(f"Found IMG tag: {tag_id}")

    # Extract other multimedia tags (simpler format)
    for tag_type, pattern in multimedia_patterns.items():
        if tag_type == "image_tags":
            continue  # Already processed above

        for match in pattern.finditer(content):
            tag_id = match.group(1).strip()
            line_position = content[: match.start()].count("\n") + 1

            tag_data = {
                "tag_id": tag_id,
                "line_position": line_position,
                "tag_type": tag_type.replace("_tags", ""),  # "sfx_tags" -> "sfx"
            }
            multimedia_data[tag_type].append(tag_data)
            logger.debug(f"Found {tag_type.upper().replace('_TAGS', '')} tag: {tag_id}")

    return multimedia_data


def extract_scenes(content: str, logger: logging.Logger) -> List[Dict[str, Any]]:
    """Extract scenes from the markdown content."""
    # Pattern to match scene markers: ## **\[SCENE: NAME\]**
    # Note: In markdown, square brackets are escaped with backslashes
    scene_pattern = re.compile(r"^## \*\*\\\[SCENE: ([^\]]+)\\\]\*\*$", re.MULTILINE)

    # Find all scene markers with their positions
    scene_matches = list(scene_pattern.finditer(content))

    if not scene_matches:
        logger.warning("No scenes found in the script")
        return []

    # Split content into lines for line number tracking
    lines = content.split("\n")

    # Build scenes list
    scenes = []
    for i, match in enumerate(scene_matches):
        scene_name = match.group(1).strip()
        scene_id = normalize_scene_id(scene_name)

        # Calculate line number (1-based)
        start_pos = match.start()
        line_number = content[:start_pos].count("\n") + 1

        # Extract content from this scene marker to the next (or end of file)
        content_start = match.end()
        if i < len(scene_matches) - 1:
            # Content ends at the start of the next scene
            content_end = scene_matches[i + 1].start()
        else:
            # Last scene - content goes to end of file
            content_end = len(content)

        # Extract and clean scene content
        scene_content = content[content_start:content_end].strip()

        # Parse dialogues within this scene
        dialogues = parse_dialogue_from_content(scene_content, logger)

        # Parse multimedia tags within this scene
        multimedia_tags = parse_multimedia_tags_from_content(scene_content, logger)

        scene_data = {
            "scene_id": scene_id,
            "scene_name": scene_name,
            "start_line": line_number,
            "content": scene_content,
            "dialogues": dialogues,
            "multimedia": multimedia_tags,
            "metadata": {
                "dialogue_count": len(dialogues),
                "image_tags": multimedia_tags["image_tags"],
                "sfx_tags": multimedia_tags["sfx_tags"],
                "music_tags": multimedia_tags["music_tags"],
                "ambient_tags": multimedia_tags["ambient_tags"],
                "transition_tags": multimedia_tags["transition_tags"],
            },
        }

        scenes.append(scene_data)
        logger.debug(
            f"Extracted scene: {scene_name} (line {line_number}, {len(dialogues)} dialogues)"
        )

    logger.info(f"Extracted {len(scenes)} scenes from the script")
    return scenes


def parse_episode_script(input_path: Path, logger: logging.Logger) -> Dict[str, Any]:
    """Parse the episode markdown script into structured data."""
    logger.info(f"Reading script from: {input_path}")

    try:
        with open(input_path, "r", encoding="utf-8") as file:
            content = file.read()
    except UnicodeDecodeError:
        logger.error(f"Failed to read file with UTF-8 encoding: {input_path}")
        raise

    # Extract episode number from filename
    episode_match = input_path.stem
    episode_number = (
        episode_match
        if episode_match.startswith("episode_")
        else f"episode_{episode_match}"
    )

    # Extract scenes from the content
    scenes = extract_scenes(content, logger)

    # Generate warnings if no scenes found
    warnings = []
    if not scenes:
        warnings.append("No scene markers found. Expected format: ## **[SCENE: NAME]**")

    # Placeholder parsing result - will be implemented in subsequent tasks
    parsed_data = {
        "episode_metadata": {
            "title": f"Episode {episode_number.replace('episode_', '').replace('_', ' ').title()}",
            "number": episode_number,
            "input_file": str(input_path.absolute()),
            "content_preview": content[:200] + "..." if len(content) > 200 else content,
            "total_scenes": len(scenes),
        },
        "scenes": scenes,
        "warnings": warnings,
        "feedback": {
            "missing_tags": [],
            "format_violations": [],
            "quality_suggestions": [],
        },
    }

    logger.info(f"Parsed episode: {parsed_data['episode_metadata']['title']}")
    logger.info(f"Content length: {len(content)} characters")
    logger.info(f"Total scenes: {len(scenes)}")

    return parsed_data


def calculate_character_counts(scenes: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculate character counts for cost estimation."""
    character_counts = {}
    total_characters = 0

    for scene in scenes:
        for dialogue in scene.get("dialogues", []):
            character = dialogue["character"]
            char_count = dialogue["character_count"]

            if character not in character_counts:
                character_counts[character] = 0
            character_counts[character] += char_count
            total_characters += char_count

    return {"total_characters": total_characters, "by_speaker": character_counts}


def calculate_multimedia_counts(scenes: List[Dict[str, Any]]) -> Dict[str, int]:
    """Calculate multimedia tag counts for cost estimation."""
    counts = {
        "image_generation_count": 0,
        "sfx_count": 0,
        "music_cue_count": 0,
        "ambient_count": 0,
        "transition_count": 0,
    }

    for scene in scenes:
        multimedia = scene.get("multimedia", {})
        counts["image_generation_count"] += len(multimedia.get("image_tags", []))
        counts["sfx_count"] += len(multimedia.get("sfx_tags", []))
        counts["music_cue_count"] += len(multimedia.get("music_tags", []))
        counts["ambient_count"] += len(multimedia.get("ambient_tags", []))
        counts["transition_count"] += len(multimedia.get("transition_tags", []))

    return counts


def generate_output_metadata(
    input_path: Path, processing_time: float, scenes: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """Generate metadata for the parsed output."""
    character_stats = calculate_character_counts(scenes)
    multimedia_stats = calculate_multimedia_counts(scenes)

    return {
        "processing_timestamp": datetime.now().isoformat(),
        "input_file_path": str(input_path.absolute()),
        "total_processing_time_seconds": round(processing_time, 3),
        "estimated_downstream_costs": {
            "elevenlabs_character_count": character_stats["total_characters"],
            "image_generation_count": multimedia_stats["image_generation_count"],
            "sfx_count": multimedia_stats["sfx_count"],
            "music_cue_count": multimedia_stats["music_cue_count"],
            "ambient_count": multimedia_stats["ambient_count"],
            "transition_count": multimedia_stats["transition_count"],
        },
        "validation_status": "passed",  # Will be determined in Task 5.1
        "character_count_by_speaker": character_stats["by_speaker"],
    }


def save_output_files(
    parsed_data: Dict[str, Any],
    metadata: Dict[str, Any],
    output_path: Path,
    episode_name: str,
    debug: bool,
    logger: logging.Logger,
) -> None:
    """Save the parsed data and metadata to output files."""

    # Combine parsed data with metadata
    output_data = {"metadata": metadata, **parsed_data}

    # Main JSON output
    json_file = output_path / f"{episode_name}.json"
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(output_data, file, indent=2, ensure_ascii=False)

    logger.info(f"✓ JSON output saved: {json_file}")

    # Validation report
    validation_file = output_path / f"{episode_name}_validation.txt"
    with open(validation_file, "w", encoding="utf-8") as file:
        file.write(f"versusMonster Script Parser - Validation Report\n")
        file.write(f"Generated: {metadata['processing_timestamp']}\n")
        file.write(f"Episode: {episode_name}\n")
        file.write(f"Processing time: {metadata['total_processing_time_seconds']}s\n")
        file.write(f"Status: {metadata['validation_status']}\n\n")

        if parsed_data.get("warnings"):
            file.write("WARNINGS:\n")
            for warning in parsed_data["warnings"]:
                file.write(f"  - {warning}\n")
        else:
            file.write("No warnings generated.\n")

    logger.info(f"✓ Validation report saved: {validation_file}")

    # Debug output (if enabled)
    if debug:
        debug_path = output_path / "debug"
        debug_file = debug_path / f"{episode_name}_debug.json"
        with open(debug_file, "w", encoding="utf-8") as file:
            json.dump(
                {
                    "debug_info": {
                        "full_metadata": metadata,
                        "parsing_details": "Debug information will be added in subsequent tasks",
                    }
                },
                file,
                indent=2,
            )
        logger.info(f"✓ Debug output saved: {debug_file}")


def main() -> int:
    """Main entry point for the script parser."""
    start_time = time.time()

    # Load configuration
    try:
        config = load_config()
    except Exception as e:
        print(f"❌ Failed to load configuration: {e}")
        return 1

    parser_config = config.get("parser", {})

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Parse versusMonster podcast scripts into structured JSON",
        epilog="Example: python parser.py episode_007.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "input_file", help="Path to the markdown script file (e.g., episode_007.md)"
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        default=parser_config.get("default_debug_mode", False),
        help="Enable debug mode with intermediate output files",
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        default=parser_config.get("default_output_dir", "output/json"),
        help=f"Custom output directory (default: {parser_config.get('default_output_dir', 'output/json')})",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"versusMonster Script Parser v{parser_config.get('version', '1.0')}",
    )

    args = parser.parse_args()

    # Set up logging
    logger = setup_logging(args.debug, config)
    parser_version = parser_config.get("version", "1.0")
    pipeline_info = config.get("pipeline", {})
    logger.info(
        f"🚀 versusMonster Script Parser v{parser_version} - Step {pipeline_info.get('step_number', 1)} of {pipeline_info.get('pipeline_total_steps', 8)}-Component Pipeline"
    )

    try:
        # Validate input file
        input_path = validate_input_file(args.input_file)
        logger.info(f"✓ Input file validated: {input_path}")

        # Ensure output directory exists
        output_path = ensure_output_directory(args.output_dir, args.debug)
        logger.info(f"✓ Output directory ready: {output_path}")

        # Parse the episode script
        parsed_data = parse_episode_script(input_path, logger)

        # Generate metadata
        processing_time = time.time() - start_time
        metadata = generate_output_metadata(
            input_path, processing_time, parsed_data["scenes"]
        )

        # Extract episode name for file naming
        episode_name = input_path.stem

        # Save output files
        save_output_files(
            parsed_data, metadata, output_path, episode_name, args.debug, logger
        )

        # Final status
        logger.info(f"✅ Parsing complete in {processing_time:.3f}s")
        logger.info(f"📄 Output: {output_path / f'{episode_name}.json'}")

        return 0

    except Exception as e:
        logger.error(f"❌ Parser failed: {e}")
        if args.debug:
            logger.exception("Full error details:")
        return 1


if __name__ == "__main__":
    sys.exit(main())
