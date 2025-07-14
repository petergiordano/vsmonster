# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
**versusMonster AVPS (Automated Video Podcast System)**
- Repository: https://github.com/petergiordano/vsmonster
- **Goal**: Transform markdown scripts into complete YouTube-ready podcast episodes
- **Target**: 104 episodes/year (2 episodes/week)
- **Philosophy**: "Function Over Fashion" - iterative build with compound value

## Architecture: 8-Component Pipeline

Sequential pipeline where each component delivers independent value:

1. **Script Parser** ✅ - Markdown → structured JSON (`parser.py`)
2. **Voice Generation** ✅ - JSON → character voice files (`voice_gen.py`) 
3. **Audio Assembly** 📝 - Voice files → complete audio track
4. **Static Video** 📝 - Audio + image → YouTube video
5. **Image Transitions** 📝 - Multiple images → dynamic video
6. **Sound Effects** 📝 - Add SFX layer
7. **Background Music** 📝 - Complete audio production
8. **Batch Processing** 📝 - Automate multiple episodes

## Task Management System
**Notion Database:** vmonster-dev-backlog
- Database ID: `22f859c6-e596-8007-86c6-c1df9f865855`
- Schema: See `config/notion-database-schema.json`
- Tasks prefixed: VSM-1, VSM-2, etc.
- **PRD Sync:** `@finalize-task` auto-updates `docs/specifications/PRD.md` component status

## Essential Commands

### Pipeline Operations
```bash
# Component 1: Parse markdown script
python parser.py scripts/episode_007.md
python src/parser.py scripts/episode_007.md  # Alternative path

# Component 2: Generate character voices
python voice_gen.py output/json/episode_007.json
python src/voice_gen.py output/json/episode_007.json  # Alternative path

# Episode post-processing (fix tag escaping)
python tools/process_episode.py scripts/episode_007.md

# Cost analysis and reporting
python src/cost_reporter.py output/json/episode_007.json
```

### Development Workflow
```bash
# Environment validation (run first on new setup)
python setup_validation.py

# Quality assurance (run before commits)
black src/ --check              # Code formatting
flake8 src/                     # Python linting
mypy src/                       # Type checking

# Testing
pytest tests/ -v                # Run test suite
pytest tests/ --cov=src         # With coverage
pytest tests/ --cov=src --cov-fail-under=80  # Coverage gate

# Integration testing with Episode 7 (gold standard)
python parser.py scripts/episode_007.md
python voice_gen.py output/json/episode_007.json
```

### Task Management Commands
```bash
# Start next available task
@next-task

# Complete and track task (auto-detects current task)
@finalize-task
```

## Data Flow and File Structure

### Pipeline Data Flow:
```
scripts/episode_007.md → output/json/episode_007.json → output/voices/episode_007/*.wav → [future: complete audio/video]
```

### Key Directories:
```
scripts/           # Input markdown episodes
output/json/       # Parsed JSON (Component 1 output)
output/voices/     # Generated voice files (Component 2 output)  
output/audio/      # Mixed audio tracks (Component 3 target)
output/videos/     # Final videos (Components 4-8 target)
src/               # Core pipeline components
tests/             # Test suite
```

### Configuration:
- `config/config.json` - Central pipeline configuration
- `.env` - API keys (ElevenLabs, future services)
- `pyproject.toml` - Python tooling configuration
- `config/notion-database-schema.json` - Task management schema

## Episode 7 as Universal Test Case

**All components validate against `scripts/episode_007.md`:**
- Contains 69 dialogues (THORAK/ZARA characters)
- Includes all multimedia tags: IMG, SFX, MUSIC, AMBIENT, TRANSITION
- Target processing: <5 minutes, ~$4.41 total cost
- Expected voice output: 69 WAV files in `output/voices/episode_007/`

## Character Voice Configuration

**ElevenLabs API Integration:**
- **THORAK**: Scholarly, gravelly tone (Stability 0.75, Similarity 0.85)
- **ZARA**: Energetic, emotional variation (Stability 0.45, Similarity 0.75)
- Voice directions processed from markdown: `(Breathless)`, `(Gravelly, impressed)`

## Pipeline Tag System

Standardized markdown tags enable automation:
```markdown
## **[SCENE: SCENE_NAME]**           # Scene boundaries
THORAK: (Voice direction) "Dialogue" # Character speech
[IMG: id] PROMPT: "description"      # Image generation  
[SFX: effect_name]                   # Sound effects
[MUSIC: track_name]                  # Background music
[AMBIENT: environment]               # Atmospheric audio
[TRANSITION: description]            # Scene transitions
```

## Development Workflow

### 1. Planning Phase (Claude Chat)
- Chief Product Officer (user) and Claude Chat determine tasks
- PRD and roadmap planning in browser session
- Claude Chat creates Notion database entries
- Tasks assigned phases: Discovery → Design → Development → Testing → Deployment

### 2. Development Phase (Claude Code)
**Workflow:**
- Run `@next-task` to get highest priority available task
- Updates task status to "In Progress" automatically
- Creates implementation plan with file paths and steps
- Implement according to plan with Episode 7 validation
- Test thoroughly using quality assurance commands
- Run `@finalize-task` to complete and track (auto-detects current task)
- Updates Notion with completion status and suggests next task

### 3. Validation Requirements
Each component must achieve:
1. **Functional**: Produces expected output format
2. **Quality**: Output usable by next component
3. **Reliable**: Works consistently with Episode 7
4. **Simple**: Single command operation

### 4. Git Workflow
**Commit Format:**
```
VSM-6: Add ElevenLabs API key validation

- Configured .env file integration
- Added API key validation logic  
- Updated error handling

Closes VSM-6
```

## Current Development Status

**Active Development**: Component 3 (Audio Assembly)
- **Dependencies**: Components 1-2 complete and validated
- **Input**: Voice files from `output/voices/episode_007/`
- **Target**: Single MP3 with proper dialogue timing
- **Next Command**: `python audio_mix.py output/voices/episode_007/`

## MCP Tool Access

You have access to:
- **Notion MCP**: Read/update task database (22f859c6-e596-8007-86c6-c1df9f865855)
- **Filesystem MCP**: File operations and project management
- **Memory MCP**: Maintain context across sessions

Use these tools to maintain the single source of truth in Notion while implementing pipeline components.

## Available Commands (Located in .claude/commands/)
- `@next-task` - Auto-selects highest priority task, updates to "In Progress", creates implementation plan
- `@finalize-task` - Auto-detects current task, tests, generates commit commands, updates Notion to "Done"

## Success Criteria

**Component Success**: Function + Quality + Reliability + Simplicity  
**Pipeline Success**: Episode 7 → Complete YouTube video in <30 minutes, <$10 cost  
**Project Success**: 104 episodes/year automated production capability