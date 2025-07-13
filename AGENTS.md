Here is the `AGENTS.md` file designed for OpenAI CODEX-1, integrating it into your existing `versusMonster AVPS` development workflow, with a specific focus on file operations and Git interactions, and incorporating best practices for AI agent documentation.

# AGENTS.md

This file provides specific guidance for using **OpenAI CODEX-1** as an **Implementer AI** within your `versusMonster AVPS` project. It outlines how CODEX-1 integrates into the established development workflow, with a particular emphasis on assisting with file operations and Git version control. Think of this as your detailed instruction manual for CODEX-1 in this project.

## 1\. Project Context & Master Rulebook

Your primary source of project context is the dynamic `AI_CONTEXT.md` file. CODEX-1, like other AI agents in this workflow, should refer to `AI_CONTEXT.md` to understand the project's goals, tech stack, coding conventions, current development status, and architectural decisions.

  * **Master Context File:** [AI\_CONTEXT.md](https://www.google.com/search?q=uploaded:petergiordano/vsmonster/vsmonster-a3752057e465e1dba5bb2129e827a8e3fb7613bd/.ai-context/AI_CONTEXT.md)

## 2\. CODEX-1 Identity & Role

CODEX-1 is designed as an **Implementer AI** within the `versusMonster AVPS` 3-party collaboration model. Your role is primarily **technical execution** and **tactical implementation** based on specific prompts. You are expected to:

  * Implement new features, functions, and modules.
  * Write and fix code.
  * Generate and run tests.
  * Refactor code.
  * Assist with common development tools like Git.
  * Follow explicit instructions and project guidelines to ensure generated code is idiomatic, maintainable, and aligned with project standards.

## 3\. Workflow Integration

CODEX-1 operates within the `versusMonster AVPS` 5-step AI-assisted development workflow. Your main role is in **Step 5: Execute Task List**, but you will also interact with outputs from earlier steps and prepare outputs for later steps.

### Context Loading and Management

While a direct context loading mechanism like `/memory show` (used by Gemini CLI) may not be available, your initial prompt should always include the full content of `AI_CONTEXT.md`. This ensures you have the necessary accumulated project knowledge.

  * **Context Updates:** If the project context evolves (`AI_CONTEXT.md` is updated), ensure you are provided with the latest version in subsequent prompts or sessions.
  * **Context Preservation:** Strive to remember previous interactions and context for continuity in multi-turn conversations.

## 4\. File Operations Guidance

CODEX-1 is expected to understand and assist with various file operations within the project.

### Reading and Analyzing Files

Before any modifications, thoroughly read and analyze relevant project files. This includes:

  * **Project Context:** `AI_CONTEXT.md` for global guidelines, `CLAUDE.md`, `GEMINI.md` for AI-specific instructions.
  * **Workflow Definitions:** Files within `.ai-rules/` for process steps (e.g., `03_execute-tasks.md`).
  * **Planning Documents:** `.project-docs/` (e.g., `Roadmap.md`, `PRD.md`) for understanding feature requirements and architectural decisions.
  * **Source Code:** `src/` directory to understand existing patterns, functions, and classes.
  * **Test Files:** `tests/` directory to understand testing methodology and existing tests.

### Creating and Modifying Files

When generating code or content, adhere strictly to the project's defined file paths and structure:

  * **Source Code:** `src/` (e.g., `parser.py`, `voice_gen.py`).
  * **Output Directories:** Generate content into the appropriate subdirectories within `/output/` (e.g., `/output/json`, `/output/voices`).
  * **Task/PRD Files:** Generate planning documents within the `tasks/` directory.
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

## 6\. Coding Conventions & Style

Adhere to the project's established coding conventions and style guidelines, as detailed in `AI_CONTEXT.md`. This includes:

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
  * **Level 3: Integration Tests:** Guide user to run `python src/parser.py scripts/episode_007.md` and `python setup_validation.py` for integration testing with the `Episode 7` reference.
  * **Level 4: Feature Completion:** Guide user to run the full test suite and confirm all PRD success criteria are met.
  * **Error Correction:** If validation fails, analyze the error output, identify the root cause, and provide targeted fixes for the user.

## 8\. Key Reminders for CODEX-1 Usage

  * **Episode 7 First:** Always prioritize and validate new features against the `Episode 7` reference implementation.
  * **Simple, Lovable, Complete (SLC):** Focus on building simple, delightful, and complete features.
  * **Command-Line Focus:** Maintain CLI interfaces with clear ASCII progress indicators and status messages.
  * **Cost Awareness:** Be mindful of API usage and associated costs during code generation (e.g., ElevenLabs characters, image prompts).
  * **Documentation as Code:** Understand that project documentation (`README.md`, `AI_CONTEXT.md`, `CONTRIBUTING.md`) serves as your instruction set.