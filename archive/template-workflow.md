# Start Coding

Feature development orchestrator that guides you through the complete development workflow (Steps 1-5).

## Command Purpose

Intelligent workflow orchestrator that detects your project state and guides you through feature development from initial idea to implementation.

## Execution Process

### Phase 1: Project State Detection

Analyze current project state to determine starting point:

```bash
echo "🔍 Analyzing project state..."

# Check if project foundation exists
if [ ! -f "AI_CONTEXT.md" ]; then
    echo "❌ Error: Project not properly set up"
    echo "💡 Run /setup-project first to initialize your workspace"
    exit 1
fi

# Detect current development stage
if [ ! -d ".project-docs" ] || [ ! -f ".project-docs/Roadmap.md" ]; then
    PROJECT_STAGE="needs_foundation"
elif [ ! -d "tasks" ] || [ -z "$(ls -A tasks 2>/dev/null)" ]; then
    PROJECT_STAGE="needs_feature_prd"
elif [ -f "tasks/prd-*.md" ] && [ ! -f "tasks/tasks-*.md" ]; then
    PROJECT_STAGE="needs_task_list"
elif [ -f "tasks/tasks-*.md" ]; then
    PROJECT_STAGE="ready_to_implement"
else
    PROJECT_STAGE="unknown"
fi

echo "📊 Current stage: $PROJECT_STAGE"
```

### Phase 2: Workflow Orchestration

Based on detected stage, guide user through appropriate workflow steps:

#### **Stage: needs_foundation**
```markdown
🏗️ **Project Foundation Required**

Your project needs foundation documents before feature development.

I'll guide you through Step 1: Project Initialization to create:
- Roadmap.md (vision, goals, technical approach)
- VibeTesting.md (user experience design)
- ComponentLibrary.md (design system)
- SLC_Session_Notes.md (development planning)
- AI_CONTEXT.md (populated with project context)

This takes 10-15 minutes and creates the foundation for all future features.

Ready to begin? (This follows .ai-rules/00_project_initialization_rule.md)
```

Load and execute project initialization:
1. Read `.ai-rules/00_project_initialization_rule.md`
2. Conduct 5-phase structured interview
3. Generate all foundation documents
4. Populate `AI_CONTEXT.md` with project-specific context
5. After completion, guide to feature development

#### **Stage: needs_feature_prd**
```markdown
📋 **Feature Definition Required**

Your project foundation is complete! Now let's define your first feature.

I'll guide you through:
- Step 3: Create Enhanced PRD (Product Requirements Document)

What feature would you like to build? Describe your idea and I'll help you create a comprehensive PRD with validation criteria.

Examples:
- "User authentication system"
- "File upload with progress tracking"
- "Real-time chat functionality"
- "Dashboard with data visualization"

What's your feature idea?
```

Execute PRD creation:
1. Read `.ai-rules/01_create-prd.md` 
2. Conduct clarifying interview
3. Generate comprehensive PRD
4. Save to `tasks/prd-[feature-name].md`
5. Guide to task generation

#### **Stage: needs_task_list**
```markdown
⚡ **Task Breakdown Required**

Found your PRD! Now let's break it down into actionable tasks.

I'll guide you through:
- Step 4: Generate Validated Task List

I'll analyze your PRD and create a detailed, step-by-step implementation plan with validation checkpoints.
```

Execute task generation:
1. Read `.ai-rules/02_generate-tasks.md`
2. Analyze existing PRD file
3. Generate hierarchical task list with validation
4. Save to `tasks/tasks-[feature-name].md`
5. Guide to implementation

#### **Stage: ready_to_implement**
```markdown
🚀 **Ready for Implementation**

Your feature is fully planned! Time to build it.

I'll guide you through:
- Step 5: Execute Task List with Quality Gates

I'll work through your task list one sub-task at a time, with testing and validation at each step.
```

Execute implementation:
1. Read `.ai-rules/03_execute-tasks.md`
2. Load task list content
3. Begin systematic implementation
4. Handle validation and error correction
5. Track progress and completion

#### **Stage: unknown**
```markdown
🤔 **Project State Unclear**

I'm not sure where you are in the development process.

Let me analyze your project structure:
```

Show detailed project analysis and guide to appropriate step.

### Phase 3: Continuous Flow Management

Handle workflow transitions and user guidance:

```bash
# After each major step completion
case $COMPLETED_STEP in
    "foundation")
        echo "✅ Project foundation complete!"
        echo "🎯 Next: Run /start-coding again to define your first feature"
        ;;
    "prd")
        echo "✅ Feature PRD complete!"
        echo "🎯 Next: Run /start-coding again to generate task list"
        ;;
    "tasks")
        echo "✅ Task list complete!"
        echo "🎯 Next: Run /start-coding again to begin implementation"
        ;;
    "implementation")
        echo "✅ Feature implementation complete!"
        echo "🎯 Next: Test your feature, then run /start-coding for next feature"
        ;;
esac
```

## Smart Features

### **State Detection Logic**
- Analyzes existing files to determine workflow position
- Provides contextual guidance based on current state
- Handles partial completion gracefully

### **Workflow Continuity**
- Remembers where you left off
- Guides through natural progression: Foundation → PRD → Tasks → Implementation
- Allows jumping back to earlier steps if needed

### **Error Recovery**
- Detects incomplete states (e.g., PRD exists but no tasks)
- Offers to complete missing steps
- Provides clear next actions

### **Multi-Feature Support**
- Handles multiple PRDs and task lists
- Guides through feature-by-feature development
- Maintains project-wide context

## Usage Patterns

### **First Time User**
```
/setup-project    # One-time workspace setup
/start-coding     # Foundation → PRD → Tasks → Implementation
```

### **Returning User**
```
/start-coding     # Detects state, continues where left off
```

### **Multi-Feature Development**
```
/start-coding     # Feature 1: Foundation → PRD → Tasks → Implementation
/start-coding     # Feature 2: PRD → Tasks → Implementation (reuses foundation)
/start-coding     # Feature 3: PRD → Tasks → Implementation
```

### **Recovery Scenarios**
```
/start-coding     # "I have a PRD but need tasks" → generates tasks
/start-coding     # "I was mid-implementation" → continues task execution
/orient          # "I'm lost" → shows current state and options
```

## Integration with Other Commands

### **Command Relationships**
- **`/setup-project`** → **`/start-coding`** (natural progression)
- **`/start-coding`** ↔ **`/orient`** (navigation and state checking)
- **`/start-coding`** → **`/start-coding`** (multi-feature development)

### **Workflow Handoffs**
- Seamless transitions between workflow steps
- Clear completion messaging with next step guidance
- Maintains context across command invocations

## Success Indicators

User should experience:
- [ ] Clear understanding of current project state
- [ ] Obvious next steps at each stage
- [ ] Smooth progression through entire workflow
- [ ] No confusion about what to do next
- [ ] Ability to handle interruptions and resume work
- [ ] Support for multiple features in same project