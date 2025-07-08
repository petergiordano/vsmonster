#!/usr/bin/env python3
"""
versusMonster Cost Estimation Reporter
Generates detailed cost analysis reports from parsed episode data.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Any


def generate_cost_report(episode_data: Dict[str, Any], output_path: Path = None) -> str:
    """Generate a formatted cost estimation report."""
    metadata = episode_data.get("metadata", {})
    episode_info = episode_data.get("episode_metadata", {})
    cost_analysis = metadata.get("detailed_cost_analysis", {})
    timing = metadata.get("timing_estimates", {})

    # Report header
    report_lines = [
        "=" * 80,
        "VERSUSMONSTER AVPS COST ESTIMATION REPORT",
        "=" * 80,
        "",
        f"Episode: {episode_info.get('title', 'Unknown')}",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Estimated Duration: {timing.get('total_duration_minutes', 0):.2f} minutes",
        f"Total Characters: {metadata.get('estimated_downstream_costs', {}).get('elevenlabs_character_count', 0):,}",
        "",
        "=" * 80,
        "COST BREAKDOWN SUMMARY",
        "=" * 80,
        "",
    ]

    # Total cost summary
    total_cost = cost_analysis.get("total_episode_cost", 0)
    currency = cost_analysis.get("currency", "USD")
    cost_per_minute = cost_analysis.get("cost_per_minute", 0)

    report_lines.extend(
        [
            f"💰 TOTAL EPISODE COST: ${total_cost:.4f} {currency}",
            f"📊 Cost per Minute: ${cost_per_minute:.4f} {currency}",
            "",
        ]
    )

    # Pipeline component costs
    pipeline_costs = cost_analysis.get("pipeline_component_costs", {})
    if pipeline_costs:
        report_lines.extend(
            [
                "PIPELINE COMPONENT COSTS:",
                "-" * 40,
            ]
        )

        for step, cost in pipeline_costs.items():
            step_name = step.replace("_", " ").title()
            if cost > 0:
                report_lines.append(f"  {step_name}: ${cost:.4f} {currency}")
            else:
                report_lines.append(f"  {step_name}: No external costs")
        report_lines.append("")

    # Detailed cost breakdowns
    cost_breakdown = cost_analysis.get("cost_breakdown", {})

    # Voice Generation Details
    voice_costs = cost_breakdown.get("voice_generation", {})
    if voice_costs:
        report_lines.extend(
            [
                "🎤 VOICE GENERATION (ElevenLabs):",
                "-" * 40,
                f"  Total Cost: ${voice_costs.get('total_cost', 0):.4f} {currency}",
                f"  Cost per Character: ${voice_costs.get('cost_per_character', 0):.6f} {currency}",
                f"  Total Characters: {voice_costs.get('total_characters', 0):,}",
                "",
                "  Costs by Speaker:",
            ]
        )

        speaker_costs = voice_costs.get("costs_by_speaker", {})
        for speaker, cost in speaker_costs.items():
            char_count = metadata.get("character_count_by_speaker", {}).get(speaker, 0)
            report_lines.append(
                f"    {speaker}: ${cost:.4f} ({char_count:,} characters)"
            )
        report_lines.append("")

    # Image Generation Details
    image_costs = cost_breakdown.get("image_generation", {})
    if image_costs:
        report_lines.extend(
            [
                "🖼️  IMAGE GENERATION:",
                "-" * 40,
                f"  Total Cost: ${image_costs.get('total_cost', 0):.4f} {currency}",
                f"  Cost per Image: ${image_costs.get('cost_per_image', 0):.4f} {currency}",
                f"  Total Images: {image_costs.get('total_images', 0)}",
                "",
            ]
        )

    # Audio Processing Details
    audio_costs = cost_breakdown.get("audio_processing", {})
    if audio_costs:
        breakdown = audio_costs.get("breakdown", {})
        report_lines.extend(
            [
                "🎵 AUDIO PROCESSING:",
                "-" * 40,
                f"  Total Cost: ${audio_costs.get('total_cost', 0):.4f} {currency}",
                "",
                "  Breakdown by Type:",
                f"    SFX: ${audio_costs.get('sfx_cost', 0):.4f} ({breakdown.get('sfx_count', 0)} effects)",
                f"    Music: ${audio_costs.get('music_cost', 0):.4f} ({breakdown.get('music_count', 0)} cues)",
                f"    Ambient: ${audio_costs.get('ambient_cost', 0):.4f} ({breakdown.get('ambient_count', 0)} tracks)",
                f"    Transitions: ${audio_costs.get('transition_cost', 0):.4f} ({breakdown.get('transition_count', 0)} transitions)",
                "",
            ]
        )

    # Content Statistics
    scenes = episode_data.get("scenes", [])
    total_dialogues = sum(len(scene.get("dialogues", [])) for scene in scenes)

    report_lines.extend(
        [
            "📈 CONTENT STATISTICS:",
            "-" * 40,
            f"  Total Scenes: {len(scenes)}",
            f"  Total Dialogues: {total_dialogues}",
            f"  Average Dialogues per Scene: {total_dialogues / len(scenes):.1f}"
            if scenes
            else "  Average Dialogues per Scene: 0",
            f"  Processing Time: {metadata.get('total_processing_time_seconds', 0):.3f} seconds",
            "",
        ]
    )

    # Cost Efficiency Metrics
    if total_cost > 0 and timing.get("total_duration_minutes", 0) > 0:
        chars_per_dollar = (
            metadata.get("estimated_downstream_costs", {}).get(
                "elevenlabs_character_count", 0
            )
            / total_cost
        )
        minutes_per_dollar = timing.get("total_duration_minutes", 0) / total_cost

        report_lines.extend(
            [
                "📊 EFFICIENCY METRICS:",
                "-" * 40,
                f"  Characters per Dollar: {chars_per_dollar:.0f}",
                f"  Minutes per Dollar: {minutes_per_dollar:.2f}",
                "",
            ]
        )

    # Scene-by-scene breakdown
    scene_timings = timing.get("scene_timings", [])
    if scene_timings:
        report_lines.extend(
            [
                "🎬 SCENE-BY-SCENE BREAKDOWN:",
                "-" * 40,
            ]
        )

        for scene_timing in scene_timings:
            scene_id = scene_timing.get("scene_id", "unknown")
            duration = scene_timing.get("dialogue_duration_seconds", 0)
            dialogue_count = scene_timing.get("dialogue_count", 0)
            word_count = scene_timing.get("word_count", 0)

            report_lines.append(
                f"  {scene_id.replace('_', ' ').title()}: "
                f"{duration:.1f}s, {dialogue_count} dialogues, {word_count} words"
            )
        report_lines.append("")

    # Footer
    report_lines.extend(
        [
            "=" * 80,
            "Report generated by versusMonster AVPS Cost Estimation System",
            f"Timestamp: {metadata.get('processing_timestamp', 'Unknown')}",
            "=" * 80,
        ]
    )

    report_text = "\n".join(report_lines)

    # Save to file if output path provided
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report_text)

    return report_text


def main():
    """Command line interface for cost report generation."""
    if len(sys.argv) != 2:
        print("Usage: python cost_reporter.py <episode_json_file>")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            episode_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {input_file}: {e}")
        sys.exit(1)

    # Generate report
    output_file = input_file.parent / f"{input_file.stem}_cost_report.txt"
    report = generate_cost_report(episode_data, output_file)

    print(f"✓ Cost report generated: {output_file}")
    print("\n" + "=" * 50)
    print("COST REPORT PREVIEW:")
    print("=" * 50)
    print(report[:1000] + "..." if len(report) > 1000 else report)


if __name__ == "__main__":
    main()
