# dev-cycle.md - AI-Powered Product Development Workflow

**Note:** This document describes the high-level component development cycle. For detailed implementation guidance, AI coordination, and task management, see [WORKFLOW_GUIDE.md](../../.ai-context/WORKFLOW_GUIDE.md).

---
## 🧠 Step 1: Use the PRD as the Source of Truth
- The `docs/specifications/PRD.md` file is the master vision and roadmap for the product.
- It defines the big picture.
- This is the only document where full product context is maintained.

## 🔍 Step 2: Identify the Next Component to Build
- Open `docs/specifications/PRD.md` and review the next prioritized component.
- Use its context to guide your detailed planning.

## 🧾 Step 3: Generate a Detailed Feature Spec
- In Claude Chat Dekstop (not claude code), paste in the PRD component context.
- Prompt it to generate a detailed feature spec using this structure:
  - **Filename:** `feat_spec-[component-name].md`
  - **Location:** `docs/specifications/`
  - **Contents should include:**
    - Purpose
    - Scope and boundaries
    - User flows
    - Edge cases
    - Logic requirements
    - UX/tech constraints
    - Test plan

## 🧠 Step 4: Codex Implements Core Product Components
- Go to chatgpt.com/codex.
- Begin a session and tell Codex to read the feature spec the AI Assistant ChatBot just created.
  - Example: `"Use docs/specifications/feat_spec-[component-name].md as input. Begin implementation."`
- Codex will:
  - Internally break down the feature spec into granular tasks.
  - Create a new branch for the implementation.
  - Implement the code and tests for the component.
  - Create a pull request (PR) upon completion.
  - Generate a detailed log of the tasks it created and completed for archiving (see Step 6.1).

## 🧪 Step 5: Review + Merge
- Help the user switch to the branch Codex created. 
- Open the PR in GitHub or VS Code. 
- Review code, verify test coverage, and request edits if needed.
- Merge once the user satisfied.

## 🔄 Step 6: Loop Back to the PRD
- Mark the component as completed in `docs/specifications/PRD.md`.
- Update any roadmap insights, follow-ups, or notes.
- Return to Step 2 and select the next component.

## 🧰 Step 6.1: Archive Codex Task Logs
- Codex will generate a detailed log of the tasks it created and completed for each component.
- These logs should be archived in `archive/codex_task_logs/feat_spec-[component-name]-tasks.md` for historical reference and auditing.

## 🧰 Step 6.2: Two-Tier Task Management
### Core Component Tasks (Codex-Managed)
- **Scope**: Components 1-8 of the main pipeline (Script Parser → Batch Processing)
- **Management**: Codex operates with full autonomy - creates, executes, and tracks tasks independently
- **Tracking**: Detailed logs in `archive/codex_task_logs/feat_spec-[component-name]-tasks.md`
- **No External Dependencies**: Codex does NOT access Notion database for core component work

### Non-Core Tasks (Notion-Managed)
- **Scope**: Housekeeping, architectural, infrastructure, process, research, and maintenance tasks
- **Database**: `vmonster-dev-backlog` - accessed ONLY when user explicitly directs
- **AI Access Control**: Claude Code and Gemini CLI access Notion only with explicit user instruction
- **Examples**: Documentation updates, dependency management, refactoring, CI/CD, security audits

### Task Type Decision Matrix
- **New Feature Implementation** → Codex (autonomous)
- **Bug Fixes in Core Components** → Codex (autonomous)
- **Documentation Updates** → Notion (user-directed)
- **Infrastructure Changes** → Notion (user-directed)
- **Process Improvements** → Notion (user-directed)
