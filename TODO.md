# Project TODO: versusMonster AVPS

## 🚀 Current Status

**Project Phase:** Component 2 (Voice Generation) Implementation  
**Last Updated:** 2025-01-12  
**PRD Source:** `/PRD.md` - Master consolidated requirements document

This file tracks development progress for the versusMonster Automated Video Podcast System's 8-component iterative build strategy.

---

## 🎯 Current Sprint: Component 2 - Voice Generation

### Active Development Tasks
- [ ] **Voice Generation Implementation** (Component 2 of 8)
  - [ ] Add ElevenLabs API key to .env file
  - [ ] Implement ElevenLabs API client wrapper
  - [ ] Create character voice mapping (THORAK: scholarly, ZARA: energetic)
  - [ ] Build voice direction processor
  - [ ] Add cost tracking system
  - [ ] Implement progress reporting
  - [ ] Add error recovery

### Validation Commands for Component 2
```bash
# Level 1 - Syntax & Style:
black src/ --check        # Code formatting check
flake8 src/               # Python linting
mypy src/                 # Type checking

# Level 2 - Unit Testing:
pytest tests/test_voice_gen.py -v                    # Voice generation unit tests
pytest tests/ --cov=src --cov-report=term           # Coverage report

# Level 3 - Integration:
python voice_gen.py output/json/episode_007.json    # Integration test with Episode 7
python scripts/validate_voice_output.py             # Validate voice file structure

# Level 4 - Feature Complete:
pytest tests/ --cov=src --cov-fail-under=80         # Full test suite with coverage
python voice_gen.py episode_007.json && echo "✓"    # PRD-v0 validation
```

---

## 📋 8-Component Pipeline Progress

### ✅ Components Completed

#### **Component 1: Script Parser** ✅ 2025-01-08
**Status:** Complete - All functionality implemented and validated  
**Performance:** 0.003s processing time (300x faster than requirement)  
**Command:** `python parser.py episode_007.md`

**Key Features:**
- Scene extraction with proper markdown parsing
- Character dialogue parsing with voice directions  
- Multimedia tag extraction (IMG, SFX, MUSIC, AMBIENT, TRANSITION)
- Timing calculation and cost estimation
- Comprehensive validation and error handling
- Output: Structured JSON ready for Voice Generation

**Validation Results:**
- ✅ Extracts all Thorak/Zara dialogue correctly
- ✅ Parses Episode 7 with 100% accuracy  
- ✅ Output serves as foundation for Components 2-8
- ✅ Single command operation
- ✅ Functions independently

### 🚧 Components In Progress

#### **Component 2: Voice Generation** 🚧 IN PROGRESS
**Goal:** Transform JSON dialogue into individual character voice files  
**Command:** `python voice_gen.py episode_007.json`  
**Target:** Generate authentic THORAK/ZARA voices via ElevenLabs API

**Current Tasks:**
- [ ] Implement ElevenLabs API client wrapper
- [ ] Create voice direction processor  
- [ ] Build cost tracking system
- [ ] Add progress reporting
- [ ] Implement error recovery

### 📝 Components Planned

#### **Component 3: Audio Assembly** 📝 PLANNED
**Goal:** Combine voice files into complete audio track  
**Command:** `python audio_mix.py episode_007`

#### **Component 4: Static Video** 📝 PLANNED  
**Goal:** Create YouTube-uploadable video with audio + single image  
**Command:** `python video_gen.py episode_007`

#### **Component 5: Image Transitions** 📝 PLANNED
**Goal:** Add visual storytelling with multiple images  

#### **Component 6: Sound Effects** 📝 PLANNED
**Goal:** Add immersive audio effects layer

#### **Component 7: Background Music** 📝 PLANNED  
**Goal:** Complete audio production with music layer

#### **Component 8: Batch Processing** 📝 PLANNED
**Goal:** Automate multiple episodes for 2 episodes/week target

---

## 🏗️ Project Foundation (Completed)  

**Project Setup & Environment** ✅ 2025-01-07  
- [x] Template repository creation and local setup
- [x] Python 3.11 environment with all dependencies  
- [x] FFmpeg 7.1 with VideoToolbox hardware acceleration
- [x] Project directory structure (scripts/, output/, assets/, etc.)
- [x] Environment validation script (100% success rate)
- [x] Security configuration (.env template, .gitignore)
- [x] Episode 7 test case integration

**Foundation Documents** ✅ 2025-01-07  
- [x] AI_CONTEXT.md with versusMonster-specific context
- [x] Pipeline Tag Specification for service integration  
- [x] Standardized tags for ElevenLabs, image generation, SFX, music APIs
- [x] Quality assurance and cost tracking framework
- [x] Component library and roadmap documentation

---

## 🔧 Technical Infrastructure

### Development Environment
- **Python:** 3.11+ with virtual environment
- **Audio:** ElevenLabs API, FFmpeg  
- **Video:** FFmpeg with VideoToolbox
- **Testing:** pytest with coverage reporting
- **Validation:** black, flake8, mypy

### File Structure  
```
versusMonster/
├── PRD.md                    # Master requirements document
├── scripts/                  # Input markdown files
├── output/
│   ├── json/                # Component 1 output  
│   ├── voices/              # Component 2 output
│   ├── audio/               # Component 3 output
│   └── videos/              # Components 4-8 output
├── src/                     # Component implementations
└── config.json              # Simple configuration
```

### Quality Standards
- **Code Quality:** black + flake8 + mypy compliance
- **Test Coverage:** ≥80% with pytest
- **Performance:** <30 minutes per episode processing
- **Independence:** Each component functions standalone
- **Validation:** Episode 7 as primary test case

---

## 📚 Documentation & References

### Primary Documents
- **`/PRD.md`** - Master Product Requirements Document (consolidated)
- **`/AI_CONTEXT.md`** - Project context and development guidelines  
- **`/CLAUDE.md`** - Claude Code workflow integration

### Archived Documents  
- **`/docs/PRD-v0.md`** - Original 8-component strategy (reference)
- **`/tasks/prd-script-parser.md`** - Component 1 detailed requirements (reference)
- **`/tasks/prd-voice-generation.md`** - Component 2 detailed requirements (reference)

### Success Metrics
- **Overall Project:** 104 episodes/year, <30min processing, <$10/episode
- **Component Success:** Function + Quality + Reliability + Simplicity
- **Validation:** Episode 7 compatibility across all components

---

## 📝 Development Notes

**Latest Updates:**

- **2025-01-12:** PRD consolidation completed - single master document created
- **2025-01-08:** Component 1 (Script Parser) completed with 100% Episode 7 validation
- **2025-01-07:** Project foundation and environment setup completed

**Development Philosophy:** Function Over Fashion - Build iteratively with compound value  
**Primary Test Case:** Episode 7 serves as validation standard for all components

---

## 🎯 Success Tracking

### Key Milestones

- [x] **Phase 1 Foundation:** Project setup and Component 1 ✅
- [ ] **Phase 2 Audio:** Components 2-3 (Voice Generation + Audio Assembly)  
- [ ] **Phase 3 Video:** Components 4-5 (Static Video + Image Transitions)
- [ ] **Phase 4 Production:** Components 6-7 (Sound Effects + Background Music)
- [ ] **Phase 5 Automation:** Component 8 (Batch Processing)

### Current Objective

**Generate first complete audio podcast episode** using Components 1-3 with Episode 7 as validation case.

---

**Reference:** This consolidated TODO replaces scattered task files. See `/PRD.md` for complete technical requirements.
