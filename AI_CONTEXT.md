# AI Project Context & Master Rulebook (Dynamic)

### **Purpose: This document serves as the evolving master briefing for any AI assistant working on this project. It accumulates context across the 5-step workflow and must be provided at the beginning of any new development session.**

### CLI Context Files Integration
- **CLAUDE.md** and **GEMINI.md** automatically reference this file for complete project context
- **Claude Code** automatically loads CLAUDE.md on startup
- **Gemini CLI** automatically loads GEMINI.md into hierarchical memory
- Both CLI assistants get the same comprehensive context through this centralized approach

---

## 1. Project Overview & Goal

- **Project Name:** [Your Project Name]
- **Core Goal:** [A one-sentence summary of what this project does, taken from your Roadmap.md]
- **Target Vibe:** [e.g., "Intuitive and powerful," "Playful and simple," taken from your VibeTesting.md]
- **Current Workflow Stage:** [INITIALIZATION | PRD_CREATED | TASKS_GENERATED | IN_DEVELOPMENT | FEATURE_COMPLETE]

---

## 2. Tech Stack

- **Frontend:** [e.g., React, Next.js, Tailwind CSS]
- **Backend:** [e.g., Node.js, Express, FastAPI]
- **Database:** [e.g., Firestore, Supabase, PostgreSQL]
- **Key Libraries:** [e.g., Pydantic for validation, Auth.js for authentication]

---

## 3. File & Folder Structure

- **`/src`**: Contains all application source code.
- **`/src/components`**: Reusable UI components.
- **`/src/lib`**: Core logic, API clients, and utility functions.
- **`/tests`**: All Pytest/Jest tests, mirroring the `/src` structure.
- **`.project-docs/`**: Contains high-level planning documents (Roadmap, etc.). Do not write code here.
- **`.ai-rules/`**: Contains the specific, step-by-step instruction templates for the development workflow.
- **`/tasks`**: Contains PRDs and task lists for feature development.

---

## 4. Coding Conventions & Style

- **Language:** [e.g., Python 3.11, TypeScript]
- **Formatting:** All code must be formatted with [e.g., `black` for Python, `prettier` for JS/TS].
- **Naming:** Use `snake_case` for variables and functions, `PascalCase` for classes.
- **Docstrings:** All functions must have Google-style docstrings.
- **Error Handling:** All external API calls must be wrapped in a `try...except` block to handle potential errors gracefully.

---

## 5. Global AI Instructions

- **Always Create Tests:** Every new feature or function must be accompanied by a corresponding unit test in the `/tests` directory.
- **No New Dependencies:** Do not add any new libraries or packages without explicit permission.
- **Follow Existing Patterns:** Before writing new code, review the existing files in `/src` to understand and replicate the established patterns.
- **Ask Before Overwriting:** Never delete or significantly refactor existing code without asking for confirmation first.

---

## 6. Context Handoff Protocols

### **Between Chat AI (Strategist) and CLI AI (Implementer)**
- **Context Transfer Method:** Always provide this complete AI_CONTEXT.md file
- **Role Boundaries:** Chat AI plans and prepares prompts; CLI AI executes specific technical tasks
- **Validation Points:** CLI AI should confirm understanding of context before beginning implementation

### **Workflow Context Accumulation**
- **Step 1-2:** Foundation context (project setup, goals, constraints)
- **Step 3:** Feature context (PRD requirements, user stories, acceptance criteria)
- **Step 4:** Implementation context (task breakdown, file structure, dependencies)
- **Step 5:** Execution context (code patterns, validation results, lessons learned)

---

## 7. Current Project Context State

### **Active Features** (Features currently in development)
[This section gets updated as features move through the workflow]

**Feature: [Name]**
- **Status:** [PRD_CREATED | TASKS_GENERATED | IN_DEVELOPMENT | TESTING | COMPLETE]
- **PRD Location:** `tasks/prd-[feature-name].md`
- **Task List:** `tasks/tasks-[feature-name].md`
- **Key Context:** [Important decisions, constraints, or patterns discovered]
- **Integration Points:** [How this feature connects with existing code]
- **Validation Status:** [Current test/validation state]

### **Completed Features** (Reference for patterns and integration)
[This section accumulates successful implementations as references]

### **Architecture Decisions Made**
[This section accumulates important architectural choices made during development]
- **Decision:** [What was decided]
- **Rationale:** [Why it was decided]
- **Impact:** [How it affects future development]
- **Date:** [When decided]

### **Known Patterns & Conventions Discovered**
[This section grows as patterns are identified during development]
- **Pattern:** [Description of the pattern]
- **Location:** [Where it's implemented]
- **Usage:** [When to use this pattern]

---

## 8. Plan Mode Best Practices (Project-Specific)

### **When to ALWAYS Use Plan Mode**
- **Project Initialization:** Understanding existing project structure
- **Feature Integration:** Planning how new features fit with existing architecture  
- **Complex Debugging:** Understanding root causes before attempting fixes
- **Architectural Changes:** Any modifications to core patterns or structure

### **Project-Specific Plan Mode Guidance**
- **Tech Stack Considerations:** [Specific considerations for your tech stack]
- **Architecture Patterns:** [Key architectural patterns to understand in Plan Mode]
- **Integration Requirements:** [Critical integration points to analyze in Plan Mode]
- **Testing Patterns:** [Testing approaches to understand before implementation]

### **Context Validation Checkpoints in Plan Mode**
- [ ] Understand current project state and active features
- [ ] Review architectural decisions that might impact new work
- [ ] Identify existing patterns that should be followed
- [ ] Confirm integration requirements with active features
- [ ] Validate test coverage approach aligns with project standards

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
# Add your project-specific validation commands here
# Example:
# npm run lint
# npm test
# npm run type-check
```

---

## 10. Context Evolution Log

### **Context Updates** (Track how context evolves during development)
- **Date:** [Date]
- **Stage:** [Which workflow step]
- **Context Added:** [What new context was discovered/added]
- **Reason:** [Why this context is important for future development]

### **Lessons Learned** (Accumulate insights across features)
- **Lesson:** [What was learned]
- **Context:** [Situation where it was learned]
- **Application:** [How to apply this lesson in future development]

---

## 11. CLI Assistant Integration & Commands

### **CLI Assistant Context Loading**
- **Claude Code:** Automatically loads `CLAUDE.md` which references this file
- **Gemini CLI:** Automatically loads `GEMINI.md` into hierarchical memory
- **Both assistants:** Get complete project context through centralized AI_CONTEXT.md

### **Project-Specific Validation Commands**
```bash
# Level 1 (Syntax & Style):
# [your formatting command]     # e.g., black . or npm run prettier
# [your linting command]        # e.g., flake8 . or npm run lint  
# [your type checking command]  # e.g., mypy . or npm run type-check

# Level 2 (Unit Tests):
# [your test command]           # e.g., pytest tests/ or npm test
# [your coverage command]       # e.g., pytest --cov=module

# Level 3 (Integration):
# [your integration command]    # e.g., npm run test:integration

# Level 4 (Full Validation):
# [your full test suite]       # e.g., pytest tests/ -v or npm run test:all
```

### **CLI Assistant Best Practices**
- **Always read this complete AI_CONTEXT.md file first**
- **Use validation commands after each change**
- **Follow established patterns in existing codebase**
- **Ask for clarification if context is unclear**
- **Claude Code:** Use Plan Mode (Shift+Tab twice) for complex analysis
- **Gemini CLI:** Use `/memory show` to verify loaded context

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