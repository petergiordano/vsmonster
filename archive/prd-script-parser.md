# Product Requirements Document: Script Parser (Step 1 of 8-Component Pipeline)

## Introduction/Overview

The Script Parser is **Step 1** of the versusMonster Automated Video Podcast System's 8-component iterative build strategy. Following the PRD-v0 "Function Over Fashion" philosophy, this component transforms markdown podcast scripts into structured JSON data that serves as the foundation for all downstream automation.

**Iterative Build Context**: As Step 1, the Script Parser establishes the data foundation that enables Steps 2-8 (Voice Generation → Audio Assembly → Static Video → Image Transitions → Sound Effects → Background Music → Batch Processing). Each step builds compound value on the previous work.

**Problem Statement**: Raw markdown scripts cannot be directly consumed by voice generation, image creation, or audio assembly services. Manual parsing would eliminate the automation benefits and introduce human error into the pipeline.

**Solution**: A simple, reliable command-line parser that extracts all dialogue, multimedia cues, scene transitions, and timing information from Episode 7 format scripts, producing standardized JSON output that feeds Step 2 (Voice Generation).

## Goals

**Primary Goal (PRD-v0 Alignment)**: Parse markdown → structured JSON to enable Step 2 (Voice Generation)

### Specific Success Criteria
1. **Foundation Goal**: Extract all Thorak/Zara dialogue correctly (validates PRD-v0 Step 1)
2. **Quality Goal**: Parse Episode 7 with 100% accuracy (all tags captured correctly)
3. **Compound Value Goal**: Output JSON serves as foundation for Steps 2-8 without modification
4. **Simplicity Goal**: Single command operation (`python parser.py episode_007.md`)
5. **Validation Goal**: Works reliably with Episode 7 content (PRD-v0 validation standard)
6. **Independence Goal**: Functions completely independently - Step 2 doesn't break if Steps 3-8 aren't built yet

## User Stories

### Primary Users: 8-Component Pipeline (PRD-v0 Iterative Strategy)

**As Step 2 (Voice Generation)**, I want structured dialogue data with character attribution and voice directions so that I can generate accurate character voices via ElevenLabs API without any data transformation.

**As Step 3 (Audio Assembly)**, I want timing information extracted by Step 1 so that I can combine voice files from Step 2 with proper dialogue synchronization.

**As Steps 4-8 (Video Pipeline)**, I want scene markers, image prompts, SFX cues, and music tags parsed by Step 1 so that each subsequent step has the data foundation needed for compound value building.

**As the overall 8-component system**, I want Step 1 to work independently so that I can test and validate the parser in isolation before building Steps 2-8.

### Secondary Users: Content Creators & System Operators

**As a podcast creator**, I want detailed parsing feedback so that I can improve script quality and ensure all required tags are present.

**As a system operator**, I want cost estimates and validation reports so that I can monitor budget usage and system health.

**As a script generator AI**, I want specific feedback on tag compliance so that I can continuously improve output quality.

## Functional Requirements

### Core Parsing Requirements

1. **Script Input Processing**: The parser must accept Episode 7 format markdown files as input and validate file structure before processing.

2. **Scene Extraction**: The parser must identify and extract all `## **[SCENE: SCENE_NAME]**` markers with proper scene boundaries and timing estimates.

3. **Dialogue Processing**: The parser must extract all character dialogue in format `CHARACTER_NAME: (Voice direction) "Dialogue text"` with character attribution, voice directions, and exact dialogue content.

4. **Multimedia Tag Extraction**: The parser must capture all multimedia tags:
   - `[IMG: image_id] PROMPT: "prompt text"` with image ID and full prompt
   - `[SFX: effect_name]` with effect identification
   - `[MUSIC: music_id]` with music cue identification
   - `[AMBIENT: environment_name]` with ambient audio specification
   - `[TRANSITION: description]` with transition details

5. **Timing Calculation**: The parser must estimate timestamp positions for all dialogue and multimedia elements based on dialogue length and natural speech patterns.

6. **Character Analysis**: The parser must count total characters per speaker (THORAK, ZARA) for accurate ElevenLabs cost estimation.

### Output Requirements

7. **JSON Structure Compliance**: The parser must output JSON exactly matching the Pipeline Tag Specification format with all required fields populated.

8. **Metadata Generation**: The parser must include comprehensive metadata object with:
   - `processing_timestamp`: ISO 8601 timestamp of processing
   - `input_file_path`: Absolute path to source markdown file
   - `total_processing_time_seconds`: Actual processing duration
   - `estimated_downstream_costs`: Object with ElevenLabs character count, image generation count, SFX count, music cue count
   - `validation_status`: "passed", "warnings", or "failed"
   - `character_count_by_speaker`: Object with per-character dialogue length

9. **File Output Management**: The parser must save output as `episode_XXX.json` in `/output/json/` directory following established naming conventions.

### Quality Assurance Requirements

10. **Warning Generation**: The parser must generate detailed warnings for any parsing issues, including specific line numbers and correction suggestions, without halting processing.

11. **Validation Reporting**: The parser must create separate validation report as `episode_XXX_validation.txt` alongside JSON output.

12. **Debug Mode Support**: The parser must support debug mode that outputs intermediate parsing steps to `/output/json/debug/` for troubleshooting.

13. **Feedback Loop Integration**: The parser must generate feedback object with arrays for `missing_tags`, `format_violations`, and `quality_suggestions` to improve script generation.

### Performance Requirements

14. **Processing Speed**: The parser must complete processing of any episode (Episode 7 complexity) in under 10 seconds on macOS with standard hardware.

15. **Memory Efficiency**: The parser must process episodes without excessive memory usage or memory leaks during batch processing.

16. **Error Recovery**: The parser must handle malformed input gracefully and continue processing despite individual tag parsing failures.

## Non-Goals (Out of Scope)

- **Multi-Format Support**: Will not support formats other than Episode 7 structure initially
- **Real-Time Processing**: Will not provide streaming or real-time parsing capabilities
- **Advanced AI Analysis**: Will not include content quality scoring or advanced script analysis
- **Direct Service Integration**: Will not directly call ElevenLabs, image generation, or other APIs
- **Script Editing**: Will not modify or correct input scripts - only parsing and feedback
- **Batch Processing**: Will not handle multiple episodes in single operation
- **Web Interface**: Will not include HTTP API or web-based interface

## Design Considerations

### CLI Interface Design (PRD-v0 Command Structure)
- **Primary Command**: `python parser.py episode_007.md` (matches PRD-v0 specification)
- **File Location**: `/src/parser.py` (follows PRD-v0 file structure)
- **Optional Flags**: `--debug` for debug mode, `--output-dir` for custom output directory
- **Progress Display**: Simple, clear terminal output (Function Over Fashion)
- **Status Feedback**: Clear success/warning/error messages with actionable guidance
- **No UI Complexity**: Pure command-line tool following PRD-v0 philosophy

### Error Handling Strategy
- **Graceful Degradation**: Parse what's possible, warn about issues, never fail completely
- **Detailed Diagnostics**: Line-by-line error reporting with specific correction suggestions
- **Recovery Guidance**: Suggest fixes for common tag format issues

### Performance Optimization
- **Efficient Parsing**: Use regex and string operations optimized for markdown structure
- **Memory Management**: Process file in streaming fashion for large episodes
- **Caching**: Cache regex patterns and reusable parsing components

## Technical Considerations

### Dependencies
- **Python 3.11+**: Modern type hints and performance features
- **Standard Library**: `re`, `json`, `datetime`, `pathlib` for core functionality
- **Markdown Library**: `markdown` or `mistune` for robust markdown parsing
- **Type Checking**: `mypy` compatible type annotations throughout

### Integration Points
- **Input**: Markdown files from `/scripts/` directory
- **Output**: JSON files to `/output/json/` directory
- **Debug Output**: Intermediate files to `/output/json/debug/` directory
- **Validation**: Text reports alongside JSON output

### File Structure Impact (PRD-v0 Compliance)
```
versusMonster/                    # PRD-v0 project root
├── scripts/
│   └── episode_007.md           # Input markdown (PRD-v0 specification)
├── output/
│   ├── json/                    # Step 1 output (PRD-v0 structure)
│   │   ├── episode_007.json     # Primary output for Step 2
│   │   ├── episode_007_validation.txt # Validation report
│   │   └── debug/               # Debug mode outputs
│   ├── voices/                  # Future: Step 2 output
│   ├── audio/                   # Future: Step 3 output
│   └── videos/                  # Future: Step 4+ output
├── src/
│   └── parser.py               # Step 1 implementation (PRD-v0)
└── config.json                 # Simple configuration (PRD-v0)
```

### Error Logging Strategy
- **Structured Logging**: Use Python `logging` module with appropriate levels
- **Performance Metrics**: Log processing time for performance monitoring
- **Validation Results**: Log warning/error counts for quality tracking

## Success Metrics (PRD-v0 Validation Standards)

### PRD-v0 Compliance Metrics
- **Step 1 Functional Test**: Can extract all Thorak/Zara dialogue correctly from Episode 7
- **Step 1 Quality Test**: Output JSON is usable for Step 2 (Voice Generation) without modification
- **Step 1 Reliability Test**: Works consistently with Episode 7 content
- **Step 1 Simplicity Test**: Can run with single command (`python parser.py episode_007.md`)

### Compound Value Building Metrics
- **Foundation Success**: JSON structure supports all Steps 2-8 data requirements
- **Independence Success**: Component works in isolation - no dependency on future steps
- **Integration Success**: Step 2 can successfully consume output without transformation
- **Immediate Value**: Produces testable, validatable output that can be manually reviewed

### Critical Success Factors (PRD-v0 Requirements)
- **Functional**: Produces expected JSON output structure
- **Quality**: Output meets minimum standards for Step 2 consumption
- **Reliable**: Works consistently with Episode 7 content
- **Simple**: Single command operation with clear success/failure feedback

## Executable Success Criteria (Validation Framework)

### Functional Validation Checklist

- [ ] **Episode 7 Complete Parsing (PRD-v0 Step 1 Validation)**
  - **Test Command**: `python parser.py episode_007.md` (PRD-v0 command format)
  - **Expected Result**: Generates `output/json/episode_007.json` with all Thorak/Zara dialogue extracted
  - **Manual Verification**: Verify all dialogue lines match Episode 7 markdown exactly

- [ ] **Character Dialogue Extraction**
  - **Test Command**: `python -c "import json; data=json.load(open('output/json/episode_007.json')); print(f'Thorak lines: {len([d for scene in data[\"scenes\"] for d in scene[\"dialogue\"] if d[\"character\"] == \"THORAK\"])}')`
  - **Expected Result**: Exact count matches manual verification of THORAK dialogue lines
  - **Manual Verification**: Count all "THORAK:" lines in episode_007.md

- [ ] **Multimedia Tag Capture**
  - **Test Command**: `python -c "import json; data=json.load(open('output/json/episode_007.json')); print(f'Images: {sum(len(s[\"images\"]) for s in data[\"scenes\"])}, SFX: {sum(len(s[\"sfx\"]) for s in data[\"scenes\"])}')`
  - **Expected Result**: All [IMG:], [SFX:], [MUSIC:] tags captured with correct IDs and context
  - **Manual Verification**: Count all multimedia tags in episode_007.md

- [ ] **Cost Estimation Accuracy**
  - **Test Command**: `python -c "import json; data=json.load(open('output/json/episode_007.json')); print(data['metadata']['estimated_downstream_costs'])`
  - **Expected Result**: Character count matches actual dialogue length, image count matches [IMG:] tags
  - **Manual Verification**: Validate character count against manual dialogue measurement

### Technical Validation Checklist

- [ ] **Code Quality Standards**
  - **Linting passes**: `flake8 src/parser.py`
  - **Type checking passes**: `mypy src/parser.py`
  - **Formatting standards met**: `black src/parser.py --check`

- [ ] **Test Coverage Requirements**
  - **Unit test coverage ≥ 80%**: `pytest tests/test_parser.py --cov=src.parser`
  - **All parsing functions have tests**: Manual review of test coverage report
  - **Integration tests included**: `pytest tests/test_parser_integration.py`

- [ ] **Performance Requirements**
  - **Episode 7 parses under 10 seconds**: `time python src/parser.py scripts/episode_007.md`
  - **Memory usage stays reasonable**: Monitor memory during processing
  - **No memory leaks in batch processing**: Process Episode 7 multiple times

### User Experience Validation Checklist

- [ ] **User Story: Voice Generation Data Handoff**
  - **Validation Steps**:
    1. Run parser on Episode 7: `python src/parser.py scripts/episode_007.md`
    2. Load output JSON: `python -c "import json; data=json.load(open('output/json/episode_007.json'))"`
    3. Verify dialogue structure has character, voice_direction, text, timestamp fields
  - **Success Criteria**: Voice Generation component can consume data without transformation

- [ ] **User Story: Cost Estimation for Budget Tracking**
  - **Validation Steps**:
    1. Parse Episode 7 and extract metadata
    2. Compare estimated costs against known ElevenLabs pricing
    3. Verify character count accuracy for cost calculation
  - **Success Criteria**: Cost estimates within 5% of actual API usage

- [ ] **User Story: Script Quality Feedback**
  - **Validation Steps**:
    1. Parse Episode 7 with intentional formatting errors
    2. Review generated warnings and suggestions
    3. Apply suggested fixes and reparse
  - **Success Criteria**: Warnings provide actionable guidance for script improvement

### Integration Validation Checklist

- [ ] **Pipeline Tag Specification Compliance**
  - **JSON schema validation**: `python scripts/validate_json_schema.py output/json/episode_007.json`
  - **Required fields present**: All fields from Pipeline Tag Specification exist
  - **No format regressions**: Output matches exact specification format

- [ ] **File System Integration**
  - **Output directory creation**: Parser creates `/output/json/` if it doesn't exist
  - **File naming convention**: Output follows `episode_XXX.json` pattern
  - **Debug mode functionality**: `--debug` flag creates debug output files

### Security & Error Handling Validation

- [ ] **Input Validation**
  - **Malformed markdown handling**: `python src/parser.py tests/fixtures/malformed_episode.md`
  - **Missing file handling**: `python src/parser.py nonexistent_file.md`
  - **Large file handling**: Process oversized markdown file gracefully

- [ ] **Error Handling**
  - **Graceful degradation**: Parser never exits with failure code unless file completely unreadable
  - **Warning generation**: All parsing issues generate warnings with line numbers
  - **Validation report creation**: Separate validation file created alongside JSON

## Validation Command Reference

### Project-Specific Validation Commands

```bash
# Code Quality (Level 1):
black src/ --check           # Code formatting validation
flake8 src/                  # Linting and style checking
mypy src/                    # Type checking validation

# Testing (Level 2):
pytest tests/ -v             # Unit test execution with verbose output
pytest tests/ --cov=src     # Test coverage reporting

# Integration (Level 3):
python parser.py episode_007.md               # PRD-v0 integration test with Episode 7
python setup_validation.py                    # Full environment validation

# Feature Complete (Level 4):
pytest tests/ --cov=src --cov-report=html     # Complete test suite with coverage
python parser.py episode_007.md && echo "Step 1 Complete"  # PRD-v0 completion validation
```

### Custom Validation for Script Parser

```bash
# Parser-Specific Validation Commands (PRD-v0 Format)
python parser.py episode_007.md --debug              # Full parsing with debug output
python scripts/compare_parser_output.py              # Compare against reference output
python scripts/validate_cost_estimation.py           # Verify cost calculation accuracy
python scripts/test_warning_generation.py            # Test error handling and warnings
python scripts/benchmark_parser_performance.py       # Performance benchmarking
```

### Continuous Integration Validation

```bash
# CI Pipeline Commands (to be run after each change) - PRD-v0 Validation
black src/ --check && flake8 src/ && mypy src/                    # Code quality gate
pytest tests/ --cov=src --cov-fail-under=80                      # Coverage gate
python parser.py episode_007.md && echo "Step 1 validated"       # PRD-v0 functional gate
```

## PRD-v0 Integration & Pipeline Progression

### Step 1 Foundation for 8-Component Strategy

**Immediate Deliverable**: JSON timeline with voice lines extracted (PRD-v0 Step 1 goal)

**Compound Value Path**:
- **Step 1** (This PRD): `episode_007.md` → `output/json/episode_007.json`
- **Step 2** (Next): `episode_007.json` → `output/voices/` (individual voice files)
- **Step 3** (Future): Voice files → `output/audio/episode_007.mp3` (complete audio)
- **Step 4** (Future): Audio → `output/videos/episode_007.mp4` (YouTube-ready)

### Critical Success Dependencies

**For Step 2 (Voice Generation) to succeed**, this parser must provide:
- Character-attributed dialogue with voice directions
- Accurate timing estimates for audio assembly
- Character count data for ElevenLabs integration

**For Steps 3-8 to succeed**, this parser must provide:
- Scene structure for video transitions
- SFX cues for audio enhancement
- Image prompts for visual storytelling
- Music cues for background audio

### PRD-v0 Validation Requirements

**"No Step Ships Until" (PRD-v0 Standard)**:
- ✅ Works with Episode 7 content
- ✅ Output quality meets minimum standards for Step 2 consumption
- ✅ Step 2 can successfully use parser output
- ✅ Error handling is clear and actionable

## Open Questions

1. **Config.json Integration**: Should parser configuration (API keys, settings) follow PRD-v0 simple config.json pattern, or use .env files as currently planned?

2. **Command Argument Evolution**: As we add Steps 2-8, should the parser command interface remain simple or evolve to support pipeline integration flags?

3. **Compound Value Optimization**: Should the parser optimize output specifically for downstream steps, or maintain format neutrality for maximum flexibility?

---

**PRD Version**: 1.1 (PRD-v0 Integrated)  
**Created**: 2025-01-07  
**Updated**: 2025-01-07 (PRD-v0 alignment)  
**Feature Owner**: versusMonster AVPS Pipeline  
**Implementation Target**: Step 1 of 8-Component Iterative Strategy (PRD-v0)  
**Pipeline Position**: Foundation for Steps 2-8 (Voice Generation → Batch Processing)