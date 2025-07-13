# versusMonster Script Parser - JSON Output Schema Documentation

## Overview

This document describes the JSON output format from the versusMonster Script Parser (Step 1 of the 8-component AVPS pipeline). The schema ensures consistent data structure for downstream processing components.

## Schema Location

- **Schema File:** `schema/output_schema.json`
- **Schema ID:** `https://versusmonster.com/schemas/parser-output.json`
- **JSON Schema Version:** Draft 07

## Top-Level Structure

```json
{
  "metadata": { ... },           // Processing and cost estimation data
  "episode_metadata": { ... },   // Episode identification
  "scenes": [ ... ],             // Ordered scene data
  "warnings": [ ... ],           // Non-fatal parsing issues
  "feedback": { ... }            // Quality and formatting feedback
}
```

## Data Sections

### 1. Metadata Section

Contains processing statistics and downstream cost estimation data.

**Key Fields for Pipeline Components:**

- `estimated_downstream_costs.elevenlabs_character_count` → **Voice Generation (Step 2)**
- `estimated_downstream_costs.image_generation_count` → **Image Generation (Step 3)**
- `timing_estimates.total_duration_seconds` → **Video Assembly (Step 7)**
- `character_count_by_speaker` → **Voice Generation cost breakdown**

**Example:**
```json
{
  "metadata": {
    "processing_timestamp": "2025-07-07T16:03:12.361005",
    "input_file_path": "/path/to/episode_007.md",
    "total_processing_time_seconds": 0.01,
    "estimated_downstream_costs": {
      "elevenlabs_character_count": 10192,
      "image_generation_count": 13,
      "sfx_count": 4,
      "music_cue_count": 5,
      "ambient_count": 3,
      "transition_count": 3
    },
    "timing_estimates": {
      "total_duration_seconds": 659.5,
      "total_duration_minutes": 10.99,
      "scene_timings": [...]
    },
    "validation_status": "passed"
  }
}
```

### 2. Episode Metadata Section

Basic episode identification and preview information.

**Fields:**
- `title`: Human-readable episode title
- `number`: Episode identifier (e.g., "episode_007")
- `input_file`: Source markdown file path
- `content_preview`: First 200-500 characters
- `total_scenes`: Number of scenes parsed

### 3. Scenes Array

Ordered list of episode scenes with complete parsing data.

**Scene Structure:**
```json
{
  "scene_id": "cold_open",           // Normalized identifier
  "scene_name": "COLD OPEN",         // Original name from markdown
  "start_line": 24,                  // Line number in source
  "content": "...",                  // Raw scene content
  "dialogues": [...],                // Parsed dialogue lines
  "multimedia": {...},               // Multimedia tags
  "metadata": {...}                  // Scene statistics
}
```

#### Dialogue Objects

**Usage:** Voice Generation (Step 2), Cost Estimation (Step 4)

```json
{
  "character": "THORAK",                    // Speaker name
  "direction": "Gravelly, impressed",      // Optional stage direction
  "text": "Aye, lass, that's...",            // Text for voice synthesis
  "character_count": 98,                   // For cost calculation
  "line_position": 7                       // Position in scene
}
```

**Character Names:** Always uppercase (THORAK, ZARA, BOTH)
**Direction:** Nullable string for delivery instructions
**Text:** Raw dialogue text ready for voice synthesis

#### Multimedia Objects

**Structure by Type:**

**Image Tags** → Image Generation (Step 3)
```json
{
  "tag_id": "cold_open_leap",
  "prompt": "Massive armored bulette...",    // Generation prompt
  "line_position": 3,
  "tag_type": "image"
}
```

**Audio Tags** → Audio Processing (Step 5)
```json
{
  "tag_id": "earth_rumbling_deep",
  "line_position": 1,
  "tag_type": "sfx"                        // "sfx", "music", "ambient", "transition"
}
```

### 4. Warnings and Feedback

**Warnings:** Non-fatal parsing issues that don't prevent processing
**Feedback:** Quality suggestions and format compliance notes

## Pipeline Component Usage

### Step 2: Voice Generation (ElevenLabs)
- **Primary Data:** `scenes[].dialogues[]`
- **Cost Estimation:** `metadata.estimated_downstream_costs.elevenlabs_character_count`
- **Speaker Breakdown:** `metadata.character_count_by_speaker`
- **Timing Context:** `metadata.timing_estimates.scene_timings[]`

### Step 3: Image Generation
- **Primary Data:** `scenes[].multimedia.image_tags[]`
- **Cost Estimation:** `metadata.estimated_downstream_costs.image_generation_count`
- **Generation Prompts:** Each `image_tags[].prompt` field

### Step 4: Cost Estimation & Reporting
- **All Cost Data:** `metadata.estimated_downstream_costs`
- **Timing Data:** `metadata.timing_estimates`
- **Character Breakdown:** `metadata.character_count_by_speaker`

### Step 5: Audio Processing
- **Audio Cues:** All `scenes[].multimedia.*_tags[]` where type != "image"
- **Timing Context:** `metadata.timing_estimates.scene_timings[]`
- **Positioning:** `line_position` fields for synchronization

### Step 6: Quality Assurance
- **Validation Status:** `metadata.validation_status`
- **Issues:** `warnings[]` and `feedback.*`
- **Schema Compliance:** Validated against `schema/output_schema.json`

### Step 7: Video Assembly
- **Complete Structure:** All sections for final video compilation
- **Timing Master:** `metadata.timing_estimates` for synchronization
- **Scene Order:** `scenes[]` array order

### Step 8: Distribution
- **Episode Metadata:** `episode_metadata` section
- **Duration:** `metadata.timing_estimates.total_duration_minutes`
- **Content Preview:** `episode_metadata.content_preview`

## Validation

The parser automatically validates output against the JSON schema:

- **Schema File:** `schema/output_schema.json`
- **Validation Library:** jsonschema (Python)
- **Validation Status:** Recorded in `metadata.validation_status`
- **Error Reporting:** Schema errors added to `warnings[]`

**Validation Levels:**
- `"passed"`: Full schema compliance
- `"failed"`: Schema validation errors (details in warnings)
- `"warning"`: Minor issues that don't break schema

## Schema Evolution

**Version:** 1.0 (Initial implementation)
**Backwards Compatibility:** Maintained for pipeline stability
**Extension Policy:** New optional fields may be added; required fields remain stable

## Example Usage

### Reading Dialogue for Voice Generation
```python
with open("output/json/episode_007.json") as f:
    data = json.load(f)

for scene in data["scenes"]:
    for dialogue in scene["dialogues"]:
        character = dialogue["character"]
        text = dialogue["text"]
        direction = dialogue.get("direction")
        # Process for ElevenLabs API
```

### Extracting Image Prompts
```python
image_prompts = []
for scene in data["scenes"]:
    for img_tag in scene["multimedia"]["image_tags"]:
        image_prompts.append({
            "id": img_tag["tag_id"],
            "prompt": img_tag["prompt"],
            "scene": scene["scene_id"]
        })
```

### Cost Estimation Access
```python
costs = data["metadata"]["estimated_downstream_costs"]
total_characters = costs["elevenlabs_character_count"]
total_images = costs["image_generation_count"]
estimated_voice_cost = total_characters * 0.0003  # Example rate
```

## Schema File Reference

The complete JSON Schema is available at `schema/output_schema.json` and includes:

- **Type Definitions:** All field types and constraints
- **Required Fields:** Mandatory vs. optional fields
- **Validation Rules:** Format, pattern, and range validations
- **Documentation:** Field descriptions and usage notes

For the latest schema version and detailed field specifications, refer to the schema file directly.