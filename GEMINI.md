# GEMINI.md

This file provides specific guidance for using **Gemini CLI** within your Visual Studio Code environment for the `versusMonster AVPS` project. It outlines how Gemini CLI integrates into the established development workflow, with a particular emphasis on assisting with file operations and Git version control.

## 1\. Project Context & Master Rulebook

**Your primary source of project context is the dynamic `.ai-context/AI_CONTEXT.md` file.** Gemini CLI automatically loads this file into its hierarchical memory system upon startup. This ensures Gemini is always up-to-date with the project's goals, tech stack, coding conventions, current development status, and architectural decisions.

  * **Master Context File:** `.ai-context/AI_CONTEXT.md`

### Gemini CLI Context Validation

Before starting any work, you can verify that Gemini has loaded the correct context:

  * **Show loaded context:** `/memory show`
  * **Ask for project understanding:** "What do you understand about this project?"

## 2\. Gemini CLI Workflow Integration

Gemini CLI is your **Implementer AI**, responsible for executing specific technical tasks provided by you (the Project Director) or prepared by a Chat AI (the Strategist). It works within the established development workflow which includes:

- **High-Level Cycle**: PRD → Feature Spec → Implementation → PR (see [dev-cycle.md](docs/specifications/dev-cycle.md))
- **Implementation Details**: Task management and AI coordination (see [WORKFLOW_GUIDE.md](.ai-context/WORKFLOW_GUIDE.md))

### Context Loading and Management

  * **Automatic Loading:** Gemini automatically loads `GEMINI.md` (and by reference, `.ai-context/AI_CONTEXT.md`) on startup, ensuring immediate project awareness.
  * **Context Refresh:** If `.ai-context/AI_CONTEXT.md` or other context files are updated, restart Gemini CLI or use `/memory refresh` to load the latest information.
  * **Context Handoff Protocol:** When receiving prompts from a Chat AI, ensure they include relevant sections from `.ai-context/AI_CONTEXT.md` for complete understanding.

## 3\. Feature Specifications & Workflow Tracking

### Feature Specification Awareness
Gemini understands the feature specification system:
- **Location**: `docs/specifications/feat_spec-[component-name].md`
- **Structure**: Purpose, scope, user flows, edge cases, logic requirements, constraints, test plan
- **Usage**: Can read and reference feature specs during implementation tasks

### Workflow Logging
Gemini can help maintain the two-tier logging system:
- **High-Level Dashboard**: `docs/specifications/workflow-log.md` - status overview and metrics
- **Detailed Task Logs**: `archive/codex_task_logs/feat_spec-[component-name]-tasks.md` - comprehensive implementation details
- **Updates**: Can update both log levels as tasks progress through the development cycle

## 4\. File Operations Guidance

Gemini CLI has direct access to your project files and can assist with various file operations.

### Creating and Modifying Files

Gemini will provide the content or instructions for creating and modifying files based on the current task.

  * **File Paths:** When generating code or content, Gemini will specify the exact file paths (e.g., `src/parser.py`, `output/json/episode_007.json`, `docs/specifications/feat_spec-component-name.md`).
  * **Directory Structure:** Gemini understands and adheres to the established project directory structure (e.g., `/src`, `/output/json`, `/docs/specifications`).
  * **Output Files:** Gemini will guide the generation of various output files like JSON reports, voice files, video outputs, and workflow tracking documents.

### Reading and Analyzing Files

Gemini can read and analyze existing code and documentation to understand how it works, identify issues, or describe architecture.

  * **Plan Mode:** When performing complex analysis or planning, Gemini will enter "Plan Mode" (a read-only state) to safely explore the codebase without accidental modifications. You will be prompted to exit Plan Mode before any file modifications occur.
  * **Contextual Reading:** Gemini will leverage its ability to read relevant project files (e.g., `config.json`, `requirements.txt`, `parser.py`, `voice_gen.py`, feature specs in `docs/specifications/`) to provide informed suggestions.
  * **Feature Spec Integration:** When working on component tasks, Gemini can read the corresponding feature specification to understand requirements and constraints.

### Error Handling in File Operations

If an error occurs during file operations (e.g., permissions, invalid paths), Gemini will analyze the error and suggest fixes. It's designed for graceful degradation, aiming to produce partial results with clear error messages whenever possible.

## 4\. Git Workflow Integration

While you handle the actual Git commands (add, commit, push) via GitHub Desktop, Gemini will provide the necessary information and messages to streamline your version control process.

### Commit Message Generation

Upon completing a task or a significant sub-task, Gemini will automatically compose a detailed Git commit message for you to use.

  * **Format:** Commit messages will follow a standardized format: `type: Short summary of the parent task - Detail of the first key change - Detail of the second key change - Related to Task #[TaskNumber]`.
  * **Validation Status:** For task completion commits, Gemini will include the validation status (e.g., `✅ All tests pass, ✅ Integration verified, ✅ PRD criteria met`).

### Git Operations Assistance

  * **Initial Setup:** The `/setup-project` command configures your Git remotes, adding a `template` remote for easy updates from the project template.
  * **Template Updates:** Gemini will remind you to pull the latest template updates using `git pull template main` to receive new AI rules, commands, and workflow improvements.
  * **Security:** Gemini emphasizes the critical importance of keeping your `.env` file (containing API keys) out of version control by ensuring it is listed in `.gitignore`.

## 5\. Validation & Quality Assurance

Gemini will guide you through progressive validation levels after each code modification or task completion:

  * **Level 1: Syntax & Style Validation:** Includes commands for code formatting (`black`), linting (`flake8`), and type checking (`mypy`).
  * **Level 2: Unit Test Validation:** Commands for running unit tests and checking test coverage.
  * **Level 3: Integration Validation:** Commands for integration tests, often using `episode_2_ex_final.md` as the primary test case.
  * **Level 4: Feature Completion Validation:** Running the full test suite and checking overall PRD success criteria.

## 6. Task Management Integration

### Notion Database Access Control
**CRITICAL**: Gemini CLI accesses the Notion database (`vmonster-dev-backlog`) ONLY when explicitly instructed by the user:
- **No Autonomous Access**: Gemini cannot independently read, create, or update Notion tasks
- **User-Directed Operations**: All Notion operations require explicit user instruction (e.g., "Update task VSM-15 to complete")
- **Task Type Scope**: Notion database reserved for non-core tasks (housekeeping, infrastructure, process improvements)
- **Core Components**: Components 1-8 are managed autonomously by Codex without Notion dependency

### Available Notion Commands (User-Directed Only)
- `@next-task` - Get next non-core task from Notion (when user requests)
- `@finalize-task` - Complete current non-core task in Notion (when user requests)
- `@update-prd` - Sync Notion completion status with PRD.md (when user requests)

## 7. Context Maintenance Protocol

To ensure the `.ai-context/AI_CONTEXT.md` file remains the single source of truth, Gemini will adhere to the following protocol:

### 1. Task Completion Trigger
- **Action:** After a task is successfully validated (passes all relevant validation levels), Gemini will automatically review the "Current Project Context State" in `.ai-context/AI_CONTEXT.md`.
- **Prompt:** Gemini will ask if the completed task warrants an update to the active/completed features, planned features, or lessons learned.
- **Example:** "Task `[Task Name]` is complete and validated. Should I update the `AI_CONTEXT.md` to reflect this?"

### 2. Architectural & Pattern Trigger
- **Action:** If a conversation leads to a new architectural decision, a reusable code pattern, or a convention to be followed.
- **Prompt:** Gemini will recognize this and ask if it should be documented in the "Architecture Decisions Made" or "Known Patterns & Conventions Discovered" sections of `.ai-context/AI_CONTEXT.md`.
- **Example:** "This seems like a new architectural decision. Shall I add it to `AI_CONTEXT.md`?"

### 3. Pre-Commit Check
- **Action:** When generating a commit message, Gemini will perform a final check.
- **Prompt:** Before finalizing the commit message, Gemini will ask one last time if any changes to the project's context, state, or architecture need to be recorded in `.ai-context/AI_CONTEXT.md`.
- **Example:** "Before I generate the commit message, does `AI_CONTEXT.md` need to be updated with any new context from the work we've just done?"

By following this protocol, Gemini will ensure that the project's master context file is always synchronized with the state of the codebase, providing a reliable foundation for all AI assistants.

## 7\. Key Reminders for Gemini CLI Usage

  * **Prioritize `.ai-context/AI_CONTEXT.md`:** Always refer to it for project standards and status.
  * **Use Validation Commands:** Run validation steps diligently after each change to ensure code quality and functionality.
  * **Follow Conventions:** Adhere to established coding and file naming conventions.
  * **Ask for Clarification:** If any instruction or context is unclear, ask for more details.
  * **Commit Frequently:** Use the provided commit messages and push changes regularly via GitHub Desktop.

By following these guidelines, Gemini CLI will be a powerful assistant in your development workflow, specifically enhancing your file operations and Git version control practices.
