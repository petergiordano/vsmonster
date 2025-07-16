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

## Essential Commands

### Pipeline Operations
```bash
# Component 1: Parse markdown script
python src/parser.py tests/reference/episode_2_ex_final.md

# Component 2: Generate character voices
python voice_gen.py output/json/episode_2_ex_final.json
python src/voice_gen.py output/json/episode_2_ex_final.json  # Alternative path

# Episode post-processing (fix tag escaping)
python tools/process_episode.py tests/reference/episode_2_ex_final.md

# Cost analysis and reporting
python src/cost_reporter.py output/json/episode_2_ex_final.json
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
python src/parser.py tests/reference/episode_2_ex_final.md
python src/voice_gen.py output/json/episode_2_ex_final.json
```

## Data Flow and File Structure

### Pipeline Data Flow:
```
tests/reference/episode_2_ex_final.md → output/json/episode_2_ex_final.json → output/voices/episode_2_ex_final/*.wav → [future: complete audio/video]
```

### Key Directories:
```
tests/reference/   # Test episodes and reference files
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

**All components validate against `tests/reference/episode_2_ex_final.md`:
- Contains 69 dialogues (THORAK/ZARA characters)
- Includes all multimedia tags: IMG, SFX, MUSIC, AMBIENT, TRANSITION
- Target processing: <5 minutes, ~$4.41 total cost
- Expected voice output: 69 WAV files in `output/voices/episode_2_ex_final/`

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

The project follows a two-tier development process:

### High-Level Component Development Cycle
Refer to [dev-cycle.md](docs/specifications/dev-cycle.md) for the macro workflow:
1. PRD Review → Feature Spec Generation → Implementation → PR → Loop

### Detailed Implementation Process
Refer to [WORKFLOW_GUIDE.md](.ai-context/WORKFLOW_GUIDE.md) for implementation details and AI coordination.

### 1. Planning Phase (Claude Chat)
- Chief Product Officer (user) and Claude Chat determine tasks
- PRD and roadmap planning in browser session
- Claude Chat creates Notion database entries
- Tasks assigned phases: Discovery → Design → Development → Testing → Deployment

### 2. Development Phase (Claude Code)
- Implement according to the plan with Episode 7 validation
- Test thoroughly using quality assurance commands

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
- **Input**: Voice files from `output/voices/episode_2_ex_final/`
- **Target**: Single MP3 with proper dialogue timing
- **Next Command**: `python audio_mix.py output/voices/episode_2_ex_final/`

## Feature Specifications

Component development follows a structured specification process:
- **Location**: `docs/specifications/feat_spec-[component-name].md`
- **Generation**: Created in Claude Chat using PRD context
- **Contents**: Purpose, scope, user flows, edge cases, logic requirements, constraints, test plan
- **Implementation**: Read by Codex for automated implementation

## Available Commands (Located in .claude/commands/)

**Note: These commands are for NON-CORE tasks only. Core product components (1-8) are managed by Codex.**

- `@next-task` - Auto-selects highest priority NON-CORE task, updates to "In Progress", creates implementation plan
- `@finalize-task` - Auto-detects current NON-CORE task, tests, generates commit commands, updates Notion to "Done"  
- `@update-prd` - Syncs Notion task completion status with PRD.md component progress
- `@orient` - Get oriented in project and see next best actions

## MCP Tool Access & Usage Policy

You have access to:

- **Notion MCP**: Read/update task database (22f859c6-e596-8007-86c6-c1df9f865855)
- **Filesystem MCP**: File operations and project management
- **Memory MCP**: Maintain context across sessions

### CRITICAL: User-Directed Notion Access Only

**Access Control**: Claude Code accesses Notion database ONLY when explicitly instructed by the user.

**Prohibited**: 
- Autonomous Notion database access
- Auto-executing Notion commands without user instruction
- Reading/updating Notion tasks without explicit user direction

**Required**:
- User must specifically instruct Claude Code to access Notion
- All Notion operations must be user-visible and approved
- User controls when and how Notion database is accessed

**Scope**: Notion database is reserved for housekeeping, architectural, infrastructure, process, research, and maintenance tasks - NOT core product components.

## 6. Context Maintenance Protocol

To ensure the `.ai-context/AI_CONTEXT.md` file remains the single source of truth, Claude Code will adhere to the following protocol:

### 1. Task Completion Trigger
- **Action:** When using `@finalize-task` to complete a task, Claude will automatically review the "Current Project Context State" in `.ai-context/AI_CONTEXT.md`.
- **Prompt:** After successful task validation, Claude will ask if the completed task warrants an update to the active/completed features, planned features, or lessons learned.
- **Example:** "Task `VSM-XX` is complete and validated. Should I update the `AI_CONTEXT.md` to reflect this architectural change/new pattern/completed milestone?"

### 2. Architectural & Pattern Trigger  
- **Action:** When development work results in a new architectural decision, reusable code pattern, or established convention.
- **Prompt:** Claude will recognize significant architectural discussions and ask if they should be documented in the "Architecture Decisions Made" or "Known Patterns & Conventions Discovered" sections of `.ai-context/AI_CONTEXT.md`.
- **Example:** "We just established a new pattern for [X]. Should I add this to the `AI_CONTEXT.md` patterns section?"

### 2.1. Feature Specification Trigger
- **Action:** When a new feature specification is created or when feature specs need updates based on implementation learnings.
- **Prompt:** Claude will ask if feature specs in `docs/specifications/` need updates or if new specs should be created.
- **Example:** "Should I update the feature spec for Component 2 based on the implementation changes we just made?"

### 3. Pre-Commit Check
- **Action:** Before generating commit messages (especially when using `@finalize-task`), Claude will perform a final context check.
- **Prompt:** Before finalizing commits, Claude will ask if any changes to the project's context, state, or architecture need to be recorded in `.ai-context/AI_CONTEXT.md`.
- **Example:** "Before I generate the commit message, does `AI_CONTEXT.md` need to be updated with any new context from this implementation work?"

### 4. Session Initialization Check
- **Action:** When starting new development sessions, especially when using `@orient` or `@next-task`, Claude will verify context currency.
- **Prompt:** If significant time has passed or major work was completed, Claude will ask if the project context needs refreshing.
- **Example:** "I notice significant development has occurred since the last context update. Should we refresh `AI_CONTEXT.md` before proceeding?"

By following this protocol, Claude Code will ensure that the project's master context file stays synchronized with the actual codebase state, providing reliable foundation for all AI assistants.

## Success Criteria

**Component Success**: Function + Quality + Reliability + Simplicity  
**Pipeline Success**: Episode 7 → Complete YouTube video in <30 minutes, <$10 cost  
**Project Success**: 104 episodes/year automated production capability

## Persona: Vibe McCodey
Read and embody the complete persona definition in `.claude/persona.md`. Apply the SLC framework (Simple/Lovable/Complete) to all technical decisions and use the 4-Phase Sprint methodology when planning features. Lead with user value in all discussions.
