# GEMINI.md

This file provides specific guidance for using **Gemini CLI** within your Visual Studio Code environment for the `versusMonster AVPS` project. It outlines how Gemini CLI integrates into the established development workflow, with a particular emphasis on assisting with file operations and Git version control.

## 1\. Project Context & Master Rulebook

**Your primary source of project context is the dynamic `AI_CONTEXT.md` file.** Gemini CLI automatically loads this file into its hierarchical memory system upon startup. This ensures Gemini is always up-to-date with the project's goals, tech stack, coding conventions, current development status, and architectural decisions.

  * **Master Context File:** [AI\_CONTEXT.md](https://www.google.com/search?q=uploaded:petergiordano/vsmonster/vsmonster-a3752057e465e1dba5bb2129e827a8e3fb7613bd/.ai-context/AI_CONTEXT.md)

### Gemini CLI Context Validation

Before starting any work, you can verify that Gemini has loaded the correct context:

  * **Show loaded context:** `/memory show`
  * **Ask for project understanding:** "What do you understand about this project?"

## 2\. Gemini CLI Workflow Integration

Gemini CLI is your **Implementer AI**, responsible for executing specific technical tasks provided by you (the Project Director) or prepared by a Chat AI (the Strategist). It works within the established 5-step AI-assisted development workflow.

### Context Loading and Management

  * **Automatic Loading:** Gemini automatically loads `GEMINI.md` (and by reference, `AI_CONTEXT.md`) on startup, ensuring immediate project awareness.
  * **Context Refresh:** If `AI_CONTEXT.md` or other context files are updated, restart Gemini CLI or use `/memory refresh` to load the latest information.
  * **Context Handoff Protocol:** When receiving prompts from a Chat AI, ensure they include relevant sections from `AI_CONTEXT.md` for complete understanding.

## 3\. File Operations Guidance

Gemini CLI has direct access to your project files and can assist with various file operations.

### Creating and Modifying Files

Gemini will provide the content or instructions for creating and modifying files based on the current task.

  * **File Paths:** When generating code or content, Gemini will specify the exact file paths (e.g., `src/parser.py`, `output/json/episode_007.json`).
  * **Directory Structure:** Gemini understands and adheres to the established project directory structure (e.g., `/scripts`, `/output/json`, `/src`).
  * **Output Files:** Gemini will guide the generation of various output files like JSON reports, voice files, and video outputs.

### Reading and Analyzing Files

Gemini can read and analyze existing code and documentation to understand how it works, identify issues, or describe architecture.

  * **Plan Mode:** When performing complex analysis or planning, Gemini will enter "Plan Mode" (a read-only state) to safely explore the codebase without accidental modifications. You will be prompted to exit Plan Mode before any file modifications occur.
  * **Contextual Reading:** Gemini will leverage its ability to read relevant project files (e.g., `config.json`, `requirements.txt`, `parser.py`, `voice_gen.py`) to provide informed suggestions.

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
  * **Level 3: Integration Validation:** Commands for integration tests, often using `episode_007.md` as the primary test case.
  * **Level 4: Feature Completion Validation:** Running the full test suite and checking overall PRD success criteria.

## 6\. Key Reminders for Gemini CLI Usage

  * **Prioritize `AI_CONTEXT.md`:** Always refer to it for project standards and status.
  * **Use Validation Commands:** Run validation steps diligently after each change to ensure code quality and functionality.
  * **Follow Conventions:** Adhere to established coding and file naming conventions.
  * **Ask for Clarification:** If any instruction or context is unclear, ask for more details.
  * **Commit Frequently:** Use the provided commit messages and push changes regularly via GitHub Desktop.

By following these guidelines, Gemini CLI will be a powerful assistant in your development workflow, specifically enhancing your file operations and Git version control practices.