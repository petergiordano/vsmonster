# VSMonster AVPS Development Workflow

This document outlines the stable and reliable development workflow for the versusMonster AVPS (Automated Video Podcast System) project. It is intended to be a persistent guide that does not change frequently.

**Note:** This document focuses on implementation details and AI coordination. For the high-level component development cycle (PRD → Feature Spec → Implementation → PR), see [dev-cycle.md](../docs/specifications/dev-cycle.md).

---

## 🎯 Core Principles

This workflow is designed around a few core principles:

*   **Two-Tier Task Management:** Core product components are self-managed by Codex; non-core tasks use Notion database with user-directed access only.
*   **Component-Based Architecture:** The system is built as a series of independent, interoperable components.
*   **AI-Assisted Implementation:** AI assistants are leveraged for various tasks, from planning to implementation and testing.
*   **User-Controlled Database Access:** All Notion database operations require explicit user instruction - no autonomous access.
*   **Continuous Validation:** A multi-layered validation process ensures code quality and correctness.

---

## 🤖 AI Assistants

This project utilizes a multi-agent AI team. Each agent has a specific role and set of capabilities. For detailed information on each AI, please refer to their respective documentation:

*   **[Claude](CLAUDE.md):** The primary AI assistant for high-level planning, architecture, and complex problem-solving.
*   **[Gemini CLI](GEMINI.md):** A command-line interface AI for executing specific, well-defined tasks and interacting with the local filesystem.
*   **[CODEX](AGENTS.md):** An AI agent specializing in code generation, refactoring, and implementation.

---

## 📊 High-Level Development Cycle

For major component development, the project follows a structured cycle:

1. **PRD Review** → Identify next component from `docs/specifications/PRD.md`
2. **Feature Spec Generation** → Create detailed specification in Claude Chat
3. **Implementation** → Codex reads spec and implements with tests
4. **Review & Merge** → Code review and integration
5. **PRD Update** → Mark component complete and loop back

See [dev-cycle.md](../docs/specifications/dev-cycle.md) for the complete high-level workflow.

---

## 🔄 Development Process

The development process follows a consistent, repeatable cycle:

### 1. Task Selection

#### Core Product Components (Codex-Managed)
*   **Components 1-8:** Tasks self-generated and managed by Codex during implementation
*   **Task Source:** Feature specifications in `docs/specifications/feat_spec-[component-name].md`
*   **Task Tracking:** Detailed logs in `archive/codex_task_logs/feat_spec-[component-name]-tasks.md`

#### Non-Core Tasks (Notion-Managed)
*   **Scope:** Housekeeping, architectural, infrastructure, process, research, and maintenance tasks
*   **Database:** [vmonster-dev-backlog](https://www.notion.so/22f859c6e596800786c6c1df9f865855)
*   **Access Control:** Claude Code accesses only when explicitly instructed by user
*   **Selection:** Based on user priority and project needs

#### Task Type Examples

**Codex-Managed Tasks (Core Components):**
- Script parsing implementation
- Voice generation with ElevenLabs
- Audio assembly and mixing
- Video generation and processing
- Component integration and testing

**Notion-Managed Tasks (Non-Core):**
- Update documentation files
- Refactor shared utilities
- Add new development tools
- Update CI/CD configuration
- Performance optimization analysis
- Security audit implementation
- Dependency updates and maintenance

### 2. Task Review and Refinement (For Codex-Managed Components)

For core component development using Codex:
*   **Pre-Implementation Review**: Before starting Codex tasks, systematically review all suggested tasks
*   **Critical Validation**: Check file references, configuration paths, and codebase alignment
*   **Technical Enhancement**: Add implementation details and specific technical approaches to task descriptions
*   **Claude Code Collaboration**: Use Claude Code to identify potential issues and suggest task improvements
*   **Edit Before Execute**: Modify task descriptions in Codex interface before beginning implementation

### 3. Implementation

*   The selected AI assistant is used to implement the task according to the plan.
*   The implementation should adhere to the project's coding standards and conventions.
*   Existing validation commands should be used throughout the implementation process.

### 3. Task Completion

*   Once the implementation is complete, it is thoroughly tested.
*   A commit message is generated, referencing the completed task.
*   The task is marked as "Done" in the Notion database.
*   The `docs/specifications/PRD.md` is automatically updated to reflect the new component progress using the `@update-prd` command.

---

## 📋 Component-Based Development

The project is broken down into an 8-component pipeline. The current status of each component is tracked in the `docs/specifications/PRD.md`.

---

## 📝 PRD Source of Truth

The `docs/specifications/PRD.md` file is the definitive source of truth for the project's requirements, success criteria, and component status. It is automatically updated as tasks are completed.

---

## 🎯 Success Metrics

Each component has a set of success criteria that must be met, including:

1.  **Command Execution:** The component can be executed with a single command.
2.  **Validation:** The component passes all tests with the reference test case.
3.  **Performance:** The component meets its performance targets.
4.  **Cost:** The component operates within its budget.

---

## 🚀 Getting Started

To begin a new development session:

1.  Familiarize yourself with the current project status by reviewing the `docs/specifications/PRD.md`.
2.  Consult the AI assistant guides ([CLAUDE.md](CLAUDE.md), [GEMINI.md](GEMINI.md), [AGENTS.md](AGENTS.md)) for specific instructions on how to interact with them.
3.  Select the next task from the [Notion backlog](https://www.notion.so/22f859c6e596800786c6c1df9f865855).
4.  Follow the development process to implement and complete the task.

## 🛠️ Available Commands

Key commands for managing the development workflow:

*   **`@next-task`** - Get the next available task and create implementation plan
*   **`@finalize-task`** - Complete current task and update Notion
*   **`@update-prd`** - Sync Notion task completion status with PRD.md component progress
*   **`@orient`** - Get oriented in the project and see next best actions