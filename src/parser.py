#!/usr/bin/env python3
"""
versusMonster Script Parser - Step 1 of 8-Component Pipeline
Transforms markdown podcast scripts into structured JSON for downstream processing.

PRD-v0 Command: python parser.py episode_007.md
"""

import argparse
import json
import logging
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any


def setup_logging(debug: bool = False) -> logging.Logger:
    """Set up logging configuration."""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
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

    # Placeholder parsing result - will be implemented in subsequent tasks
    parsed_data = {
        "episode_metadata": {
            "title": f"Episode {episode_number.replace('episode_', '').replace('_', ' ').title()}",
            "number": episode_number,
            "input_file": str(input_path.absolute()),
            "content_preview": content[:200] + "..." if len(content) > 200 else content,
        },
        "scenes": [],  # Will be populated in Task 2.1
        "warnings": [],
        "feedback": {
            "missing_tags": [],
            "format_violations": [],
            "quality_suggestions": [],
        },
    }

    logger.info(f"Parsed episode: {parsed_data['episode_metadata']['title']}")
    logger.info(f"Content length: {len(content)} characters")

    return parsed_data


def generate_output_metadata(
    input_path: Path, processing_time: float
) -> Dict[str, Any]:
    """Generate metadata for the parsed output."""
    return {
        "processing_timestamp": datetime.now().isoformat(),
        "input_file_path": str(input_path.absolute()),
        "total_processing_time_seconds": round(processing_time, 3),
        "estimated_downstream_costs": {
            "elevenlabs_character_count": 0,  # Will be calculated in Task 4.1
            "image_generation_count": 0,  # Will be calculated in Task 2.3
            "sfx_count": 0,  # Will be calculated in Task 2.3
            "music_cue_count": 0,  # Will be calculated in Task 2.3
        },
        "validation_status": "passed",  # Will be determined in Task 5.1
        "character_count_by_speaker": {},  # Will be calculated in Task 4.1
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
        help="Enable debug mode with intermediate output files",
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        default="output/json",
        help="Custom output directory (default: output/json)",
    )

    parser.add_argument(
        "--version", action="version", version="versusMonster Script Parser v1.0"
    )

    args = parser.parse_args()

    # Set up logging
    logger = setup_logging(args.debug)
    logger.info("🚀 versusMonster Script Parser v1.0 - Step 1 of 8-Component Pipeline")

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
        metadata = generate_output_metadata(input_path, processing_time)

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
