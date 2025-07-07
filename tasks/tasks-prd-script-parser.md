# Task List: Script Parser Implementation (Step 1 of 8-Component Pipeline)

## Relevant Files

- `src/parser.py` - Main parser implementation (PRD-v0 compliant location)
- `tests/test_parser.py` - Unit tests for parser functionality
- `src/utils/markdown_processor.py` - Markdown parsing utilities
- `tests/test_markdown_processor.py` - Unit tests for markdown utilities
- `src/utils/timing_calculator.py` - Dialogue timing estimation logic
- `tests/test_timing_calculator.py` - Unit tests for timing calculations
- `src/utils/cost_estimator.py` - API cost estimation utilities
- `tests/test_cost_estimator.py` - Unit tests for cost estimation
- `scripts/episode_007.md` - Episode 7 test script (must be added)
- `output/json/episode_007.json` - Expected output location
- `config.json` - Simple configuration file (PRD-v0 pattern)
- `scripts/validate_parser_output.py` - Output validation script
- `scripts/compare_parser_output.py` - Reference comparison tool
- `docs/parser_usage.md` - CLI usage documentation

### Validation Commands Reference
```bash
# Level 1 - Syntax & Style:
black src/ --check        # Code formatting check
flake8 src/               # Python linting
mypy src/                 # Type checking

# Level 2 - Unit Testing:
pytest tests/test_parser.py -v                    # Parser unit tests
pytest tests/ --cov=src --cov-report=term        # Coverage report

# Level 3 - Integration:
python parser.py episode_007.md                   # Integration test with Episode 7
python scripts/validate_parser_output.py          # Validate JSON structure

# Level 4 - Feature Complete:
pytest tests/ --cov=src --cov-fail-under=80      # Full test suite with coverage
python parser.py episode_007.md && echo "✓"       # PRD-v0 validation
```

### Notes

- Parser must follow PRD-v0 "Function Over Fashion" philosophy - simple CLI with clear output
- Episode 7 is the primary validation case - all features must work with this reference script
- Output JSON must exactly match Pipeline Tag Specification for Step 2 compatibility
- Never fail completely - always produce usable JSON with warnings for issues

## Tasks with Integrated Validation

- [ ] 1.0 **Project Setup & Core Infrastructure**
  - [ ] 1.1 Create PRD-v0 compliant directory structure
    **Validation:**
    - ✅ Level 1: Directory structure matches PRD-v0 specification
    - ✅ Manual: `/src/parser.py` location confirmed
    - ✅ Manual: `/output/json/` directory exists
    
  - [ ] 1.2 Initialize Python project with dependencies
    **Validation:**
    - ✅ Level 1: `python --version` shows 3.11+
    - ✅ Level 1: `pip install -r requirements.txt` succeeds
    - ✅ Manual: All dependencies from PRD installed
    
  - [ ] 1.3 Set up basic parser skeleton with CLI argument handling
    **Validation:**
    - ✅ Level 1: `python parser.py --help` displays usage
    - ✅ Level 1: `black src/ --check` passes
    - ✅ Manual: Command structure matches `python parser.py episode_007.md`
    
  - [ ] 1.4 Create config.json with basic settings
    **Validation:**
    - ✅ Level 1: `python -m json.tool config.json` validates JSON
    - ✅ Manual: Config follows PRD-v0 simple pattern
    - ✅ Manual: Config loads successfully in parser

- [ ] 2.0 **Episode 7 Markdown Parsing Engine**
  - [ ] 2.1 Implement scene extraction (`## **[SCENE: NAME]**`)
    **Validation:**
    - ✅ Level 1: `flake8 src/parser.py` passes
    - ✅ Level 2: `pytest tests/test_parser.py::test_scene_extraction -v` passes
    - ✅ Manual: All Episode 7 scenes extracted correctly
    
  - [ ] 2.2 Implement dialogue parsing (CHARACTER: (direction) "text")
    **Validation:**
    - ✅ Level 1: `mypy src/parser.py` passes
    - ✅ Level 2: `pytest tests/test_parser.py::test_dialogue_parsing -v` passes
    - ✅ Level 2: Test coverage ≥ 80% for dialogue module
    - ✅ Manual: All Thorak/Zara dialogue extracted with directions
    
  - [ ] 2.3 Implement multimedia tag extraction ([IMG:], [SFX:], etc.)
    **Validation:**
    - ✅ Level 1: `black src/ --check` passes
    - ✅ Level 2: `pytest tests/test_parser.py::test_multimedia_tags -v` passes
    - ✅ Manual: All [IMG:], [SFX:], [MUSIC:], [AMBIENT:], [TRANSITION:] tags captured
    
  - [ ] 2.4 Add timing calculation based on dialogue length
    **Validation:**
    - ✅ Level 1: `flake8 src/utils/timing_calculator.py` passes
    - ✅ Level 2: `pytest tests/test_timing_calculator.py -v` passes
    - ✅ Manual: Timing estimates reasonable for natural speech

- [ ] 3.0 **JSON Output Generation & Pipeline Tag Compliance**
  - [ ] 3.1 Implement Pipeline Tag Specification JSON structure
    **Validation:**
    - ✅ Level 1: `mypy src/parser.py` passes
    - ✅ Level 2: `pytest tests/test_parser.py::test_json_structure -v` passes
    - ✅ Level 3: `python scripts/validate_json_schema.py output/json/episode_007.json` passes
    - ✅ Manual: JSON structure matches Pipeline Tag Specification exactly
    
  - [ ] 3.2 Add scene-based organization with nested elements
    **Validation:**
    - ✅ Level 2: `pytest tests/test_parser.py::test_scene_organization -v` passes
    - ✅ Manual: Each scene contains dialogue, images, sfx, music arrays
    - ✅ Manual: Scene boundaries correctly identified
    
  - [ ] 3.3 Implement file output with proper naming convention
    **Validation:**
    - ✅ Level 1: Output file follows `episode_XXX.json` pattern
    - ✅ Level 3: `python parser.py episode_007.md` creates `/output/json/episode_007.json`
    - ✅ Manual: File permissions and encoding correct

- [ ] 4.0 **Cost Estimation & Metadata System**
  - [ ] 4.1 Implement character counting by speaker
    **Validation:**
    - ✅ Level 1: `flake8 src/utils/cost_estimator.py` passes
    - ✅ Level 2: `pytest tests/test_cost_estimator.py::test_character_counting -v` passes
    - ✅ Manual: Character counts accurate for Thorak and Zara
    
  - [ ] 4.2 Add downstream cost estimation (ElevenLabs, images, etc.)
    **Validation:**
    - ✅ Level 2: `pytest tests/test_cost_estimator.py::test_cost_calculation -v` passes
    - ✅ Manual: Cost estimates within 5% of manual calculation
    - ✅ Manual: All cost categories included (voice, images, sfx, music)
    
  - [ ] 4.3 Generate comprehensive metadata object
    **Validation:**
    - ✅ Level 2: `pytest tests/test_parser.py::test_metadata_generation -v` passes
    - ✅ Manual: All required metadata fields present
    - ✅ Manual: Processing timestamp in ISO 8601 format
    
  - [ ] 4.4 Add validation status tracking
    **Validation:**
    - ✅ Level 2: `pytest tests/test_parser.py::test_validation_status -v` passes
    - ✅ Manual: Status correctly shows "passed", "warnings", or "failed"
    - ✅ Manual: Status reflects actual parsing results

- [ ] 5.0 **Validation & Quality Assurance**
  - [ ] 5.1 Implement warning generation with line numbers
    **Validation:**
    - ✅ Level 1: `mypy src/parser.py` passes with no type errors
    - ✅ Level 2: `pytest tests/test_parser.py::test_warning_generation -v` passes
    - ✅ Manual: Warnings include specific line numbers and suggestions
    
  - [ ] 5.2 Create validation report generation
    **Validation:**
    - ✅ Level 2: `pytest tests/test_parser.py::test_validation_report -v` passes
    - ✅ Level 3: `python parser.py episode_007.md` creates validation report
    - ✅ Manual: Report saved as `episode_007_validation.txt`
    
  - [ ] 5.3 Add debug mode with intermediate output
    **Validation:**
    - ✅ Level 2: `pytest tests/test_parser.py::test_debug_mode -v` passes
    - ✅ Level 3: `python parser.py episode_007.md --debug` creates debug files
    - ✅ Manual: Debug files in `/output/json/debug/` directory
    
  - [ ] 5.4 Implement feedback loop for script improvement
    **Validation:**
    - ✅ Level 2: `pytest tests/test_parser.py::test_feedback_generation -v` passes
    - ✅ Manual: Feedback object includes missing_tags, format_violations, quality_suggestions
    - ✅ Manual: Feedback actionable for script generator

- [ ] 6.0 **CLI Interface & Error Handling**
  - [ ] 6.1 Implement graceful error handling (never fail completely)
    **Validation:**
    - ✅ Level 2: `pytest tests/test_parser.py::test_error_handling -v` passes
    - ✅ Level 3: Parser handles malformed markdown without crashing
    - ✅ Manual: Always produces valid JSON even with errors
    
  - [ ] 6.2 Add progress display and status messages
    **Validation:**
    - ✅ Level 3: `python parser.py episode_007.md` shows clear progress
    - ✅ Manual: Success/warning/error messages are actionable
    - ✅ Manual: Progress display follows "Function Over Fashion" principle
    
  - [ ] 6.3 Complete PRD-v0 command integration
    **Validation:**
    - ✅ Level 3: `python parser.py episode_007.md` works as specified
    - ✅ Level 4: Parser integrates with overall pipeline structure
    - ✅ Manual: Output usable by Step 2 (Voice Generation) without modification

## Final Feature Validation Checklist

After completing all tasks, validate against original PRD:

### PRD Success Criteria Validation
- [ ] **Episode 7 Parsing**: All dialogue, scenes, and tags extracted correctly
  - **Command:** `python parser.py episode_007.md`
  - **Manual Check:** Compare output against manual Episode 7 analysis
  
- [ ] **Pipeline Tag Specification**: JSON output matches specification exactly
  - **Command:** `python scripts/validate_json_schema.py output/json/episode_007.json`
  - **Success:** No schema violations, all required fields present
  
- [ ] **Performance Requirements**: Processing completes in under 10 seconds
  - **Command:** `time python parser.py episode_007.md`
  - **Success:** Execution time < 10 seconds

### Technical Quality Validation
- [ ] **Code Quality**: All code meets project standards
  - **Command:** `black src/ --check && flake8 src/ && mypy src/`
  - **Success:** No formatting, linting, or type errors
  
- [ ] **Test Coverage**: Comprehensive test coverage achieved
  - **Command:** `pytest tests/ --cov=src --cov-report=term`
  - **Success:** Coverage ≥ 80%, all critical paths tested
  
- [ ] **PRD-v0 Compliance**: Follows 8-component iterative strategy
  - **Command:** `python parser.py episode_007.md`
  - **Success:** Works independently, enables Step 2

### User Experience Validation
- [ ] **Simplicity**: Single command operation works perfectly
  - **Manual Test:** Run parser with just episode file argument
  - **Success:** No complex configuration needed
  
- [ ] **Error Recovery**: Parser handles issues gracefully
  - **Manual Test:** Test with malformed markdown
  - **Success:** Produces usable output with clear warnings
  
- [ ] **Cost Tracking**: Accurate downstream cost estimation
  - **Manual Test:** Verify character counts and cost calculations
  - **Success:** Estimates match expected API usage

## PRD-v0 Integration Checkpoint

**Step 1 Deliverable**: JSON timeline with voice lines extracted
- [ ] Thorak dialogue extracted with voice directions
- [ ] Zara dialogue extracted with voice directions
- [ ] Scene structure preserved for video generation
- [ ] Multimedia tags captured for downstream processing
- [ ] Cost estimation data for budget tracking
- [ ] Validation feedback for script improvement

**Ready for Step 2**: Voice Generation can consume output without modification