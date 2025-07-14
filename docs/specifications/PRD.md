# VersusMonster Automated Video Podcast System - Product Requirements Document

**Version**: 2.0 (Consolidated Master)  
**Last Updated**: 2025-01-12  
**Development Philosophy**: Function Over Fashion - Build iteratively with compound value

## Executive Summary

### Vision
An automated Python-based system that transforms markdown scripts into complete multimedia podcast episodes suitable for YouTube. The system eliminates manual audio/video production work, enabling focus on creative content generation.

### Business Goal
Generate **2 podcast episodes per week for a full year (104 episodes)** to build an audience and explore monetization through advertising and sponsorships.

### Component Status (Auto-Updated: 2025-07-13)
- **Component 1**: ✅ COMPLETE (2025-01-08) - Script Parser validated with Episode 7
- **Component 2**: 🚧 IN PROGRESS (1/9 tasks) - Voice Generation: ElevenLabs integration  
- **Component 3**: 📝 PLANNED - Audio Assembly (pending Component 2)
- **Component 4**: 📝 PLANNED - Static Video (pending Component 3)
- **Components 5-8**: 📝 PLANNED - Advanced features (pending core pipeline)

#### Component 1 Validation ✅
```bash
python parser.py episode_007.md
# Output: output/json/episode_007.json (69 dialogues parsed)
```
**Last Validated:** 2025-01-08 ✅ **Status:** All success criteria met

#### Component 2 Target
```bash
python voice_gen.py episode_007.json  
# Target: output/voices/ with 69 voice files, <5min processing
```
**Status:** 🚧 Implementation in progress (Notion tasks VSM-31 to VSM-39)

### Development Philosophy
**Function Over Fashion**: Build iteratively in simple steps where each step compounds the benefit from the previous one. No fancy UI/UX - purely command-line tools that deliver functional value immediately.

## System Architecture

### 8-Component Pipeline Overview

```
1. Script Parser      ✅ Markdown → JSON (Complete)
2. Voice Generation   🚧 JSON → Voice Files (In Progress)  
3. Audio Assembly     📝 Voices → Complete Audio
4. Static Video       📝 Audio + Image → Video
5. Image Transitions  📝 Multiple Images → Dynamic Video
6. Sound Effects      📝 Add SFX Layer
7. Background Music   📝 Add Music Layer
8. Batch Processing   📝 Automate Multiple Episodes
```

### Technical Stack
- **Language**: Python 3.11+
- **Audio**: ElevenLabs API, FFmpeg
- **Video**: FFmpeg with VideoToolbox
- **Deployment**: Command-line tools
- **Storage**: Local filesystem

### File Structure
```
versusMonster/
├── scripts/              # Input markdown files
├── output/
│   ├── json/            # Component 1 output
│   ├── voices/          # Component 2 output
│   ├── audio/           # Component 3 output
│   └── videos/          # Components 4-8 output
├── src/                 # Component implementations
└── config.json          # Simple configuration
```

## Component Specifications

### Component 1: Script Parser ✅ COMPLETE

**Status**: Complete (2025-01-08)  
**Performance**: 0.003s processing time (300x faster than requirement)  
**Accuracy**: 100% successful parsing of Episode 7

> **Implementation Details:** See `archive/COMPLETED_TASKS.md` for full development history and validation results.

#### Overview
Transforms markdown podcast scripts into structured JSON data that serves as the foundation for all downstream automation.

#### Key Requirements
1. **Scene Extraction**: Parse `## **[SCENE: NAME]**` markers
2. **Dialogue Processing**: Extract character dialogue with voice directions
3. **Multimedia Tags**: Capture IMG, SFX, MUSIC, AMBIENT, TRANSITION tags
4. **Timing Calculation**: Estimate timestamps for synchronization
5. **Cost Estimation**: Calculate ElevenLabs and other API costs

#### Command Interface
```bash
python parser.py episode_007.md
```

#### Output Format
Structured JSON with scenes, dialogues, multimedia tags, timing, and metadata.

#### Validation Results
- ✅ Extracts all Thorak/Zara dialogue correctly
- ✅ Parses Episode 7 with 100% accuracy
- ✅ Output serves as foundation for Components 2-8
- ✅ Single command operation
- ✅ Functions independently

### Component 2: Voice Generation 🚧 IN PROGRESS

**Status**: In Development  
**Target**: Generate authentic character voices via ElevenLabs API

#### Overview
Transforms structured JSON dialogue data into individual character voice files using ElevenLabs API integration.

#### Key Requirements
1. **Character Voice Mapping**: 
   - THORAK: Scholarly, gravelly tone
   - ZARA: Energetic, emotional variation
2. **Voice Direction Integration**: Apply emotional context to voice parameters
3. **ElevenLabs API Integration**: Use official Python SDK
4. **File Output**: WAV files at 44.1kHz
5. **Cost Tracking**: Monitor API usage against estimates

#### Command Interface
```bash
python voice_gen.py episode_007.json
```

#### Output Format
Individual WAV files: `{episode}_{scene}_{index}_{character}.wav`

#### Current Tasks
- [ ] Implement ElevenLabs API client wrapper
- [ ] Create voice direction processor
- [ ] Build cost tracking system
- [ ] Add progress reporting
- [ ] Implement error recovery

### Component 3: Audio Assembly 📝 PLANNED

**Status**: Not Started  
**Target**: Combine voice files into complete audio track

#### Overview
Assembles individual voice files with proper timing to create a complete podcast audio file.

#### Key Requirements
1. Voice file synchronization using timing data
2. Fade/transition effects between scenes
3. Audio normalization and quality control
4. MP3 output with proper metadata
5. Duration validation

#### Command Interface
```bash
python audio_mix.py episode_007
```

### Component 4: Static Video 📝 PLANNED

**Status**: Not Started  
**Target**: Create YouTube-uploadable video

#### Overview
Combines audio track with single background image to create basic video file.

#### Key Requirements
1. FFmpeg integration for video creation
2. 1920x1080 resolution output
3. MP4 format with YouTube-compatible encoding
4. Metadata embedding
5. Thumbnail generation

#### Command Interface
```bash
python video_gen.py episode_007
```

### Component 5: Image Transitions 📝 PLANNED

**Status**: Not Started  
**Target**: Add visual storytelling with multiple images

#### Overview
Enhances video with image changes at scene breaks using IMG prompts from script.

#### Key Requirements
1. Image timing synchronization
2. Smooth transition effects
3. Ken Burns effect support
4. Resolution optimization
5. Visual consistency

### Component 6: Sound Effects 📝 PLANNED

**Status**: Not Started  
**Target**: Add immersive audio effects

#### Overview
Integrates sound effects based on SFX tags to enhance production quality.

#### Key Requirements
1. SFX library management
2. Timing synchronization
3. Volume balancing
4. Effect layering
5. Quality preservation

### Component 7: Background Music 📝 PLANNED

**Status**: Not Started  
**Target**: Complete audio production

#### Overview
Adds background music layer to create broadcast-ready content.

#### Key Requirements
1. Music cue processing
2. Dynamic volume adjustment
3. Scene-based music selection
4. Fade in/out effects
5. Audio mixing

### Component 8: Batch Processing 📝 PLANNED

**Status**: Not Started  
**Target**: True automation for 2 episodes/week

#### Overview
Processes multiple episodes automatically with queue management.

#### Key Requirements
1. Queue management system
2. Error recovery and retry logic
3. Progress tracking across episodes
4. Resource optimization
5. Notification system

#### Command Interface
```bash
python batch.py episode_007.md episode_008.md
```

## Technical Requirements

### Dependencies
- Python 3.11+
- ElevenLabs Python SDK
- FFmpeg 7.1 with VideoToolbox
- python-dotenv for environment management
- Standard libraries: json, re, pathlib, datetime

### API Integrations
- **ElevenLabs**: Voice generation (Component 2)
- **Future**: Image generation APIs (Component 5)
- **Future**: SFX/Music libraries (Components 6-7)

### Performance Standards
- Script parsing: <10 seconds
- Voice generation: <5 minutes per episode
- Complete pipeline: <30 minutes per episode

### Error Handling
- Graceful degradation
- Detailed error reporting
- Resume capability
- Partial result preservation

## Success Metrics

### Overall Project Success
- ✅ 104 episodes produced in one year
- ✅ <30 minutes processing per episode
- ✅ <$10 cost per episode
- ✅ YouTube-ready quality
- ✅ Zero manual intervention required

### Component Success Criteria
Each component must:
1. **Function**: Produce expected output
2. **Quality**: Output meets minimum standards
3. **Reliability**: Work consistently with Episode 7
4. **Simplicity**: Single command operation

### Validation Standards
- Episode 7 serves as primary test case
- Each component validates against Episode 7
- Integration testing between adjacent components
- End-to-end testing after Component 4

## Appendices

### A. Episode 7 Validation Requirements
Episode 7 contains:
- 9 scenes with specific markers
- 69 character dialogues (mix of THORAK/ZARA)
- Multiple multimedia tags (IMG, SFX, MUSIC, AMBIENT)
- ~15-20 minute target duration
- Complex voice directions and emotions

### B. Pipeline Tag Specification
Standardized tags for service integration:
- `[IMG: id] PROMPT: "description"`
- `[SFX: effect_name]`
- `[MUSIC: track_id]`
- `[AMBIENT: environment]`
- `[TRANSITION: description]`

### C. Cost Estimates
Per episode estimates:
- ElevenLabs voice generation: ~$3.06
- Image generation: ~$0.40-0.80
- Total per episode: <$10

### D. Command Reference
```bash
# Component Commands (Current)
python parser.py episode_007.md              # Component 1
python voice_gen.py episode_007.json         # Component 2

# Future Commands
python audio_mix.py episode_007              # Component 3
python video_gen.py episode_007              # Component 4
python batch.py scripts/*.md                 # Component 8
```

### E. Validation Commands
```bash
# Code Quality
black src/ --check
flake8 src/
mypy src/

# Testing
pytest tests/ -v
pytest tests/ --cov=src

# Integration
python parser.py episode_007.md && python voice_gen.py episode_007.json
```

---

## Project References

### Development History
- **Component Implementation:** See `archive/COMPLETED_TASKS.md` for detailed development history
- **Task Management:** See `TODO.md` for current active tasks and upcoming work
- **Context Guidelines:** See `AI_CONTEXT.md` for development patterns and context

### Archive Documentation
- `archive/COMPLETED_TASKS.md` - Complete history of implemented components and milestones
- `archive/README.md` - Guide to archived PRD and task files
- `archive/prd-*.md` - Original component-specific requirements (historical reference)

---

## PRD Maintenance & Automation

### Source of Truth Protocol
This PRD.md file serves as the definitive source of truth for component specifications and progress tracking.

### Automated Updates
- **Component Status**: Auto-updated via `@finalize-task` when Notion tasks complete
- **Validation Commands**: Added when components reach completion
- **Progress Tracking**: Synced from Notion database (VSM task completion)

### Manual Update Rules
**Never Change**: Core requirements, success criteria, component architecture  
**Always Update**: Status markers, completion dates, validation results, task progress

### Update Commands
```bash
@finalize-task     # Completes task + updates PRD component status
@update-prd        # Sync all component progress from Notion
@next-task         # Get next priority based on current component
```

### Validation Requirements
Each completed component must include:
1. **Command validation** - Exact command that proves component works
2. **Success criteria verification** - All PRD requirements met
3. **Episode 7 test case** - Validated against reference implementation

---

**Bottom Line**: Build the simplest possible version of each component first. Each step should deliver immediate, testable value that compounds with previous work. No fancy interfaces - just rock-solid functionality that gets you closer to automated episode production with every iteration.