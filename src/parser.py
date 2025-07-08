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

try:
    import jsonschema

    SCHEMA_VALIDATION_AVAILABLE = True
except ImportError:
    SCHEMA_VALIDATION_AVAILABLE = False


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


def parse_episode_script(
    input_path: Path, logger: logging.Logger, config: Dict[str, Any]
) -> Dict[str, Any]:
    """Parse the episode markdown script into structured data."""
    logger.info(f"Reading script from: {input_path}")

    try:
        with open(input_path, "r", encoding="utf-8") as file:
            content = file.read()
    except UnicodeDecodeError:
        logger.error(f"Failed to read file with UTF-8 encoding: {input_path}")
        raise
    except IOError as e:
        logger.error(f"Failed to read file: {e}")
        # Return minimal structure to allow processing to continue
        return {
            "episode_metadata": {
                "title": "Error Reading File",
                "number": "error",
                "input_file": str(input_path.absolute()),
                "content_preview": "",
                "total_scenes": 0,
            },
            "scenes": [],
            "warnings": [f"Could not read input file: {str(e)}"],
            "feedback": {
                "missing_tags": [],
                "format_violations": ["File could not be read"],
                "quality_suggestions": ["Check file permissions and try again"],
            },
        }

    # Extract episode number from filename
    episode_match = input_path.stem
    episode_number = (
        episode_match
        if episode_match.startswith("episode_")
        else f"episode_{episode_match}"
    )

    # Extract scenes from the content
    scenes = extract_scenes(content, logger)

    # Validate content and generate warnings/feedback
    validation_results = validate_episode_content(content, scenes, config, logger)

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
        "warnings": validation_results["warnings"],
        "feedback": validation_results["feedback"],
    }

    logger.info(f"Parsed episode: {parsed_data['episode_metadata']['title']}")
    logger.info(f"Content length: {len(content)} characters")
    logger.info(f"Total scenes: {len(scenes)}")

    return parsed_data


def validate_episode_content(
    content: str,
    scenes: List[Dict[str, Any]],
    config: Dict[str, Any],
    logger: logging.Logger,
) -> Dict[str, Any]:
    """Validate episode content and generate warnings/feedback."""
    validation_config = config.get("validation", {})
    warnings = []
    feedback = {
        "missing_tags": [],
        "format_violations": [],
        "quality_suggestions": [],
    }

    # Check for required scenes
    if not scenes:
        warnings.append("No scene markers found. Expected format: ## **[SCENE: NAME]**")
        feedback["format_violations"].append("Missing scene structure")

    # Check for required characters
    required_characters = validation_config.get(
        "required_characters", ["THORAK", "ZARA"]
    )
    found_characters = set()

    # Collect all dialogues for character validation
    total_dialogues = 0
    total_character_count = 0
    scene_dialogue_counts = []

    for scene in scenes:
        scene_dialogues = len(scene.get("dialogues", []))
        total_dialogues += scene_dialogues
        scene_dialogue_counts.append(scene_dialogues)

        for dialogue in scene.get("dialogues", []):
            found_characters.add(dialogue["character"])
            total_character_count += dialogue["character_count"]

    # Check for missing required characters
    missing_characters = set(required_characters) - found_characters
    if missing_characters:
        for char in missing_characters:
            warnings.append(f"Required character '{char}' not found in any dialogue")
            feedback["missing_tags"].append(f"Character: {char}")

    # Check multimedia tag usage
    required_multimedia = validation_config.get("multimedia_tags", [])
    found_multimedia = set()
    multimedia_counts = {}

    for scene in scenes:
        multimedia = scene.get("multimedia", {})
        for tag_type, tags in multimedia.items():
            if tags:  # If there are any tags of this type
                # Map tag types to config format
                tag_mapping = {
                    "image_tags": "IMG:",
                    "sfx_tags": "SFX:",
                    "music_tags": "MUSIC:",
                    "ambient_tags": "AMBIENT:",
                    "transition_tags": "TRANSITION:",
                }
                tag_name = tag_mapping.get(
                    tag_type, tag_type.replace("_tags", "").upper() + ":"
                )
                found_multimedia.add(tag_name)
                multimedia_counts[tag_name] = multimedia_counts.get(tag_name, 0) + len(
                    tags
                )

    # Check for missing multimedia types
    missing_multimedia = set(required_multimedia) - found_multimedia
    if missing_multimedia and validation_config.get("warning_on_missing_tags", True):
        for tag in missing_multimedia:
            warnings.append(f"No {tag} tags found in episode")
            feedback["missing_tags"].append(f"Multimedia: {tag}")

    # Content quality checks
    if total_dialogues < 10:
        feedback["quality_suggestions"].append(
            f"Episode has only {total_dialogues} dialogues - consider adding more content"
        )

    if total_character_count < 1000:
        feedback["quality_suggestions"].append(
            f"Episode has only {total_character_count} characters - may be too short for podcast format"
        )

    # Check for scene balance
    if scenes:
        avg_dialogues_per_scene = total_dialogues / len(scenes)
        if avg_dialogues_per_scene < 2:
            feedback["quality_suggestions"].append(
                "Some scenes have very few dialogues - consider consolidating or expanding"
            )

        # Check for scenes with no dialogues
        empty_scenes = [
            scene["scene_name"]
            for scene in scenes
            if len(scene.get("dialogues", [])) == 0
        ]
        if empty_scenes:
            for scene_name in empty_scenes:
                warnings.append(f"Scene '{scene_name}' contains no dialogue")
                feedback["format_violations"].append(f"Empty scene: {scene_name}")

    # Check dialogue format compliance
    for scene in scenes:
        for dialogue in scene.get("dialogues", []):
            # Check for very short dialogues
            if dialogue["character_count"] < 5:
                feedback["quality_suggestions"].append(
                    f"Very short dialogue in {scene['scene_name']}: '{dialogue['text'][:50]}'"
                )

            # Check for very long dialogues (potential formatting issues)
            if dialogue["character_count"] > 1000:
                warnings.append(
                    f"Extremely long dialogue in {scene['scene_name']} ({dialogue['character_count']} chars) - check for formatting errors"
                )
                feedback["format_violations"].append(
                    f"Oversized dialogue in {scene['scene_name']}"
                )

    # Check multimedia distribution
    scenes_with_images = sum(
        1 for scene in scenes if scene.get("multimedia", {}).get("image_tags", [])
    )
    if scenes_with_images == 0:
        warnings.append(
            "No image tags found in any scene - visual content may be missing"
        )
        feedback["missing_tags"].append("Images: No visual content")
    elif (
        scenes_with_images < len(scenes) * 0.5
    ):  # Less than half the scenes have images
        feedback["quality_suggestions"].append(
            f"Only {scenes_with_images}/{len(scenes)} scenes have images - consider adding more visual content"
        )

    # Log validation summary
    logger.info(
        f"Content validation: {len(warnings)} warnings, {len(feedback['missing_tags']) + len(feedback['format_violations']) + len(feedback['quality_suggestions'])} feedback items"
    )

    return {"warnings": warnings, "feedback": feedback}


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


def calculate_detailed_costs(
    scenes: List[Dict[str, Any]], config: Dict[str, Any]
) -> Dict[str, Any]:
    """Calculate detailed cost breakdown for all pipeline components."""
    cost_config = config.get("cost_estimation", {})

    # Voice generation costs (ElevenLabs)
    character_stats = calculate_character_counts(scenes)
    elevenlabs_cost_per_char = cost_config.get("elevenlabs_cost_per_character", 0.0003)
    voice_generation_cost = (
        character_stats["total_characters"] * elevenlabs_cost_per_char
    )

    # Voice costs by speaker
    voice_costs_by_speaker = {}
    for speaker, char_count in character_stats["by_speaker"].items():
        voice_costs_by_speaker[speaker] = char_count * elevenlabs_cost_per_char

    # Multimedia costs
    multimedia_stats = calculate_multimedia_counts(scenes)
    image_cost_per_prompt = cost_config.get("image_generation_cost_per_prompt", 0.05)
    sfx_cost_per_effect = cost_config.get("sfx_cost_per_effect", 0.02)
    music_cost_per_cue = cost_config.get("music_cost_per_cue", 0.10)

    image_generation_cost = (
        multimedia_stats["image_generation_count"] * image_cost_per_prompt
    )
    sfx_processing_cost = multimedia_stats["sfx_count"] * sfx_cost_per_effect
    music_processing_cost = multimedia_stats["music_cue_count"] * music_cost_per_cue
    ambient_processing_cost = (
        multimedia_stats["ambient_count"] * sfx_cost_per_effect
    )  # Same rate as SFX
    transition_processing_cost = (
        multimedia_stats["transition_count"] * sfx_cost_per_effect
    )  # Same rate as SFX

    # Total audio processing cost
    audio_processing_cost = (
        sfx_processing_cost
        + music_processing_cost
        + ambient_processing_cost
        + transition_processing_cost
    )

    # Total episode cost
    total_episode_cost = (
        voice_generation_cost + image_generation_cost + audio_processing_cost
    )

    # Cost breakdown by pipeline component
    pipeline_costs = {
        "step_1_script_parsing": 0.0,  # No cost for parsing
        "step_2_voice_generation": voice_generation_cost,
        "step_3_image_generation": image_generation_cost,
        "step_4_cost_estimation": 0.0,  # No cost for cost estimation
        "step_5_audio_processing": audio_processing_cost,
        "step_6_quality_assurance": 0.0,  # No cost for QA
        "step_7_video_assembly": 0.0,  # No external cost for video assembly
        "step_8_distribution": 0.0,  # No cost for distribution processing
    }

    return {
        "total_episode_cost": round(total_episode_cost, 4),
        "currency": cost_config.get("currency", "USD"),
        "cost_breakdown": {
            "voice_generation": {
                "total_cost": round(voice_generation_cost, 4),
                "cost_per_character": elevenlabs_cost_per_char,
                "total_characters": character_stats["total_characters"],
                "costs_by_speaker": {
                    speaker: round(cost, 4)
                    for speaker, cost in voice_costs_by_speaker.items()
                },
            },
            "image_generation": {
                "total_cost": round(image_generation_cost, 4),
                "cost_per_image": image_cost_per_prompt,
                "total_images": multimedia_stats["image_generation_count"],
            },
            "audio_processing": {
                "total_cost": round(audio_processing_cost, 4),
                "sfx_cost": round(sfx_processing_cost, 4),
                "music_cost": round(music_processing_cost, 4),
                "ambient_cost": round(ambient_processing_cost, 4),
                "transition_cost": round(transition_processing_cost, 4),
                "breakdown": {
                    "sfx_count": multimedia_stats["sfx_count"],
                    "music_count": multimedia_stats["music_cue_count"],
                    "ambient_count": multimedia_stats["ambient_count"],
                    "transition_count": multimedia_stats["transition_count"],
                },
            },
        },
        "pipeline_component_costs": pipeline_costs,
        "cost_per_minute": round(
            total_episode_cost
            / (
                config.get("episode_settings", {}).get(
                    "expected_characters_per_minute", 200
                )
                / 60
            ),
            4,
        )
        if total_episode_cost > 0
        else 0.0,
    }


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


def calculate_timing_estimates(
    scenes: List[Dict[str, Any]], config: Dict[str, Any]
) -> Dict[str, Any]:
    """Calculate timing estimates for dialogue and scenes."""
    episode_settings = config.get("episode_settings", {})
    speech_rate = episode_settings.get("default_speech_rate_words_per_minute", 150)
    pause_between_speakers = episode_settings.get(
        "pause_duration_between_speakers_seconds", 0.5
    )
    scene_transition_duration = episode_settings.get(
        "scene_transition_duration_seconds", 1.0
    )

    total_dialogue_duration = 0
    total_words = 0
    scene_timings = []

    for scene in scenes:
        scene_dialogue_duration = 0
        scene_words = 0
        dialogue_count = len(scene.get("dialogues", []))

        # Calculate dialogue duration for this scene
        for dialogue in scene.get("dialogues", []):
            text = dialogue["text"]
            # Estimate words (simple split by spaces)
            words = len(text.split())
            scene_words += words

            # Calculate speech duration (words per minute to seconds)
            speech_duration = (words / speech_rate) * 60
            scene_dialogue_duration += speech_duration

        # Add pauses between speakers (one less pause than dialogue count)
        if dialogue_count > 1:
            scene_dialogue_duration += (dialogue_count - 1) * pause_between_speakers

        # Store scene timing data
        scene_timing = {
            "scene_id": scene["scene_id"],
            "dialogue_duration_seconds": round(scene_dialogue_duration, 2),
            "word_count": scene_words,
            "dialogue_count": dialogue_count,
            "estimated_reading_speed_wpm": speech_rate,
        }
        scene_timings.append(scene_timing)

        total_dialogue_duration += scene_dialogue_duration
        total_words += scene_words

    # Add scene transition time (between scenes, not before first or after last)
    num_scene_transitions = max(0, len(scenes) - 1)
    total_transition_duration = num_scene_transitions * scene_transition_duration

    # Calculate total episode duration
    total_duration = total_dialogue_duration + total_transition_duration

    timing_data = {
        "total_duration_seconds": round(total_duration, 2),
        "total_duration_minutes": round(total_duration / 60, 2),
        "dialogue_duration_seconds": round(total_dialogue_duration, 2),
        "transition_duration_seconds": round(total_transition_duration, 2),
        "total_words": total_words,
        "average_speech_rate_wpm": speech_rate,
        "scene_count": len(scenes),
        "scene_timings": scene_timings,
    }

    return timing_data


def load_output_schema() -> Dict[str, Any]:
    """Load the JSON schema for output validation."""
    schema_path = Path("schema/output_schema.json")
    try:
        with open(schema_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # No schema validation if file not found
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in schema file {schema_path}: {e}")


def validate_output_against_schema(
    output_data: Dict[str, Any], logger: logging.Logger
) -> List[str]:
    """Validate output data against JSON schema. Returns list of validation errors."""
    if not SCHEMA_VALIDATION_AVAILABLE:
        logger.warning("jsonschema package not available - skipping schema validation")
        return []

    schema = load_output_schema()
    if not schema:
        logger.warning("Output schema not found - skipping schema validation")
        return []

    errors = []
    try:
        jsonschema.validate(output_data, schema)
        logger.info("✓ Output validates against JSON schema")
    except jsonschema.ValidationError as e:
        error_msg = f"Schema validation error: {e.message} at {'.'.join(str(p) for p in e.absolute_path)}"
        errors.append(error_msg)
        logger.error(error_msg)
    except jsonschema.SchemaError as e:
        error_msg = f"Schema definition error: {e.message}"
        errors.append(error_msg)
        logger.error(error_msg)

    return errors


def determine_validation_status(
    warnings: List[str], feedback: Dict[str, Any], config: Dict[str, Any]
) -> str:
    """Determine overall validation status based on warnings and feedback."""
    validation_config = config.get("validation", {})
    fail_on_critical = validation_config.get("fail_on_critical_errors", False)

    # Count different types of issues
    critical_errors = len(
        [w for w in warnings if "missing" in w.lower() or "no scene" in w.lower()]
    )
    format_violations = len(feedback.get("format_violations", []))

    if fail_on_critical and critical_errors > 0:
        return "failed"
    elif warnings or format_violations > 0:
        return "warning"
    else:
        return "passed"


def generate_output_metadata(
    input_path: Path,
    processing_time: float,
    scenes: List[Dict[str, Any]],
    config: Dict[str, Any],
) -> Dict[str, Any]:
    """Generate metadata for the parsed output."""
    character_stats = calculate_character_counts(scenes)
    multimedia_stats = calculate_multimedia_counts(scenes)
    timing_stats = calculate_timing_estimates(scenes, config)
    detailed_costs = calculate_detailed_costs(scenes, config)

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
        "detailed_cost_analysis": detailed_costs,
        "timing_estimates": timing_stats,
        "validation_status": "passed",  # Will be determined by validation and schema checks
        "character_count_by_speaker": character_stats["by_speaker"],
    }


def save_output_files(
    parsed_data: Dict[str, Any],
    metadata: Dict[str, Any],
    output_path: Path,
    episode_name: str,
    debug: bool,
    logger: logging.Logger,
    config: Dict[str, Any],
) -> None:
    """Save the parsed data and metadata to output files."""

    # Combine parsed data with metadata
    output_data = {"metadata": metadata, **parsed_data}

    # Determine content validation status first
    content_validation_status = determine_validation_status(
        parsed_data.get("warnings", []), parsed_data.get("feedback", {}), config
    )

    # Validate against schema and update metadata
    schema_errors = validate_output_against_schema(output_data, logger)
    if schema_errors:
        final_status = "failed"
        # Add schema errors to warnings
        if "warnings" not in parsed_data:
            parsed_data["warnings"] = []
        parsed_data["warnings"].extend(
            [f"Schema validation: {error}" for error in schema_errors]
        )
        # Recreate output data with updated metadata and warnings
        output_data = {"metadata": metadata, **parsed_data}
    else:
        # Use content validation status if schema validation passes
        final_status = content_validation_status

    # Update final validation status
    metadata["validation_status"] = final_status

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

        # Include schema validation results
        if schema_errors:
            file.write("SCHEMA VALIDATION ERRORS:\n")
            for error in schema_errors:
                file.write(f"  - {error}\n")
            file.write("\n")

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
        print(f"💡 Using default configuration to continue processing...")
        config = load_config()  # This will return default config on error
        print(f"✓ Default configuration loaded successfully")

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
        # Step 1: Validate input file
        logger.info(f"🔍 Step 1: Validating input file...")
        input_path = validate_input_file(args.input_file)
        logger.info(f"✓ Input file validated: {input_path}")

        # Step 2: Prepare output directory
        logger.info(f"📁 Step 2: Preparing output directory...")
        output_path = ensure_output_directory(args.output_dir, args.debug)
        logger.info(f"✓ Output directory ready: {output_path}")

        # Step 3: Parse the episode script
        logger.info(f"📖 Step 3: Parsing episode script...")
        parsed_data = parse_episode_script(input_path, logger, config)
        scene_count = len(parsed_data.get("scenes", []))
        logger.info(f"✓ Episode parsing complete - found {scene_count} scenes")

        # Step 4: Generate metadata and cost estimates
        logger.info(f"📊 Step 4: Generating metadata and cost estimates...")
        processing_time = time.time() - start_time
        metadata = generate_output_metadata(
            input_path, processing_time, parsed_data["scenes"], config
        )

        # Show cost summary
        cost_data = metadata.get("detailed_cost_analysis", {})
        total_cost = cost_data.get("total_episode_cost", 0)
        total_chars = metadata.get("estimated_downstream_costs", {}).get(
            "elevenlabs_character_count", 0
        )
        logger.info(
            f"✓ Cost analysis complete - estimated ${total_cost:.2f} ({total_chars} characters)"
        )

        # Step 5: Save output files
        logger.info(f"💾 Step 5: Saving output files...")
        episode_name = input_path.stem
        save_output_files(
            parsed_data, metadata, output_path, episode_name, args.debug, logger, config
        )

        # Final status with summary
        validation_status = metadata.get("validation_status", "unknown")
        warnings_count = len(parsed_data.get("warnings", []))

        logger.info(f"✅ Parsing complete in {processing_time:.3f}s")
        logger.info(f"📄 Output: {output_path / f'{episode_name}.json'}")
        logger.info(
            f"🎯 Status: {validation_status.upper()} ({warnings_count} warnings)"
        )

        if validation_status == "failed":
            logger.info(f"❌ Processing completed with errors - check validation report")
            return 1
        elif validation_status == "warning":
            logger.info(
                f"⚠️ Processing completed with warnings - review validation report"
            )
        else:
            logger.info(f"🎉 Processing completed successfully!")

        return 0

    except FileNotFoundError as e:
        logger.error(f"❌ Input file not found: {e}")
        logger.info(f"💡 Please check the file path and try again")
        return 1
    except ValueError as e:
        logger.error(f"❌ Input validation error: {e}")
        logger.info(f"💡 Please ensure the file is a valid markdown (.md) file")
        return 1
    except UnicodeDecodeError as e:
        logger.error(f"❌ File encoding error: {e}")
        logger.info(f"💡 Please ensure the file is saved with UTF-8 encoding")
        # Try to create emergency output with error details
        try:
            emergency_output_path = ensure_output_directory(args.output_dir, args.debug)
            emergency_data = {
                "metadata": {
                    "processing_timestamp": datetime.now().isoformat(),
                    "input_file_path": args.input_file,
                    "total_processing_time_seconds": time.time() - start_time,
                    "validation_status": "failed",
                    "error_type": "encoding_error",
                },
                "episode_metadata": {
                    "title": "Processing Failed",
                    "number": "error",
                    "input_file": args.input_file,
                    "total_scenes": 0,
                },
                "scenes": [],
                "warnings": [f"File encoding error: {str(e)}"],
                "feedback": {
                    "missing_tags": [],
                    "format_violations": ["File could not be read with UTF-8 encoding"],
                    "quality_suggestions": [
                        "Save file with UTF-8 encoding and try again"
                    ],
                },
            }

            output_name = Path(args.input_file).stem
            with open(
                emergency_output_path / f"{output_name}.json", "w", encoding="utf-8"
            ) as f:
                json.dump(emergency_data, f, indent=2, ensure_ascii=False)
            logger.info(f"✓ Emergency output saved with error details")
        except Exception:
            pass  # If emergency save fails, continue gracefully
        return 1
    except Exception as e:
        logger.error(f"❌ Unexpected error during processing: {e}")
        if args.debug:
            logger.exception("Full error details:")

        # Try to create emergency output even for unexpected errors
        try:
            emergency_output_path = ensure_output_directory(args.output_dir, args.debug)
            emergency_data = {
                "metadata": {
                    "processing_timestamp": datetime.now().isoformat(),
                    "input_file_path": args.input_file,
                    "total_processing_time_seconds": time.time() - start_time,
                    "validation_status": "failed",
                    "error_type": "unexpected_error",
                },
                "episode_metadata": {
                    "title": "Processing Failed",
                    "number": "error",
                    "input_file": args.input_file,
                    "total_scenes": 0,
                },
                "scenes": [],
                "warnings": [f"Unexpected error: {str(e)}"],
                "feedback": {
                    "missing_tags": [],
                    "format_violations": ["Parser encountered an unexpected error"],
                    "quality_suggestions": [
                        "Please report this error with the input file for investigation"
                    ],
                },
            }

            output_name = Path(args.input_file).stem
            with open(
                emergency_output_path / f"{output_name}.json", "w", encoding="utf-8"
            ) as f:
                json.dump(emergency_data, f, indent=2, ensure_ascii=False)
            logger.info(f"✓ Emergency output saved with error details")
            logger.info(f"💡 Partial JSON output available for debugging")
        except Exception:
            logger.error(f"❌ Failed to create emergency output")

        return 1


if __name__ == "__main__":
    sys.exit(main())
