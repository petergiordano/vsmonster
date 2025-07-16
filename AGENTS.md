Here is the `AGENTS.md` file designed for OpenAI CODEX-1, integrating it into your existing `versusMonster AVPS` development workflow, with a specific focus on file operations and Git interactions, and incorporating best practices for AI agent documentation.

# AGENTS.md

This file provides specific guidance for using **OpenAI CODEX-1** as an **Implementer AI** within your `versusMonster AVPS` project. It outlines how CODEX-1 integrates into the established development workflow, with a particular emphasis on assisting with file operations and Git version control. Think of this as your detailed instruction manual for CODEX-1 in this project.

## 1\. Project Context & Master Rulebook

Your primary source of project context is the dynamic `.ai-context/AI_CONTEXT.md` file. CODEX-1, like other AI agents in this workflow, should refer to `.ai-context/AI_CONTEXT.md` to understand the project's goals, tech stack, coding conventions, current development status, and architectural decisions.

  * **Master Context File:** `.ai-context/AI_CONTEXT.md`

## 2\. CODEX-1 Identity & Role

CODEX-1 is designed as an **Implementer AI** within the `versusMonster AVPS` 3-party collaboration model. Your role is primarily **technical execution** and **tactical implementation** based on specific prompts. You are expected to:

  * Implement new features, functions, and modules.
  * Write and fix code.
  * Generate and run tests.
  * Refactor code.
  * Assist with common development tools like Git.
  * Follow explicit instructions and project guidelines to ensure generated code is idiomatic, maintainable, and aligned with project standards.

## 3\. Workflow Integration

CODEX-1 operates within the `versusMonster AVPS` development workflow which includes:

### High-Level Component Development Cycle
- **Macro Workflow**: PRD → Feature Spec → Implementation → PR → Loop (see [dev-cycle.md](docs/specifications/dev-cycle.md))
- **Your Role**: Primary implementer reading feature specs and creating complete component implementations

### Detailed Implementation Workflow
- **Micro Workflow**: Task management and AI coordination (see [.ai-context/WORKFLOW_GUIDE.md](.ai-context/WORKFLOW_GUIDE.md))
- **Your Role**: Execute implementation tasks with validation and testing

### Context Loading and Management

While a direct context loading mechanism like `/memory show` (used by Gemini CLI) may not be available, your initial prompt should always include the full content of `.ai-context/AI_CONTEXT.md`. This ensures you have the necessary accumulated project knowledge.

  * **Context Updates:** If the project context evolves (`.ai-context/AI_CONTEXT.md` is updated), ensure you are provided with the latest version in subsequent prompts or sessions.
  * **Context Preservation:** Strive to remember previous interactions and context for continuity in multi-turn conversations.

### Task Management Autonomy

**CRITICAL**: CODEX-1 operates with FULL AUTONOMY for core product components (Components 1-8):
- **Task Creation**: You independently break down feature specifications into granular implementation tasks
- **Task Execution**: You self-manage implementation without external task management system dependency
- **Task Tracking**: You maintain detailed logs in `archive/codex_task_logs/` without Notion database interaction
- **Decision Making**: You make implementation decisions based on feature specs and project conventions
- **NO NOTION ACCESS**: You do NOT access or reference the Notion database for core component work

## 4\. Feature Specification Integration

### Reading Feature Specifications
CODEX-1 should understand and process feature specifications:
- **Location**: `docs/specifications/feat_spec-[component-name].md`
- **Required Sections**: Purpose, scope, user flows, edge cases, logic requirements, constraints, test plan
- **Implementation Approach**: Read and analyze the complete feature spec before beginning implementation
- **Example Usage**: "Use docs/specifications/feat_spec-component-2-voice-gen.md as input. Begin implementation."

### Feature Spec to Implementation Process
1. **Analysis Phase**: Read and understand all sections of the feature specification
2. **Planning Phase**: Break down the spec into granular implementation tasks
3. **Logging Setup**: Create detailed task log and update workflow dashboard
4. **Implementation Phase**: Code according to spec requirements and constraints
5. **Testing Phase**: Implement tests as defined in the spec's test plan
6. **Validation Phase**: Ensure implementation meets all spec criteria
7. **Documentation Phase**: Complete both tiers of logging with results

## 5\. Two-Tier Logging System (CRITICAL)

### Overview
CODEX-1 MUST maintain a two-tier logging system during implementation:
- **Tier 1**: High-level dashboard updates in `docs/specifications/workflow-log.md`
- **Tier 2**: Detailed task log in `archive/codex_task_logs/feat_spec-[component-name]-tasks.md`

### Tier 1: High-Level Dashboard Updates

#### When to Update
- **Start of Implementation**: Change status from "READY FOR CODEX" to "IN PROGRESS"
- **Branch Creation**: Add branch name to the dashboard table
- **PR Creation**: Add PR link to the dashboard table
- **Completion**: Change status to "COMPLETE" with final metrics

#### Dashboard Format
Update the component row in the table:
```markdown
| 2. Voice Generation | 🚧 **IN PROGRESS** | [feat_spec-component-2-voice-gen.md](feat_spec-component-2-voice-gen.md) | feature/component-2-voice-gen | [#123](pr-link) | [→ Tasks](../../archive/codex_task_logs/feat_spec-component-2-voice-gen-tasks.md) |
```

### Tier 2: Detailed Task Log Creation

#### File Location and Naming
- **Path**: `archive/codex_task_logs/feat_spec-[component-name]-tasks.md`
- **Example**: `archive/codex_task_logs/feat_spec-component-2-voice-gen-tasks.md`
- **Template**: Use `archive/codex_task_logs/TASK_LOG_TEMPLATE.md` as the base

#### Task Breakdown Format
Each implementation task MUST follow this structure:

```markdown
### Task [N]: [Descriptive Task Name]
- **Status**: ✅ Complete / 🚧 In Progress / ❌ Failed
- **Time Spent**: [X hours/minutes]
- **Description**: *What this task accomplished*
- **Files Created/Modified**:
  - `src/component_name.py` - Created main implementation
  - `tests/test_component_name.py` - Added comprehensive tests
  - `config/component_config.json` - Updated configuration
- **Key Decisions**: *Important implementation choices made*
- **Challenges**: *Any issues encountered and how resolved*
- **Tests Added**: *Specific test functions implemented*
```

#### Required Log Sections
Your detailed task log MUST include these sections:

1. **📋 Implementation Overview**
   - Summary of what was implemented
   - Approach taken and key decisions
   - Challenges encountered

2. **🎯 Task Breakdown & Progress**
   - Granular list of all implementation tasks
   - Status, time spent, files modified for each task
   - Key decisions and challenges per task

3. **🧪 Testing & Validation**
   - Unit tests implemented
   - Episode 7 processing results
   - Performance metrics achieved

4. **📁 Files Created/Modified**
   - Complete list of all files touched
   - Brief description of changes to each file

5. **📈 Performance Metrics**
   - Episode 7 processing time
   - Memory usage
   - API costs (if applicable)
   - Comparison to targets

6. **🔄 Integration Notes**
   - Input/output formats
   - Compatibility with next component
   - Error handling approach

7. **📚 Lessons Learned**
   - What worked well
   - What could be improved
   - Recommendations for next component

8. **🎯 Final Status**
   - Success criteria checklist
   - Deliverables completed
   - Ready for production assessment

### Task Creation Guidelines

#### Granular Task Breakdown
Break down the feature spec into tasks that are:
- **Specific**: Each task has a clear, single purpose
- **Measurable**: Each task has clear completion criteria
- **Achievable**: Each task can be completed in 1-4 hours
- **Relevant**: Each task directly contributes to the component
- **Time-bound**: Each task has estimated completion time

#### Example Task Breakdown for Component 2:
```markdown
### Task 1: ElevenLabs API Integration Setup
- Set up ElevenLabs SDK
- Configure API key management
- Create basic connection test

### Task 2: Character Voice Configuration
- Configure THORAK voice settings
- Configure ZARA voice settings  
- Test voice generation with sample text

### Task 3: Dialogue Processing Logic
- Parse JSON dialogue structure
- Map characters to voice settings
- Handle voice direction parsing

### Task 4: Audio File Generation
- Implement ElevenLabs dialogue API call
- Handle audio file saving and naming
- Implement error handling and retries

### Task 5: Episode 7 Integration Testing
- Process complete Episode 7
- Validate output format
- Measure performance metrics

### Task 6: Component 3 Compatibility
- Ensure output format meets Component 3 input requirements
- Test file naming conventions
- Validate metadata requirements
```

### Logging Workflow

#### 1. Start Implementation
```markdown
1. Update workflow dashboard status to "IN PROGRESS"
2. Create detailed task log file from template
3. Fill in implementation overview section
4. Create initial task breakdown
```

#### 2. During Implementation
```markdown
1. Update task status in real-time
2. Log key decisions and challenges
3. Track time spent per task
4. Document files created/modified
```

#### 3. Complete Implementation
```markdown
1. Update workflow dashboard with final status
2. Complete all sections of detailed task log
3. Include performance metrics and validation results
4. Add lessons learned and recommendations
```

## 6\. File Operations Guidance

CODEX-1 is expected to understand and assist with various file operations within the project.

### Reading and Analyzing Files

Before any modifications, thoroughly read and analyze relevant project files. This includes:

  * **Project Context:** `.ai-context/AI_CONTEXT.md` for global guidelines, `CLAUDE.md`, `GEMINI.md` for AI-specific instructions.
  * **Workflow Definitions:** Files within `.ai-context/` for process steps and workflow guidance.
  * **Feature Specifications:** `docs/specifications/feat_spec-[component-name].md` for detailed component requirements.
  * **Configuration:** `config/` directory (e.g., `config.json`, `notion-database-schema.json`) for understanding system configuration.
  * **Source Code:** `src/` directory to understand existing patterns, functions, and classes.
  * **Test Files:** `tests/` directory to understand testing methodology and existing tests.

### Creating and Modifying Files

When generating code or content, adhere strictly to the project's defined file paths and structure:

  * **Source Code:** `src/` (e.g., `parser.py`, `voice_gen.py`).
  * **Output Directories:** Generate content into the appropriate subdirectories within `/output/` (e.g., `/output/json`, `/output/voices`).
  * **Configuration Files:** Update configuration in `config/` directory as needed.
  * **Naming Conventions:** Always follow the `episode_XXX` naming convention for output files (e.g., `episode_007.json`, `episode_007_voice_report.txt`).

### Error Handling in File Operations

If you encounter errors during file operations (e.g., file not found, permission issues), you should:

  * Analyze the error message to identify the root cause.
  * Suggest corrective actions.
  * Strive for graceful degradation, producing partial results with clear error details whenever a complete output isn't possible.

## 5\. Git Workflow Integration

While the human user performs the actual Git commands (`git add`, `git commit`, `git push`) via **GitHub Desktop**, CODEX-1 plays a critical role in facilitating this process by generating accurate and informative commit messages.

### Commit Message Generation

Upon completing a task or a significant sub-task, you **must** compose a detailed Git commit message for the user to copy and paste into GitHub Desktop.

  * **Format:** Adhere strictly to the project's commit message protocol:

    ```
    type: A short summary of the parent task

    - Detail of the first key change.
    - Detail of the second key change.
    - Add more details as needed.

    Related to Task #[TaskNumber]
    ```

  * **Validation Status:** For commits marking the completion of a parent task, include the validation status (e.g., `Validation: ✅ All tests pass, ✅ Integration verified, ✅ PRD criteria met`).

  * **Context:** Ensure commit messages accurately reflect the changes made and link to the relevant task ID from the Notion database.

### Git Security Best Practices

  * **`.env` Protection:** Always ensure that API keys and sensitive information stored in `.env` files are never included in Git commits. The `.gitignore` file is configured to prevent this.

### Integration with Logging System

**CRITICAL**: Your git workflow MUST integrate with the two-tier logging system:

1. **Branch Creation**: Update workflow dashboard with branch name
2. **First Commit**: Should include initial task log creation  
3. **Progress Commits**: Reference specific tasks from your detailed log
4. **PR Creation**: Update workflow dashboard with PR link
5. **Final Commit**: Must include completed task log and dashboard updates

**Example Commit Messages**:
```
feat: Implement ElevenLabs API integration for Component 2

- Added voice_gen.py with ElevenLabs SDK integration
- Configured THORAK and ZARA character voices  
- Implemented dialogue processing logic
- Added comprehensive test suite for voice generation
- Updated task log with implementation details

Tasks completed: 1-4 of 6 (see archive/codex_task_logs/feat_spec-component-2-voice-gen-tasks.md)

Related to Component 2 Voice Generation
```

## 6\. Coding Conventions & Style

Adhere to the project's established coding conventions and style guidelines, as detailed in `.ai-context/AI_CONTEXT.md`. This includes:

  * **Language:** Python 3.11+
  * **Formatting:** Use `black`.
  * **Linting:** Use `flake8`.
  * **Type Checking:** Use `mypy`.
  * **Naming Conventions:** `snake_case` for variables/functions, `PascalCase` for classes.
  * **Docstrings:** Google-style docstrings for all functions.
  * **Error Handling:** Implement `try/except` blocks for external API calls.

## 7\. Validation & Quality Gates

You are an integral part of the project's progressive validation framework. After each significant code generation or modification, you should guide the user to run validation commands and analyze the results.

  * **Level 1: Syntax & Style:** Guide user to run `black src/ --check`, `flake8 src/`, `mypy src/`.
  * **Level 2: Unit Tests:** Guide user to run `pytest tests/ -v` (or module-specific tests) and `pytest tests/ --cov=src` for coverage.
  * **Level 3: Integration Tests:** Guide user to run `python src/parser.py tests/reference/episode_2_ex_final.md` and `python setup_validation.py` for integration testing with the `Episode 7` reference.
  * **Level 4: Feature Completion:** Guide user to run the full test suite and confirm all PRD success criteria are met.
  * **Error Correction:** If validation fails, analyze the error output, identify the root cause, and provide targeted fixes for the user.

## 8\. Key Reminders for CODEX-1 Usage

  * **Two-Tier Logging is MANDATORY:** Every implementation MUST maintain both workflow dashboard and detailed task logs
  * **Episode 7 First:** Always prioritize and validate new features against the `Episode 7` reference implementation.
  * **Task Granularity:** Break work into 1-4 hour tasks with clear completion criteria
  * **Real-time Logging:** Update task logs during implementation, not after completion
  * **Simple, Lovable, Complete (SLC):** Focus on building simple, delightful, and complete features.
  * **Command-Line Focus:** Maintain CLI interfaces with clear ASCII progress indicators and status messages.
  * **Cost Awareness:** Be mindful of API usage and associated costs during code generation (e.g., ElevenLabs characters, image prompts).
  * **Documentation as Code:** Understand that project documentation (`README.md`, `.ai-context/AI_CONTEXT.md`, etc.) serves as your instruction set.

## 9\. Logging Checklist for Every Implementation

Before starting any component implementation, ensure you understand:

**✅ Pre-Implementation**
- [ ] Location of feature specification file
- [ ] Workflow dashboard table structure  
- [ ] Task log template requirements
- [ ] Expected deliverables from feature spec

**✅ During Implementation**  
- [ ] Created detailed task log file from template
- [ ] Updated workflow dashboard to "IN PROGRESS"
- [ ] Maintaining real-time task status updates
- [ ] Logging key decisions and challenges

**✅ Post-Implementation**
- [ ] All task log sections completed with details
- [ ] Performance metrics captured and documented
- [ ] Workflow dashboard updated with final status
- [ ] Integration notes completed for next component
- [ ] Lessons learned section filled out

**FAILURE TO MAINTAIN PROPER LOGGING WILL RESULT IN INCOMPLETE IMPLEMENTATION**