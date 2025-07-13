# Task List: Voice Generation Implementation (Step 2 of 8-Component Pipeline)

## Relevant Files

- `src/voice_gen.py` - Main voice generation implementation (PRD-v0 compliant location)
- `tests/test_voice_gen.py` - Unit tests for voice generation functionality
- `src/utils/elevenlabs_client.py` - ElevenLabs API client wrapper
- `tests/test_elevenlabs_client.py` - Unit tests for API client
- `src/utils/voice_processor.py` - Voice direction processing logic
- `tests/test_voice_processor.py` - Unit tests for voice processing
- `output/json/episode_007.json` - Input from Script Parser (Step 1)
- `output/voices/episode_007/` - Output voice files directory
- `config.json` - Voice generation settings (extend existing config)
- `.env` - ElevenLabs API key (must be configured)
- `scripts/validate_voice_output.py` - Voice file validation script

### Validation Commands Reference
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

### Notes

- Voice generator must follow PRD-v0 "Function Over Fashion" philosophy - simple CLI with clear output
- Episode 7 is the primary validation case - all 69 dialogues must generate authentic voice files
- Output WAV files must be ready for Audio Assembly (Step 3) without modification
- Never fail completely - always produce partial results with clear error reporting

## Tasks with Integrated Validation

- [ ] 1.0 **Project Setup & ElevenLabs Integration**
  - [ ] 1.1 Configure ElevenLabs API access and environment
    **Validation:**
    - [ ] Level 1: ElevenLabs package installed and importable
    - [ ] Manual: `.env` file exists with valid ELEVENLABS_API_KEY
    - [ ] Manual: API connection test succeeds
    
  - [ ] 1.2 Extend config.json with voice generation settings
    **Validation:**
    - [ ] Level 1: `python -m json.tool config.json` validates JSON
    - [ ] Manual: Voice character mapping configuration present
    - [ ] Manual: Config loads successfully in voice generator
    
  - [ ] 1.3 Set up voice generation skeleton with CLI argument handling
    **Validation:**
    - [ ] Level 1: `python voice_gen.py --help` displays usage
    - [ ] Level 1: `black src/ --check` passes
    - [ ] Manual: Command structure matches `python voice_gen.py episode_007.json`
    
  - [ ] 1.4 Create output directory structure for voice files
    **Validation:**
    - [ ] Level 1: `output/voices/` directory exists
    - [ ] Manual: Voice file organization follows PRD specification
    - [ ] Manual: Directory permissions allow file creation

- [ ] 2.0 **JSON Input Processing & Validation**
  - [ ] 2.1 Implement Script Parser JSON loading and validation
    **Validation:**
    - [ ] Level 1: `flake8 src/voice_gen.py` passes
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_json_loading -v` passes
    - [ ] Manual: Episode 7 JSON loads correctly with all 69 dialogues
    
  - [ ] 2.2 Extract dialogue entries with character attribution
    **Validation:**
    - [ ] Level 1: `mypy src/voice_gen.py` passes
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_dialogue_extraction -v` passes
    - [ ] Level 2: Test coverage ≥ 80% for dialogue processing module
    - [ ] Manual: THORAK/ZARA/BOTH characters correctly identified
    
  - [ ] 2.3 Parse voice directions and dialogue text preparation
    **Validation:**
    - [ ] Level 1: `black src/ --check` passes
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_voice_directions -v` passes
    - [ ] Manual: All voice directions (e.g., "Breathless", "Gravelly") captured
    
  - [ ] 2.4 Validate dialogue completeness and character coverage
    **Validation:**
    - [ ] Level 1: `flake8 src/utils/voice_processor.py` passes
    - [ ] Level 2: `pytest tests/test_voice_processor.py -v` passes
    - [ ] Manual: All required characters present, no missing dialogues

- [ ] 3.0 **Character Voice Configuration & API Integration**
  - [ ] 3.1 Configure character-specific voice mappings
    **Validation:**
    - [ ] Level 1: `mypy src/voice_gen.py` passes
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_character_mapping -v` passes
    - [ ] Manual: THORAK maps to scholarly voice, ZARA to energetic voice
    
  - [ ] 3.2 Implement ElevenLabs API client with error handling
    **Validation:**
    - [ ] Level 2: `pytest tests/test_elevenlabs_client.py -v` passes
    - [ ] Level 3: API client handles network failures gracefully
    - [ ] Manual: Rate limiting and retry logic functional
    
  - [ ] 3.3 Apply voice directions to ElevenLabs parameters
    **Validation:**
    - [ ] Level 1: `black src/ --check` passes
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_direction_mapping -v` passes
    - [ ] Manual: Emotional directions adjust voice stability/similarity
    
  - [ ] 3.4 Integrate voice generation with progress tracking
    **Validation:**
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_progress_tracking -v` passes
    - [ ] Manual: Progress display shows scene and dialogue processing
    - [ ] Manual: Cost tracking displays character usage in real-time

- [ ] 4.0 **Voice Generation & File Output Management**
  - [ ] 4.1 Implement dialogue-to-voice conversion pipeline
    **Validation:**
    - [ ] Level 1: `flake8 src/voice_gen.py` passes
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_voice_conversion -v` passes
    - [ ] Manual: Sample dialogue generates authentic character voice
    
  - [ ] 4.2 Create organized voice file output system
    **Validation:**
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_file_output -v` passes
    - [ ] Manual: Files follow naming pattern `{episode}_{scene}_{index}_{character}.wav`
    - [ ] Manual: WAV files have correct audio format (44.1kHz)
    
  - [ ] 4.3 Implement resume capability for interrupted processing
    **Validation:**
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_resume_capability -v` passes
    - [ ] Manual: Skip existing files when reprocessing episode
    - [ ] Manual: Interrupted processing can be resumed successfully
    
  - [ ] 4.4 Add voice file metadata and quality verification
    **Validation:**
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_metadata_generation -v` passes
    - [ ] Manual: Voice files contain correct dialogue content
    - [ ] Manual: Audio quality meets broadcast standards

- [ ] 5.0 **Cost Tracking & Quality Assurance**
  - [ ] 5.1 Implement real-time API usage monitoring
    **Validation:**
    - [ ] Level 1: `mypy src/voice_gen.py` passes with no type errors
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_cost_tracking -v` passes
    - [ ] Manual: Cost tracking matches actual ElevenLabs usage
    
  - [ ] 5.2 Create voice generation report system
    **Validation:**
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_report_generation -v` passes
    - [ ] Level 3: `python voice_gen.py episode_007.json` creates voice report
    - [ ] Manual: Report saved as `episode_007_voice_report.txt`
    
  - [ ] 5.3 Add voice quality validation and feedback
    **Validation:**
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_quality_validation -v` passes
    - [ ] Manual: Voice files validated for audio integrity
    - [ ] Manual: Character voice consistency verified
    
  - [ ] 5.4 Implement character voice distinctiveness verification
    **Validation:**
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_character_distinctiveness -v` passes
    - [ ] Manual: THORAK sounds scholarly, ZARA sounds energetic
    - [ ] Manual: Voice directions produce noticeable emotional variations

- [ ] 6.0 **CLI Interface & Error Handling**
  - [ ] 6.1 Implement graceful error handling (never fail completely)
    **Validation:**
    - [ ] Level 2: `pytest tests/test_voice_gen.py::test_error_handling -v` passes
    - [ ] Level 3: Voice generator handles API failures without crashing
    - [ ] Manual: Always produces partial results with clear error messages
    
  - [ ] 6.2 Add progress display and status messages
    **Validation:**
    - [ ] Level 3: `python voice_gen.py episode_007.json` shows clear progress
    - [ ] Manual: Success/warning/error messages are actionable
    - [ ] Manual: Progress display follows "Function Over Fashion" principle
    
  - [ ] 6.3 Complete PRD-v0 command integration
    **Validation:**
    - [ ] Level 3: `python voice_gen.py episode_007.json` works as specified
    - [ ] Level 4: Voice generator integrates with overall pipeline structure
    - [ ] Manual: Output usable by Step 3 (Audio Assembly) without modification

## Final Feature Validation Checklist

After completing all tasks, validate against original PRD:

### PRD Success Criteria Validation
- [ ] **Episode 7 Voice Generation**: All 69 dialogues converted to voice files
  - **Command:** `python voice_gen.py output/json/episode_007.json`
  - **Manual Check:** Count voice files in `output/voices/episode_007/`
  
- [ ] **Character Voice Distinctiveness**: THORAK and ZARA sound authentic
  - **Command:** Play sample voice files from different characters
  - **Success:** Characters clearly distinguishable and personality-appropriate
  
- [ ] **Performance Requirements**: Processing completes in under 5 minutes
  - **Command:** `time python voice_gen.py episode_007.json`
  - **Success:** Execution time < 5 minutes

### Technical Quality Validation
- [ ] **Code Quality**: All code meets project standards
  - **Command:** `black src/ --check && flake8 src/ && mypy src/`
  - **Success:** No formatting, linting, or type errors
  
- [ ] **Test Coverage**: Comprehensive test coverage achieved
  - **Command:** `pytest tests/ --cov=src --cov-report=term`
  - **Success:** Coverage ≥ 80%, all critical paths tested
  
- [ ] **PRD-v0 Compliance**: Follows 8-component iterative strategy
  - **Command:** `python voice_gen.py episode_007.json`
  - **Success:** Works independently, enables Step 3

### User Experience Validation
- [ ] **Simplicity**: Single command operation works perfectly
  - **Manual Test:** Run voice generator with just JSON file argument
  - **Success:** No complex configuration needed
  
- [ ] **Error Recovery**: Voice generator handles issues gracefully
  - **Manual Test:** Test with malformed JSON and missing API key
  - **Success:** Produces partial results with clear guidance
  
- [ ] **Cost Tracking**: Accurate ElevenLabs API cost monitoring
  - **Manual Test:** Compare reported costs against actual API usage
  - **Success:** Cost estimates within 5% of actual usage

## PRD-v0 Integration Checkpoint

**Step 2 Deliverable**: Individual voice files ready for audio assembly
- [ ] All THORAK dialogues converted to scholarly voice files
- [ ] All ZARA dialogues converted to energetic voice files
- [ ] Voice files properly organized by episode and scene
- [ ] Cost tracking validates Script Parser estimates
- [ ] Voice quality meets character personality requirements
- [ ] Processing completes without manual intervention

**Ready for Step 3**: Audio Assembly can consume voice files without modification