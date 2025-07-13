# TODO: versusMonster AVPS

**Current Phase:** Component 2 (Voice Generation)  
**Status:** 1 of 8 components complete  
**Objective:** Generate first complete audio podcast episode

---

## 🎯 Active Tasks: Voice Generation

### Implementation Tasks
- [ ] Add ElevenLabs API key to .env file
- [ ] Implement ElevenLabs API client wrapper (`src/utils/elevenlabs_client.py`)
- [ ] Create character voice mapping
  - [ ] THORAK: Scholarly, gravelly tone (Stability 0.75, Similarity 0.85)
  - [ ] ZARA: Energetic, emotional variation (Stability 0.45, Similarity 0.75)
- [ ] Build voice direction processor
- [ ] Add cost tracking system ($3.06/episode estimate)
- [ ] Implement progress reporting (5-step display)
- [ ] Add error recovery and retry logic

### Testing & Validation
- [ ] Unit tests for voice generation (`tests/test_voice_gen.py`)
- [ ] Integration test with Episode 7 JSON
- [ ] Verify 69 voice files generated
- [ ] Character voice distinctiveness check
- [ ] Cost tracking accuracy validation

### Success Criteria
- [ ] Command: `python voice_gen.py episode_007.json` works
- [ ] All Episode 7 dialogues convert to voice files
- [ ] Processing completes in <5 minutes
- [ ] Voice files ready for Audio Assembly (Component 3)

---

## 📅 Upcoming Components

### Component 3: Audio Assembly
- Combine voice files into complete audio track
- Command: `python audio_mix.py episode_007`
- Output: Single MP3 with proper dialogue timing

### Component 4: Static Video
- Create YouTube-uploadable video
- Command: `python video_gen.py episode_007`
- Output: MP4 with static background image

### Components 5-8: Production & Automation
- Image Transitions
- Sound Effects
- Background Music
- Batch Processing

---

## 🔧 Technical Debt

### Code Quality
- [ ] Add type annotations to process_episode.py
- [ ] Fix remaining line length warnings in process_episode.py
- [ ] Create comprehensive test suite for parser.py

### Documentation
- [ ] Create setup guide for new developers
- [ ] Document API key requirements
- [ ] Add examples for each component

### Infrastructure
- [ ] Set up CI/CD pipeline
- [ ] Configure pre-commit hooks
- [ ] Add automated testing on push

---

## 📝 Quick Reference

### Commands
```bash
# Component 1 (Complete)
python parser.py episode_007.md

# Component 2 (Current)
python voice_gen.py episode_007.json

# Validation
pytest tests/ -v --cov=src
black src/ --check
flake8 src/
mypy src/
```

### Key Files
- `/PRD.md` - Master requirements
- `/AI_CONTEXT.md` - Development context
- `output/json/episode_007.json` - Parser output
- `output/voices/` - Voice generation target

### Resources
- Episode 7: Primary test case
- Target: 104 episodes/year
- Budget: <$10/episode
- Performance: <30min/episode

---

## 📚 References

### Project Documentation
- `/PRD.md` - Complete technical requirements for all 8 components
- `/AI_CONTEXT.md` - Development guidelines and project context
- `archive/COMPLETED_TASKS.md` - History of completed work and achievements

### Completed Work
**Component 1 (Script Parser)** completed 2025-01-08 with 100% Episode 7 validation.  
See `archive/COMPLETED_TASKS.md` for full implementation history.

---

**Last Updated:** 2025-01-13