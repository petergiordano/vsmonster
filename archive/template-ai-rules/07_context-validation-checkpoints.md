# Rule: Context Validation Checkpoints

## Goal
Ensure context continuity and prevent context drift across the 5-step workflow through systematic validation checkpoints.

## Context Validation Framework

### **Checkpoint 1: Project Initialization (Step 1)**
**Trigger:** Beginning of any new project or major feature
**Validation Requirements:**
- [ ] AI_CONTEXT.md is populated with project-specific details
- [ ] All project context documents exist and are complete
- [ ] Tech stack and conventions are clearly defined
- [ ] File structure is established and documented

**Context Accumulation:**
- Update AI_CONTEXT.md with project foundation
- Set workflow stage to "INITIALIZATION"
- Document initial architecture decisions

### **Checkpoint 2: Session Handoff (Step 2)**
**Trigger:** Beginning of any new AI assistant session
**Validation Requirements:**
- [ ] AI assistant has read complete AI_CONTEXT.md
- [ ] Current project state is understood
- [ ] Active features and their status are known
- [ ] Role boundaries are clear (Chat AI vs CLI AI)

**Context Validation Protocol:**
```
1. AI reads: "I have read the AI_CONTEXT.md. Current project state is [STATE]. 
   Active features: [LIST]. I understand my role as [CHAT_AI/CLI_AI]."
2. User confirms or corrects understanding
3. AI proceeds with context-aware assistance
```

### **Checkpoint 3: PRD Creation (Step 3)**
**Trigger:** After PRD is generated and before task creation
**Validation Requirements:**
- [ ] PRD aligns with project goals and constraints
- [ ] Integration points with existing features identified
- [ ] Technical feasibility confirmed within current architecture
- [ ] Success criteria are measurable and specific

**Context Accumulation:**
- Update AI_CONTEXT.md "Active Features" section
- Set feature status to "PRD_CREATED"
- Document key integration requirements
- Record architectural implications

### **Checkpoint 4: Task Generation (Step 4)**
**Trigger:** After task list is generated and before execution
**Validation Requirements:**
- [ ] Tasks align with existing code patterns
- [ ] File structure follows project conventions
- [ ] Dependencies and integration points identified
- [ ] Validation steps are executable and specific

**Context Accumulation:**
- Update feature status to "TASKS_GENERATED"
- Document planned file structure
- Record dependencies discovered
- Update validation commands if needed

### **Checkpoint 5: Execution Progress (Step 5)**
**Trigger:** After each parent task completion
**Validation Requirements:**
- [ ] Code follows established patterns
- [ ] Tests pass and coverage is maintained
- [ ] Integration points work correctly
- [ ] No architectural drift has occurred

**Context Accumulation:**
- Update feature status as progress occurs
- Document patterns discovered during implementation
- Record architectural decisions made
- Log lessons learned for future reference

### **Final Checkpoint: Feature Completion**
**Trigger:** When all tasks are marked complete
**Validation Requirements:**
- [ ] All PRD success criteria are met
- [ ] Complete feature works end-to-end
- [ ] Documentation is updated
- [ ] Context is properly archived

**Context Accumulation:**
- Move feature to "Completed Features" section
- Document final patterns and conventions
- Record integration lessons learned
- Update architectural decision log

## Context Handoff Protocols

### **Chat AI to CLI AI Handoff**
1. **Chat AI Preparation:**
   - Reviews current AI_CONTEXT.md state
   - Prepares specific, context-rich prompts
   - Includes relevant context sections in prompts
   
2. **CLI AI Context Loading:**
   - Reads AI_CONTEXT.md at start of session
   - Confirms understanding of current project state
   - Validates context before beginning work

3. **Validation Exchange:**
   ```
   CLI AI: "Context loaded. Project: [NAME], Stage: [STAGE], 
           Active features: [LIST]. Ready to proceed with [TASK]."
   User: "Confirmed" or provides corrections
   ```

### **Session-to-Session Continuity**
1. **Session End Protocol:**
   - Update AI_CONTEXT.md with session progress
   - Document any new patterns or decisions
   - Set clear status for next session

2. **Session Start Protocol:**
   - Read complete AI_CONTEXT.md
   - Confirm current state understanding
   - Review any changes since last session

## Context Drift Prevention

### **Warning Signs of Context Drift**
- AI suggests patterns that contradict existing code
- Proposed solutions ignore established architecture
- Validation commands don't match project setup
- File structure suggestions diverge from conventions

### **Context Drift Recovery**
1. **Immediate Stop:** Halt current work
2. **Context Re-validation:** Return to AI_CONTEXT.md
3. **Plan Mode Analysis:** Use Plan Mode to understand current state
4. **Realignment:** Adjust approach to match established context
5. **Documentation Update:** Record what caused the drift

## Implementation Notes

### **For Chat AI (Strategist):**
- Always reference AI_CONTEXT.md when preparing prompts
- Include relevant context sections in CLI AI instructions
- Update context accumulation sections as features progress

### **For CLI AI (Implementer):**
- Start every session by reading AI_CONTEXT.md
- Validate understanding before beginning implementation
- Use Plan Mode to confirm context alignment for complex tasks

### **For Users:**
- Review context updates after each major milestone
- Confirm AI understanding at validation checkpoints
- Keep AI_CONTEXT.md updated with project evolution