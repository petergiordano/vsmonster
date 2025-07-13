# AI-Assisted Development: The Complete Workflow Guide

### **Purpose: A detailed guide for using this template with the 3-party collaboration model.**

This document explains the guiding philosophies, the roles of each participant, and the step-by-step instructions for building features with this template.

---

## 🏗️ Workspace Setup & Prerequisites

### **Before You Begin: Verify Your Workspace**

**Important:** Ensure you're working in your project workspace, not the template repository.

#### **✅ Workspace Checklist:**
```bash
# You should be in your project directory:
pwd  # Should show: /path/to/your-project-name (NOT ai-new-project-template)

# Verify essential files exist:
ls -la
# Should see:
# - .ai-rules/           (copied from template)
# - .project-docs/       (copied from template) 
# - src/                 (your source code directory)
# - AI_CONTEXT.md        (template - will be populated)
# - CLAUDE.md            (Claude Code CLI context file)
# - GEMINI.md            (Gemini CLI context file)
# - WORKFLOW_GUIDE.md    (this file)
# - README.md            (customize for your project)
```

#### **🔧 Prerequisites:**
- **VS Code** with terminal access
- **Git** for version control
- **AI Assistant Access:**
  - **Chat AI:** ChatGPT, Gemini, Claude (web interface) - for strategy and planning
  - **CLI AI:** Claude Code CLI, Gemini CLI, or similar - for implementation
- **Your project workspace** properly set up from the template

### **First-Time Setup: Initialize Your Project**

If you haven't completed workspace setup yet:

1. **Return to README.md** and complete "Quick Start" steps 1-2
2. **Verify all template files** are copied to your workspace root
3. **Customize your README.md** for your specific project
4. **Come back here** to begin the development workflow

---

## Using Plan Mode Effectively

*This section applies when using Claude Code CLI and leverages its built-in Plan Mode feature.*

### **What is Plan Mode?**

Plan Mode is Claude Code's read-only analysis mode that prevents accidental file modifications while allowing comprehensive codebase exploration and planning. Access it by pressing Shift+Tab twice, and it creates a safe environment where Claude can research, analyze, and plan without making any changes to your files.

### **Plan Mode Benefits for This Workflow**

- **Safe Exploration:** Analyze existing code without risk of accidental changes
- **Better Planning:** Ask Claude to make a plan before coding and explicitly tell it not to code until you've confirmed its plan looks good
- **Architectural Alignment:** Understand existing patterns before implementing new features
- **Reduced Iterations:** More thoughtful analysis leads to better initial implementations

### **Plan Mode Integration Points**

**Step 1 - Project Initialization:**
- Use Plan Mode to safely explore any existing project structure
- Analyze current dependencies and configuration files
- Better informed questions based on discovered project context

**Step 3 - PRD Creation:**
- Enter Plan Mode to understand how the new feature fits into existing architecture
- Research similar implementations in the codebase
- Plan integration points before defining requirements

**Step 4 - Task Generation:**
- Use Plan Mode to thoroughly analyze the PRD and existing codebase
- Understand dependencies and architectural constraints
- Create more accurate task breakdowns

**Step 5 - Task Execution:**
- Enter Plan Mode before complex parent tasks
- Use for debugging when implementations don't work as expected
- Plan integration strategies for multi-file changes

### **Plan Mode Best Practices**

1. **Always Plan First:** Use Plan Mode for initial analysis - the 2 minutes spent planning saves 20 minutes of refactoring later
2. **Use Thinking Modes:** Use "think", "think hard", "think harder", or "ultrathink" to trigger extended thinking mode for better analysis
3. **Exit to Execute:** Remember to exit Plan Mode (Shift+Tab) before actual implementation
4. **Strategic Usage:** Use Plan Mode for complex tasks, skip for simple repetitive patterns

---

## 🔧 CLI Assistant Context Integration

*This section explains how Claude Code and Gemini CLI automatically receive project context.*

### **Automatic Context Loading**

**Your workspace includes context files that automatically brief CLI assistants:**

- **`CLAUDE.md`**: Claude Code automatically loads this file on startup
- **`GEMINI.md`**: Gemini CLI automatically loads this into hierarchical memory
- **Both files reference `AI_CONTEXT.md`** for complete project context

### **How It Works**

**When you start Claude Code CLI:**
```bash
claude  # Automatically loads CLAUDE.md → AI_CONTEXT.md context
```

**When you start Gemini CLI:**
```bash
gemini  # Automatically loads GEMINI.md into memory system
```

**Context Loading Verification:**
- **Claude Code**: Use Plan Mode to verify context understanding
- **Gemini CLI**: Use `/memory show` to view loaded context files

### **Benefits of This Approach**

✅ **Zero Setup Required**: CLI assistants get project context immediately  
✅ **Consistent Context**: All AI assistants work from the same project knowledge  
✅ **Automatic Updates**: Context evolves as your project grows  
✅ **Pattern Recognition**: CLI assistants understand your project conventions immediately  

### **Context Validation**

**Before starting work with CLI assistants:**

**Claude Code Validation:**
```
1. Start claude in your project directory
2. Enter Plan Mode (Shift+Tab twice)
3. Ask: "What do you understand about this project from the context?"
4. Verify it references AI_CONTEXT.md content correctly
5. Exit Plan Mode (Shift+Tab) when ready to implement
```

**Gemini CLI Validation:**
```
1. Start gemini in your project directory  
2. Run: /memory show
3. Verify GEMINI.md content is loaded
4. Ask: "What do you understand about this project?"
5. Confirm it references AI_CONTEXT.md content correctly
```

### **Troubleshooting Context Loading**

**Common Issues:**
- **"CLI doesn't seem to understand my project"** → Verify you're in the correct directory with CLAUDE.md/GEMINI.md files
- **"Context seems outdated"** → Update AI_CONTEXT.md, then restart CLI assistant
- **"CLI ignoring project patterns"** → Use context validation steps above to verify loading

**Context Update Protocol:**
1. **Update AI_CONTEXT.md** with new patterns or decisions
2. **Restart CLI assistant** to load updated context
3. **Verify loading** using validation steps above

---

## Guiding Philosophy

This template is built upon two key concepts that ensure high-quality, consistent results from AI assistants.

-   **Vibe Coding**: We use natural language to direct AI assistants, but provide them with highly structured context. This requires systematic thinking, rigorous version control, and detailed project documentation.
-   **SLC Framework**: Instead of a Minimum Viable Product (MVP), we build features that are **Simple** (does one thing well), **Lovable** (has a great user experience), and **Complete** (fully delivers on its promise).

---

## The 3-Party Collaboration Model

This workflow splits responsibilities between you and two types of AI assistants to maximize efficiency.

#### 1. The User (You) - The Project Director
You are the ultimate authority. You drive the process, make final decisions, and are responsible for testing and validation.

#### 2. The Chat Assistant (e.g., ChatGPT, Gemini, Claude) - The Strategist
This AI runs in a web browser. Its role is high-level thinking, planning, and preparing prompts. It does **not** write the final code.

#### 3. The CLI Assistant (e.g., Gemini CLI, Claude Code) - The Implementer
This AI runs in your VS Code terminal. It has access to your files and its only job is to execute the specific prompts you provide.

---

## The Development Workflow

### **Phase 1: Project Setup & Context**

Before starting any coding, it's crucial to establish the project's foundation.

#### **Step 1: Generate Project Context Documents**
Instead of manually filling out the planning documents, use the AI-assisted initialization process to create your project foundation.

**🎯 Outcome:** You'll have 5 fully populated planning documents plus a project-specific AI_CONTEXT.md

**📋 Process:**
1.  **You to Chat Assistant:** "Help me initialize a new project using the template."
2.  **Chat Assistant to You:** Provides the initialization prompt based on `.ai-rules/00_project-initialization.md`.
3.  **You to CLI Assistant:** Paste the initialization prompt into the terminal.
4.  **CLI Assistant:** **Enters Plan Mode (Shift+Tab twice)** to safely explore any existing project structure and dependencies
5.  **CLI Assistant to You:** Conducts a structured interview through five phases:
    -   **Phase A:** Project Vision & Strategy (→ `Roadmap.md`)
    -   **Phase B:** User Experience & Emotional Design (→ `VibeTesting.md`)
    -   **Phase C:** Design System & Visual Identity (→ `ComponentLibrary.md`)
    -   **Phase D:** First Sprint Planning (→ `SLC_Session_Notes.md`)
    -   **Phase E:** Technical Foundation & AI Context (→ `AI_CONTEXT.md`)
6.  **You:** Answer the questions thoughtfully - these become your project's foundation.
7.  **CLI Assistant:** **Exits Plan Mode** and generates all five populated documents with project-specific Plan Mode guidance.
8.  **You:** Save the generated documents in your project (`.project-docs/` for the first four, root directory for `AI_CONTEXT.md`).

**⚡ Alternative Option:** If you prefer to fill out the context documents manually, you can skip Step 1 and complete the templates yourself, but you'll need to manually create your project-specific `AI_CONTEXT.md`.

### **Phase 2: Feature Implementation**

For any new feature, follow this process. **Important:** Always begin new AI sessions by providing your project-specific `AI_CONTEXT.md` to the AI assistant.

#### **Step 2: Brief AI Assistants with Dynamic Context (Context Convergence)**

**🎯 Goal**: Ensure all AI assistants have current, accumulated project context for optimal collaboration.

**Enhanced Context Loading Process**:

1. **Context Validation Checkpoint:**
   - **Action:** Copy the entire contents of your **dynamic** `AI_CONTEXT.md` file and paste it as your first message to any AI assistant
   - **Validation:** AI assistant should respond: "Context loaded. Project: [NAME], Current stage: [STAGE], Active features: [LIST]. Ready to assist with [CURRENT_TASK]."
   - **Confirm:** Verify the AI's understanding matches your current project state

2. **Context Convergence Benefits:**
   - **Accumulated Knowledge:** AI_CONTEXT.md now contains lessons learned from previous features
   - **Architecture Awareness:** AI knows existing patterns and decisions made
   - **Integration Intelligence:** AI understands how new features fit with existing code
   - **Validation Continuity:** AI knows what validation approaches work for your project

3. **Role-Specific Context Loading:**
   
   **For Chat AI (Strategist):**
   ```
   "I've loaded the project context. I understand:
   - Project goals and current workflow stage
   - Existing architecture and patterns
   - Active features and their status
   - My role as strategist for planning and prompt preparation
   Ready to help with [current need: PRD creation, task planning, etc.]"
   ```
   
   **For CLI AI (Implementer):**
   ```
   "Context loaded via AI_CONTEXT.md. Current state:
   - Project: [name], Stage: [stage]
   - Tech stack: [details]
   - Active features: [list]
   - Role: CLI implementer for code execution
   Ready for specific implementation tasks."
   ```

4. **Context Handoff Protocol:**
   - **Between Sessions:** Always start with fresh AI_CONTEXT.md loading
   - **Between AI Types:** Chat AI prepares context-rich prompts for CLI AI
   - **Progress Updates:** Update AI_CONTEXT.md as features move through workflow stages

**✅ Critical Success Factors:**
- ✅ AI demonstrates understanding of current project state
- ✅ AI references existing patterns and architecture decisions
- ✅ AI knows which features are active and their current status
- ✅ AI follows established validation and testing approaches

#### **Step 3: Create the Product Requirements Document (PRD)**

**🎯 Goal**: To define the feature requirements clearly enough for a junior developer to understand.

**📋 Process**:
1.  **You to Chat Assistant:** "I need to build [feature]. Help me think through the requirements."
2.  **Chat Assistant to You:** Helps you brainstorm and prepares a detailed prompt for the CLI Assistant, using the rules from `.ai-rules/01_create-prd.md`.
3.  **You to CLI Assistant:** Paste the prepared prompt into the terminal. 
4.  **CLI Assistant:** **Enters Plan Mode** to understand how the feature fits into existing architecture and research similar implementations
5.  **CLI Assistant:** **Exits Plan Mode** and asks clarifying questions about the feature requirements
6.  **You:** Answer the questions. The CLI Assistant will then generate the final PRD.
7.  **You:** Save the PRD in a new `tasks/` directory (e.g., `tasks/prd-feature-name.md`).

**💡 Enhanced PRD Features:**
- **Executable Success Criteria:** Specific commands to validate feature completion
- **Context Integration:** References existing project patterns and architecture
- **Validation Commands:** Built-in testing and quality gates

#### **Step 4: Generate the Task List**

**🎯 Goal**: To break down the PRD into a detailed, step-by-step checklist with integrated validation.

**📋 Process**:
1.  **You to Chat Assistant:** "Here is the PRD we just created. Prepare the prompt to turn this into a task list."
2.  **Chat Assistant to You:** Provides a prompt containing the rules from `.ai-rules/02_generate-tasks.md` and the PRD content.
3.  **You to CLI Assistant:** Paste the prepared prompt into the terminal.
4.  **CLI Assistant:** **Enters Plan Mode** to thoroughly analyze the PRD and examine existing codebase patterns
5.  **CLI Assistant:** **Exits Plan Mode** and generates a hierarchical task list based on the analysis
6.  **You:** Review the task list and save it (e.g., `tasks/tasks-feature-name.md`).

**✨ Enhanced Task Generation:**
- **Progressive Validation Steps:** Each task includes validation checkpoints
- **Dependency Mapping:** Tasks ordered based on architectural dependencies
- **Error Prevention:** Common pitfall identification and mitigation

#### **Step 5: Execute the Task List**

**🎯 Goal**: To implement the feature by completing one sub-task at a time, with systematic validation at each step.

**📋 Process**:
1.  **You to CLI Assistant:** Paste the rules from `.ai-rules/03_execute-tasks.md` into the terminal, followed by the content of your task list file.
2.  **CLI Assistant:** **Uses Plan Mode strategically** - enters Plan Mode for complex parent tasks to analyze context and plan implementation approach
3.  **CLI Assistant to You:** Provides the code for the **first sub-task** and then **PAUSES**.
4.  **You:** Implement and test the AI's suggestion in VS Code.
5.  **You:** If the code works, mark the task as complete (`[x]`) in your task file.
6.  **You to CLI Assistant:** Type **"Go"** to proceed to the next sub-task.
7.  **Loop:** Repeat steps 2-6 until all tasks are complete. The CLI Assistant will use Plan Mode again for complex tasks, debugging, or when issues arise.

**🔄 Enhanced Task Execution:**
- **4-Level Progressive Validation:** Syntax → Tests → Integration → Feature validation
- **Error Correction Loops:** Systematic approach to fixing issues
- **Context Accumulation:** Lessons learned feed back into AI_CONTEXT.md

---

## 🎯 Summary: Complete Enhanced Workflow

### **Phase 1: Foundation** 
1. **✅ Verify Workspace Setup** - Confirm you're in project workspace with all template files
2. **📝 Generate Project Context** - AI-driven interview creates all planning documents

### **Phase 2: Feature Development**
3. **🔄 Load Dynamic Context** - Brief AI with accumulated project knowledge
4. **📋 Create Enhanced PRD** - Feature requirements with validation criteria
5. **📝 Generate Validated Tasks** - Detailed implementation plan with quality gates
6. **⚡ Execute with Validation** - Progressive implementation with error correction

### **🚀 Getting Started Right Now**

**If this is your first time using the template:**
1. **✅ Complete workspace setup** (see top of this guide)
2. **📝 Run Step 1** to generate your project foundation
3. **⚡ Start building features** with Steps 2-5

**If you have an existing project with context:**
1. **🔄 Load your AI_CONTEXT.md** (Step 2)
2. **📋 Define your next feature** (Step 3)
3. **🛠️ Break it down and build** (Steps 4-5)

**If you're exploring the workflow:**
1. **📖 Read this entire guide** to understand the process
2. **🔍 Explore .ai-rules/ directory** to see AI instructions
3. **📝 Review .project-docs/ templates** to understand the planning approach
4. **🎯 Come back when ready** to start a real project

---

### **⚡ Quick Decision Tree**

**Question: What's your current situation?**

- **"I just set up my workspace and I'm ready to start a new project"**  
  → **Go to Step 1** (Generate Project Context Documents)

- **"I have an existing project and want to add a new feature"**  
  → **Go to Step 2** (Brief AI with Dynamic Context)

- **"I want to understand how this all works first"**  
  → **Keep reading** this guide completely, then return to Step 1

- **"I have an existing codebase and want to use this template"**  
  → **Move your code to src/**, manually populate AI_CONTEXT.md, then **go to Step 2**

This systematic approach ensures that both you and the AI have comprehensive context at every stage, leading to more consistent, higher-quality results with built-in quality assurance and error prevention.

---

## 🚀 Advanced Task Management with Claude Task Master (Optional)

*This section explains how to enhance Steps 4-5 with Claude Task Master MCP for sophisticated task management.*

### **What is Claude Task Master?**

Claude Task Master is an AI-powered task management system that integrates with our framework to provide advanced task execution capabilities:

- **PRD Parsing:** Automatically generate tasks from requirements documents
- **Complexity Analysis:** Identify which tasks need breakdown using AI research
- **Smart Dependencies:** Intelligent task sequencing and dependency management
- **Progress Tracking:** Systematic status management and next-task recommendations

### **Integration with Our Framework**

**Our Framework Provides:**
- Project setup and context engineering (Steps 1-3)
- AI collaboration patterns and validation systems
- Context accumulation and session bridging

**Task Master Enhances:**
- Task generation sophistication (Step 4)
- Task execution management (Step 5)
- Dependency tracking and complexity analysis

### **Enhanced Workflow Options**

**Standard Step 4:** Use our AI rule-based task generation  
**Enhanced Step 4:** Use Task Master's `parse_prd` for more sophisticated task breakdown

**Standard Step 5:** Manual task tracking with commit messages  
**Enhanced Step 5:** Use Task Master tools for dependency management and smart task selection

### **Key Task Master Tools for Our Workflow**

**For Enhanced Task Generation (Step 4):**
- `parse_prd` - Parse your PRD into structured tasks with dependencies
- `analyze_project_complexity` - Identify tasks needing further breakdown
- `expand_all` - Break down complex tasks into manageable subtasks

**For Enhanced Task Execution (Step 5):**
- `next_task` - Get dependency-aware task recommendations
- `get_task` - Understand task context and requirements
- `set_task_status` - Track progress systematically
- `update_task` - Modify tasks based on implementation learnings

### **Setup Claude Task Master**

**If you want to use these enhanced capabilities:**

1. **Install Task Master MCP** in your editor (Cursor, Claude Desktop, etc.)
2. **Configure API keys** for AI model access
3. **Initialize in your project:** Use `initialize_project` tool
4. **Choose enhanced options** in Steps 4-5 of our workflow

### **Workflow Decision Points**

**Step 4 Decision:**
- **Simple projects:** Use our standard AI rule-based approach
- **Complex projects:** Use Task Master `parse_prd` for sophisticated breakdown

**Step 5 Decision:**
- **Linear development:** Use our standard commit-based tracking
- **Complex dependencies:** Use Task Master tools for smart task management

**Both approaches maintain:**
- ✅ Context engineering from our framework
- ✅ Progressive validation loops
- ✅ Chat AI ↔ CLI AI collaboration patterns
- ✅ Human-in-the-loop control

---

## 🛠️ Advanced Features & Context Engineering

This workflow leverages advanced context engineering principles:

- **🔄 Dynamic Context Accumulation:** Your AI_CONTEXT.md evolves and improves with each feature
- **✅ Progressive Validation Loops:** 4-level validation system prevents error accumulation  
- **🎯 Context Convergence:** AI assistants maintain project awareness across sessions
- **⚡ Command-Driven Structure:** Structured transitions between workflow phases
- **🛡️ Plan Mode Integration:** Safe exploration and thoughtful planning before implementation

**Ready to build? Start with Step 1 if this is a new project, or Step 2 if you have existing context!**
