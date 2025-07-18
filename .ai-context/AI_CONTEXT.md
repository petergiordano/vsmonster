# AI Project Context & Master Rulebook (Dynamic)

### **Purpose: This document serves as the evolving master briefing for any AI assistant working on this project. It accumulates context across the 5-phase workflow detailed in the [WORKFLOW_GUIDE.md](.ai-context/WORKFLOW_GUIDE.md) and must be provided at the beginning of any new development session.**

### CLI Context Files Integration
- **CLAUDE.md**, **GEMINI.md**, and **AGENTS.md** automatically reference this file for complete project context
- **Claude Code** automatically loads CLAUDE.md on startup (primary development AI)
- **Gemini CLI** loads GEMINI.md into hierarchical memory (specialized file operations)
- **OpenAI CODEX-1** references AGENTS.md for implementation guidance
- All AI assistants get the same comprehensive context through this centralized approach

---

## 1. Project Overview & Goal

- **Project Name:** versusMonster AVPS (Automated Video Podcast System)
- **Core Goal:** Transform markdown podcast scripts into complete multimedia YouTube episodes, enabling 2 episodes per week production with minimal manual intervention
- **Target Vibe:** "Excitement through reliable automation" - thrilled about creative possibilities while completely confident the system will deliver
- **Current Workflow Stage:** FOUNDATION_COMPLETE

---

## 2. Tech Stack

- **Core Language:** Python 3.11+ with virtual environment
- **Media Processing:** FFmpeg with VideoToolbox hardware acceleration (macOS)
- **Voice Generation:** ElevenLabs API with streaming capabilities
- **Key Libraries:** elevenlabs, pydub, ffmpeg-python, moviepy, python-dotenv, opencv-python, pillow
- **Interface:** Command-line first, ASCII progress indicators
- **Asset Management:** Simple folder-based library structure
- **Environment:** macOS optimized with Homebrew dependencies

---

## 3. File & Folder Structure

- **`src/`**: Contains all application source code for the 8-component pipeline
- **`tests/reference/`**: Test episodes and reference files (e.g., episode_2_ex_final.md)
- **`output/`**: Generated content organized by episode and component
  - `output/json/`: Parsed script data (includes debug/ subdirectory)
  - `output/voices/`: Generated voice files (organized by episode)
  - `output/audio/`: Mixed audio tracks (Component 3 target)
  - `output/videos/`: Final video outputs (Components 4-8 target)
- **`assets/`**: Reusable media library
  - `assets/branding/`: Logo and brand assets
  - `assets/images/`: Background images, character portraits, scenes
  - `assets/sfx/`: Sound effects (combat, ambient, UI)
  - `assets/music/`: Themes, ambient music, stings
  - `assets/templates/`: Template files for episodes
- **`tests/`**: Test suite for all pipeline components
  - `tests/fixtures/`: Test fixtures
  - `tests/reference/`: Reference test episodes
- **`.ai-context/`**: AI agent documentation and context files
  - `.ai-context/AI_CONTEXT.md`: This master context file
  - `.ai-context/WORKFLOW_GUIDE.md`: VSMonster workflow guide
- **`config/`**: Configuration files and schema definitions
  - `config/config.json`: Central pipeline configuration
  - `config/notion-database-schema.json`: Task management schema
- **`docs/`**: Project documentation
  - `docs/architecture/`: Foundation documents (Roadmap, VibeTesting, etc.)
  - `docs/specifications/`: Technical specs, schemas, and feature specifications
    - `docs/specifications/PRD.md`: Master product requirements
    - `docs/specifications/dev-cycle.md`: High-level development workflow
    - `docs/specifications/feat_spec-[component-name].md`: Component feature specifications
  - `docs/setup/`: Development setup guides
- **`tools/`**: Utility scripts and setup tools
  - `tools/process_episode.py`: Episode post-processing
  - `tools/setup_validation.py`: Environment validation
- **`archive/`**: Historical documents and deprecated files
  - `archive/codex_task_logs/`: Detailed implementation logs from Codex

---

## 4. Coding Conventions & Style

- **Language:** Python 3.11+ (for modern type hints and features)
- **Formatting:** All code formatted with `black` (included in requirements.txt)
- **Linting:** Use `flake8` for code quality checking
- **Naming:** Use `snake_case` for variables and functions, `PascalCase` for classes
- **Docstrings:** All functions must have Google-style docstrings
- **Error Handling:** Fail fast with clear error messages; all external API calls wrapped in try/except
- **CLI Design:** ASCII progress bars, clear status messages, actionable error guidance
- **File Naming:** Use episode naming convention (e.g., episode_2_ex_final.md, episode_007.json)

---

## 5. Global AI Instructions

- **Episode 7 First:** Always validate new features against Episode 7 reference implementation
- **Simple, Lovable, Complete:** Follow SLC framework - build simple, delightful, complete features
- **Command-Line Focus:** Prioritize CLI interfaces with clear progress indication
- **Cost Awareness:** Track API usage and provide cost estimation for each component
- **Fault Tolerance:** Build resume capability and component isolation
- **Asset Library Integration:** Always consider reusable assets when building features
- **Script Generator Feedback:** Establish feedback loops to improve input quality

---

## 6. Development Workflow Architecture

### **Two-Tier Workflow System**
The project employs a two-tier development process:

#### High-Level Component Development Cycle
- **Location**: `docs/specifications/dev-cycle.md`
- **Process**: PRD Review → Feature Spec Generation → Codex Implementation → PR Review → PRD Update
- **Purpose**: Macro workflow for complete component development
- **AI Coordination**: Claude Chat (planning) → Codex (implementation) → Claude Code (review)

#### Detailed Implementation Workflow  
- **Location**: `.ai-context/WORKFLOW_GUIDE.md`
- **Process**: Task selection → Implementation → Validation → Completion
- **Purpose**: Micro workflow for task management and quality assurance
- **AI Coordination**: Claude Code primary with Gemini CLI for specific operations

### **Feature Specification System**
- **Template**: `docs/specifications/FEATURE_SPEC_TEMPLATE.md`
- **Naming**: `feat_spec-[component-name].md`
- **Required Sections**: Purpose, scope, user flows, edge cases, logic requirements, constraints, test plan
- **Usage**: Input for Codex implementation, reference for all development work

### **Two-Tier Logging System**
- **High-Level Dashboard**: `docs/specifications/workflow-log.md` - executive overview and metrics
- **Detailed Task Logs**: `archive/codex_task_logs/feat_spec-[component-name]-tasks.md` - comprehensive implementation audit trail
- **Template**: `archive/codex_task_logs/TASK_LOG_TEMPLATE.md`
- **Purpose**: Scalable tracking from quick status checks to deep implementation details

## 7. Task Management Architecture

### **Two-Tier Task Management System**
The project employs a clear division of task management responsibilities:

#### Codex-Managed Tasks (Core Product Components)
- **Scope**: Components 1-8 of the main pipeline (Script Parser → Batch Processing)
- **Task Creation**: Codex breaks down feature specifications into granular implementation tasks
- **Task Execution**: Codex self-manages implementation according to feature specs
- **Task Tracking**: Detailed logs maintained in `archive/codex_task_logs/feat_spec-[component-name]-tasks.md`
- **Autonomy**: Codex operates independently without Notion database dependency

#### Notion Database Tasks (Non-Core Support)
- **Scope**: Housekeeping, architectural, infrastructure, process, research, and maintenance tasks
- **Database**: `vmonster-dev-backlog` (22f859c6-e596-8007-86c6-c1df9f865855)
- **Access Control**: Claude Code accesses ONLY when explicitly instructed by user
- **Task Examples**: Documentation updates, refactoring, tooling, CI/CD, security, performance optimization
- **User Direction Required**: No autonomous Notion database access permitted

#### Task Type Decision Matrix
- **Feature Implementation** → Codex self-manages
- **Bug Fixes in Core Components** → Codex self-manages  
- **New Core Component** → Codex self-manages
- **Documentation Updates** → Notion database (user-directed)
- **Tool/Infrastructure Changes** → Notion database (user-directed)
- **Process Improvements** → Notion database (user-directed)
- **Architecture Decisions** → Notion database (user-directed)

## 8. Context Handoff Protocols

### **Between Chat AI (Strategist) and CLI AI (Implementer)**
- **Context Transfer Method:** Always provide this complete AI_CONTEXT.md file.
- **Role Boundaries:** The Chat AI (Strategist) plans and prepares prompts. The CLI AI (Implementer) executes specific technical tasks.
- **Validation Points:** The CLI AI should confirm its understanding of the context before beginning implementation.

### **Workflow Context Accumulation**
- **Phase 1: Project Initialization:** Foundation context (project setup, goals, constraints).
- **Phase 2: Brief AI Assistants:** Shared contextual understanding across the AI team.
- **Phase 3: Create PRD:** Feature context (PRD requirements, user stories, acceptance criteria).
- **Phase 4: Generate Task List:** Implementation context (task breakdown, file structure, dependencies).
- **Phase 5: Execute Task List:** Execution context (code patterns, validation results, lessons learned).

---

## 7. Current Project Context State

### **Completed Features**
**✅ Script Parser (Component 1) - COMPLETE**
- **Status:** ALL TASKS COMPLETE (Tasks 1.0 through 6.0)
- **Completion Date:** 2025-01-08
- **Success Criteria Met:** ✅ Parses Episode 7 with 100% accuracy
- **Key Features Implemented:**
  - Scene extraction with proper markdown parsing
  - Character dialogue parsing with voice directions
  - Multimedia tag extraction ([IMG:], [SFX:], [MUSIC:], [AMBIENT:], [TRANSITION:])
  - Timing calculation based on dialogue length
  - JSON output with Pipeline Tag Specification compliance
  - Cost estimation for all downstream components
  - Comprehensive validation and error handling
  - Graceful degradation - never fails completely
  - Clear progress reporting with 5-step status updates
- **Performance:** 0.003s processing time (well under 10s requirement)
- **Output:** Structured JSON ready for Voice Generation (Component 2)
- **Command:** `python parser.py episode_2_ex_final.md`

### **Active Features** (Features currently in development)
**Ready to Start: Voice Generation (Component 2)**
- **Status:** NOT STARTED - Awaiting implementation
- **Priority:** CRITICAL - Next component in pipeline
- **Success Criteria:** Generate individual WAV files for each character line
- **Key Context:** Must integrate with ElevenLabs API for Thorak/Zara voices
- **Integration Points:** Consumes JSON from Script Parser, outputs voice files
- **Validation:** Voice files must match character personalities and directions

### **Planned Features** (Next in pipeline)
- **Voice Generation (Component 2)**: ElevenLabs integration with character-specific settings
- **Audio Assembly (Component 3)**: Combine voice files with timing synchronization
- **Video Generation (Component 4)**: Create MP4 with static background
- **Asset Library Foundation**: Simple folder-based management with auto-discovery

### **Architecture Decisions Made**
- **Decision:** 8-component iterative pipeline approach
- **Rationale:** Each component delivers independent value and can be validated separately
- **Impact:** Enables systematic development and easy debugging
- **Date:** 2025-01-07

- **Decision:** Command-line first with ASCII progress indicators
- **Rationale:** Simple, Lovable, Complete framework - focus on functionality over UI
- **Impact:** Faster development, easier automation, professional developer experience
- **Date:** 2025-01-07

- **Decision:** Episode 7 as universal test case
- **Rationale:** Complete, representative example with all required elements
- **Impact:** Consistent validation across all components
- **Date:** 2025-01-07

### **Known Patterns & Conventions Discovered**
- **Pattern:** Folder-based asset organization
- **Location:** `/assets` directory with logical subdirectories
- **Usage:** Auto-discovery for reusable images, SFX, music

- **Pattern:** Episode naming convention
- **Location:** All file operations use episode_XXX format
- **Usage:** Consistent file naming across all components and outputs

- **Pattern:** JSON schema for component handoffs
- **Location:** Output from Script Parser, input to Voice Generation
- **Usage:** Structured data exchange between pipeline components

---

## 8. Plan Mode Best Practices (Project-Specific)

### **When to ALWAYS Use Plan Mode**
- **Component Integration:** Planning how new pipeline components integrate with existing ones
- **Episode 7 Analysis:** Understanding script structure before building parsers
- **API Cost Planning:** Estimating and optimizing API usage before implementation
- **Asset Library Design:** Planning media organization and discovery patterns

### **Project-Specific Plan Mode Guidance**
- **8-Component Pipeline:** Always consider impact on downstream components
- **ElevenLabs Integration:** Plan API usage patterns and cost implications
- **FFmpeg Operations:** Understand hardware acceleration and output format requirements
- **Asset Management:** Consider reusability and organization patterns

### **Context Validation Checkpoints in Plan Mode**
- [ ] Understand current pipeline component status and dependencies
- [ ] Review Episode 7 structure for parsing/processing requirements
- [ ] Validate API cost implications and budget constraints
- [ ] Confirm asset library integration patterns
- [ ] Verify output format compatibility with next component in pipeline

---

## 9. Validation & Quality Gates

### **Progressive Validation Levels**
1. **Syntax Level:** Code compiles, follows formatting standards
2. **Unit Test Level:** All new functionality has passing tests
3. **Integration Level:** Changes work with existing system
4. **Feature Level:** Complete feature meets PRD success criteria
5. **Architecture Level:** Implementation follows established patterns

### **Context Validation Commands**
```bash
# Level 1: Syntax & Style validation
source venv/bin/activate
black src/ --check
flake8 src/

# Level 2: Unit test execution  
pytest tests/ -v

# Level 3: Integration testing with Episode 7
python parser.py scripts/episode_2_ex_final.md
python tools/setup_validation.py

# Level 4: Full validation suite
python -m pytest tests/ --cov=src
python tools/setup_validation.py
```

---

## 10. Context Evolution Log

### **Context Updates** (Track how context evolves during development)
- **Date:** 2025-01-07
- **Stage:** Foundation Interview Complete
- **Context Added:** Complete foundation documents (Roadmap, VibeTesting, ComponentLibrary, SLC_Session_Notes)
- **Reason:** Establishes clear project vision, user experience goals, and development strategy for 8-component pipeline

### **Lessons Learned** (Accumulate insights across features)
- **Lesson:** Episode 7 provides comprehensive test case covering all system requirements
- **Context:** Foundation interview revealed Episode 7 contains dialogue, SFX, music, images, scene transitions
- **Application:** Use Episode 7 as validation test for every component in the pipeline

- **Lesson:** Simple, Lovable, Complete framework critical for maintaining focus
- **Context:** User emphasized avoiding complexity while building delightful, fault-tolerant system
- **Application:** Prioritize CLI simplicity, clear progress indication, and robust error handling

- **Lesson:** Configuration system enables PRD-v0 simplicity with powerful flexibility
- **Context:** Task 1.4 showed config.json provides central control while maintaining simple CLI
- **Application:** Store pipeline context, cost estimation, and validation rules in config for easy modification

- **Lesson:** Graceful degradation prevents pipeline failures
- **Context:** Parser designed to never fail completely, always produce usable JSON with warnings
- **Application:** Each component should handle errors gracefully to maintain automation flow

- **Lesson:** Clear progress reporting enhances user confidence
- **Context:** Task 6.2 implementation showed 5-step progress updates with emojis improve UX
- **Application:** All pipeline components should show clear step-by-step progress with visual indicators

- **Lesson:** Emergency output creation ensures debugging capability
- **Context:** Task 6.1 added emergency JSON output even during catastrophic failures
- **Application:** Components should always produce some output for debugging, even partial results

---

## 11. CLI Assistant Integration & Commands

### **CLI Assistant Context Loading**
- **Claude Code:** Automatically loads `CLAUDE.md` which references this file
- **Gemini CLI:** Automatically loads `GEMINI.md` into hierarchical memory
- **Both assistants:** Get complete project context through centralized AI_CONTEXT.md

### **Project-Specific Validation Commands**
```bash
# Level 1 (Syntax & Style):
black src/ --check              # Code formatting validation
flake8 src/                     # Python linting
mypy src/                       # Type checking validation

# Level 2 (Unit Tests):
pytest tests/test_parser.py -v  # Parser unit tests
pytest tests/ --cov=src         # Test coverage reporting

# Level 3 (Integration):
python parser.py scripts/episode_2_ex_final.md # Integration test with Episode 7
# Validation integrated into parser output

# Level 4 (Full Validation):
pytest tests/ --cov=src --cov-fail-under=80 # Full test suite with coverage
python parser.py scripts/episode_2_ex_final.md && echo "✓" # PRD-v0 validation
```

### **CLI Assistant Best Practices**
- **Always read this complete AI_CONTEXT.md file first**
- **Use validation commands after each change**
- **Follow established patterns in existing codebase**
- **Ask for clarification if context is unclear**
- **Claude Code:** Use Plan Mode (Shift+Tab twice) for complex analysis
- **Gemini CLI:** Use `/memory show` to verify loaded context

---

## 12. Environment Setup & Integration Patterns

### **Python/FFmpeg Integration Strategy**
- **Primary Approach:** Direct subprocess control for maximum flexibility and performance
- **FFmpeg Path:** System-installed via Homebrew (`/opt/homebrew/bin/ffmpeg` on Apple Silicon)
- **Hardware Acceleration:** Use VideoToolbox codecs on macOS (`h264_videotoolbox`, `hevc_videotoolbox`)
- **Output Format:** MP4 container, H.264 video codec, AAC audio codec, 1920x1080 @ 30fps

### **ElevenLabs API Integration**
- **SDK:** Official Python SDK (`elevenlabs` package)
- **Voice Models:** Eleven Multilingual v2 for highest quality
- **Streaming:** Use streaming API for real-time voice generation
- **Voice Settings:** 
  - Thorak: Stability 0.75, Similarity 0.85 (consistent scholarly tone)
  - Zara: Stability 0.45, Similarity 0.75 (more emotional variation)

### **API Key Management**
- **Method:** python-dotenv for environment variables
- **File:** `.env` in project root (NEVER commit to git)
- **Loading:** `load_dotenv()` at application startup
- **Access:** `os.getenv('ELEVENLABS_API_KEY')`
- **Security:** Add `.env` to `.gitignore` immediately

### **Core Dependencies**
```
elevenlabs      # Official ElevenLabs SDK
pydub           # Audio manipulation
ffmpeg-python   # FFmpeg Python wrapper
moviepy         # High-level video editing
python-dotenv   # Environment variable management
requests        # HTTP requests
opencv-python   # Image processing
pillow          # Image manipulation
imageio         # Image I/O operations
imageio-ffmpeg  # FFmpeg plugin for imageio
```

### **Project Media Structure**
```
versusMonster/
├── scripts/          # Input markdown scripts
├── output/
│   ├── json/        # Parsed script data
│   ├── voices/      # Generated voice files
│   ├── audio/       # Mixed audio tracks
│   └── videos/      # Final video outputs
├── assets/
│   ├── images/      # Background images
│   ├── sfx/         # Sound effects
│   └── music/       # Background music
└── reference/       # Test episodes
```

### **Validation Requirements**
- Python ≥ 3.9 (for modern type hints and features)
- FFmpeg ≥ 5.0 (for Apple Silicon optimization)
- All output directories must exist before processing
- .env file must contain valid ELEVENLABS_API_KEY
- Test with Episode 7 before processing other episodes

### **Git Workflow & Version Control**
- **Primary Tool:** GitHub Desktop for commits and pushes
- **Repository:** https://github.com/petergiordano/vsmonster.git
- **Branch Strategy:** Main branch for stable development
- **Commit Frequency:** Regular commits after completing major setup steps or features
- **Security:** Never commit .env files or API keys (protected by .gitignore)
- **Template Updates:** Use `git pull template main` for framework improvements

### **CRITICAL: Pipeline Tag Standards**
- **Specification Document:** `docs/pipeline_tag_specification.md` (MUST READ)
- **Purpose:** Standardized tags enable automated service integration without human intervention
- **Tag Categories:** SCENE, CHARACTER DIALOGUE, [IMG:], [SFX:], [MUSIC:], [AMBIENT:], [TRANSITION:]
- **Service Integration:** Tags directly map to ElevenLabs, image generation, SFX, music APIs
- **Quality Requirement:** All script generator output must follow exact tag formats
- **Cost Tracking:** Tag-based BOM calculation for all service usage
- **Validation:** Automated feedback loop ensures script generator produces parseable content

**Critical Tag Examples:**
```markdown
THORAK: (Gravelly, impressed) "Dialogue text"
[IMG: image_id] PROMPT: "Detailed generation prompt with style consistency"
[SFX: earth_rumbling_deep]
[MUSIC: main_theme_intro]
```

---

## IMPORTANT: Context Continuity Instructions

### **For New AI Sessions:**
1. **Always start by reading this entire document**
2. **Pay special attention to "Current Project Context State"**
3. **Review any active features and their current status**
4. **Understand architectural decisions before making changes**
5. **Use Plan Mode to validate context understanding**

### **For Context Updates:**
1. **Update "Current Project Context State" as features progress**
2. **Add architectural decisions to the appropriate section**
3. **Record new patterns discovered during development**
4. **Log important lessons learned for future reference**