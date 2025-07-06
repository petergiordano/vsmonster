# AI-Assisted Development Workflow Reference

## **Quick Reference for Chat Assistant - Strategist**

### **The 5-Step Workflow Overview**

```
Step 1: Generate Project Context Documents
├─ User → Chat AI: "Help me initialize a new project"
├─ Chat AI → User: Initialization prompt for CLI AI
├─ User → CLI AI: Execute initialization interview
└─ Outcome: 5 populated documents + AI_CONTEXT.md

Step 2: Brief AI Assistants with Dynamic Context
├─ User → Chat AI: [Paste AI_CONTEXT.md]
├─ Chat AI: Validate context understanding
└─ Ready for feature development

Step 3: Create Product Requirements Document (PRD)
├─ User → Chat AI: "I need to build [feature]"
├─ Chat AI: Strategic analysis + CLI AI prompt
├─ User → CLI AI: Execute PRD creation
└─ Outcome: Comprehensive PRD in tasks/

Step 4: Generate Task List
├─ User → Chat AI: "Prepare task generation prompt"
├─ Chat AI: PRD analysis + CLI AI prompt
├─ User → CLI AI: Execute task generation
└─ Outcome: Detailed task list with validation

Step 5: Execute Task List
├─ User → CLI AI: Execute tasks with validation loops
├─ CLI AI: Progressive implementation with quality gates
└─ Outcome: Working feature + updated context
```

---

## **Context Engineering Patterns**

### **Context Loading Pattern**
```
User Action: Paste AI_CONTEXT.md content
Your Response: "Context loaded. Project: [NAME], Current stage: [STAGE]..."
Validation: Confirm understanding of project state
```

### **Strategic Analysis Pattern**
```
1. Analyze user requirements
2. Review current project context
3. Identify architectural implications
4. Plan integration points
5. Prepare comprehensive CLI AI prompt
```

### **CLI AI Prompt Structure**
```
=== PROMPT FOR CLI AI ===

[Project Context from AI_CONTEXT.md]

[User Requirements & Strategic Analysis]

[Architectural Guidance & Pattern References]

[Reference to specific .ai-rules/ file for structure]

[Success Criteria & Validation Framework]

=== END PROMPT ===
```

---

## **Key Template Files Reference**

### **AI Rules Directory Structure**
```
.ai-rules/
├── 00_project-initialization.md     # AI-driven project setup
├── 01_create-prd.md                # PRD creation process
├── 02_generate-tasks.md            # Task breakdown process
├── 03_execute-tasks.md             # Task execution with validation
├── 04_plan-mode-best-practices.md  # Claude Code Plan Mode guide
├── 05_generate-prd-command.md      # Enhanced PRD generation
├── 06_generate-tasks-command.md    # Enhanced task generation
├── 07_context-validation-checkpoints.md # Context validation
└── 08_validation-loops.md          # Progressive validation system
```

### **Project Documents Structure**
```
.project-docs/
├── Roadmap.md                      # Project vision and strategy
├── ComponentLibrary.md            # Design system and UI patterns
├── VibeTesting.md                  # User experience design
└── SLC_Session_Notes.md           # Sprint planning (Simple, Lovable, Complete)
```

### **Dynamic Context Structure**
```
AI_CONTEXT.md (evolves throughout development)
├── Project Overview & Goals
├── Tech Stack & Architecture
├── Coding Conventions & Style
├── Context Handoff Protocols
├── Current Project Context State
│   ├── Active Features
│   ├── Completed Features
│   ├── Architecture Decisions Made
│   └── Known Patterns & Conventions
├── Plan Mode Best Practices
├── Validation & Quality Gates
└── Context Evolution Log
```

---

## **Success Indicators**

### **Context Transfer Success**
- ✅ CLI AI demonstrates understanding of project context
- ✅ CLI AI references existing patterns and architecture
- ✅ CLI AI follows established validation approaches
- ✅ Implementation aligns with project conventions

### **Strategic Collaboration Success**
- ✅ User requirements transformed into actionable CLI AI prompts
- ✅ Architectural implications identified and addressed
- ✅ Integration points planned and documented
- ✅ Quality gates built into implementation strategy

### **Workflow Efficiency Success**
- ✅ Minimal back-and-forth between strategic and tactical phases
- ✅ Context accumulates systematically across features
- ✅ Each workflow step builds on previous context
- ✅ CLI AI execution requires minimal strategic intervention

---

## **Common Strategic Scenarios**

### **New Project Initialization**
```
User: "Help me initialize a new project using the template."
Action: Prepare initialization prompt referencing .ai-rules/00_project-initialization.md
Focus: Ensure comprehensive context foundation
```

### **Feature Requirements Analysis**
```
User: "I need to build [feature]. Help me think through the requirements."
Action: Strategic analysis + PRD preparation prompt
Focus: Architectural integration and comprehensive context transfer
```

### **Task Planning Strategy**
```
User: "Here is the PRD. Prepare the prompt to turn this into a task list."
Action: PRD analysis + task generation prompt
Focus: Implementation strategy and validation framework
```

### **Context Update Facilitation**
```
User: "The CLI AI completed the feature. How should we update our context?"
Action: Guide AI_CONTEXT.md updates with lessons learned
Focus: Context accumulation and pattern recognition
```

---

## **Template Evolution Awareness**

### **Current Template State**
- ✅ Context Engineering Framework Complete
- ✅ 5-Step Workflow with Validation Loops
- ✅ Progressive Quality Gates
- ✅ Dynamic Context Accumulation
- ✅ Plan Mode Integration

### **Strategic Role Evolution**
- **Enhanced Context Engineering:** Advanced prompt preparation techniques
- **Architectural Intelligence:** Deep understanding of project patterns
- **Quality Assurance Integration:** Built-in validation and quality gates
- **Symbiotic Optimization:** Perfect collaboration with CLI AI implementers

### **Future Enhancement Areas**
- **Pattern Library Integration:** Reference successful implementation patterns
- **Automated Context Updates:** Streamlined context evolution processes
- **Quality Metric Integration:** Success measurement and optimization
- **Multi-Project Context:** Managing context across multiple projects
