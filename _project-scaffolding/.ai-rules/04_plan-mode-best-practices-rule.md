# Rule: Plan Mode Best Practices for AI-Assisted Development

## Goal

To provide comprehensive guidance for using Claude Code's Plan Mode effectively within the AI-assisted development workflow. This rule file enhances the quality and safety of development by leveraging Plan Mode's read-only analysis capabilities.

## What is Plan Mode?

Plan Mode is Claude Code's built-in read-only mode that creates a safe environment for analysis, research, and planning without risk of accidental file modifications. It enforces the senior engineering practice of "plan first, then build."

### **Access Plan Mode:**
- **Enter:** Press Shift+Tab twice
- **Exit:** Press Shift+Tab once
- **Status:** Plan Mode is indicated in the CLI interface

## Strategic Plan Mode Usage

### **When to ALWAYS Use Plan Mode**

1. **Project Initialization** (Step 1)
   - Exploring existing project structure
   - Analyzing current dependencies and configuration
   - Understanding existing patterns before asking questions

2. **Complex Feature Planning** (Steps 3-4)
   - Understanding how new features integrate with existing architecture
   - Researching similar implementations in the codebase
   - Planning multi-file changes or architectural modifications

3. **Debugging Sessions** (Step 5)
   - Understanding issues before attempting fixes
   - Analyzing error patterns and root causes
   - Planning debugging strategies

4. **Code Reviews and Analysis**
   - Understanding changes before providing feedback
   - Analyzing impact of proposed modifications
   - Reviewing test coverage and patterns

### **When to CONSIDER Plan Mode**

1. **Simple Tasks with Unknown Context**
   - Even straightforward tasks benefit from context understanding
   - Quick analysis of existing patterns

2. **Refactoring Tasks**
   - Understanding current implementation before improving
   - Planning refactoring strategies

3. **Performance Optimization**
   - Analyzing bottlenecks before optimizing
   - Understanding system performance characteristics

### **When Plan Mode is OPTIONAL**

1. **Repetitive Pattern Implementation**
   - Tasks following well-established patterns
   - Simple bug fixes with clear solutions

2. **Isolated Utility Functions**
   - Self-contained functions with minimal dependencies
   - Pure functions with clear inputs/outputs

## Plan Mode Workflow Patterns

### **Pattern 1: Analysis → Plan → Execute**
*Best for complex features and architectural changes*

```
1. Enter Plan Mode (Shift+Tab twice)
2. Analyze existing codebase and requirements
3. Research patterns and dependencies
4. Create comprehensive implementation plan
5. Exit Plan Mode (Shift+Tab)
6. Present plan for approval
7. Execute according to approved plan
```

### **Pattern 2: Explore → Question → Plan**
*Best for unfamiliar codebases or unclear requirements*

```
1. Enter Plan Mode
2. Explore codebase structure and patterns
3. Formulate specific questions based on discoveries
4. Plan approach based on understanding
5. Exit Plan Mode
6. Ask clarifying questions
7. Implement with informed context
```

### **Pattern 3: Debug → Analyze → Fix**
*Best for troubleshooting and issue resolution*

```
1. Enter Plan Mode
2. Analyze error conditions and context
3. Research similar issues in codebase
4. Plan debugging strategy
5. Exit Plan Mode
6. Implement fix with confidence
```

## Plan Mode Thinking Strategies

### **Thinking Mode Escalation**

Use increasingly powerful thinking modes based on complexity:

1. **Standard Analysis:** Default Plan Mode thinking
2. **"think":** For moderately complex planning (basic thinking budget)
3. **"think hard":** For intricate business logic and integration planning
4. **"think harder":** For architectural decisions and complex debugging
5. **"ultrathink":** For major structural changes (31,999 token budget)

### **When to Use Each Thinking Mode**

**"think":**
- Understanding new feature requirements
- Planning simple integrations
- Basic architectural alignment

**"think hard":**
- Complex business logic implementation
- Multi-system integration planning
- Performance optimization strategies

**"think harder":**
- Major architectural decisions
- Complex debugging scenarios
- System design challenges

**"ultrathink":**
- Complete system overhauls
- Complex migration strategies
- Critical system design decisions

## Plan Mode Safety Protocols

### **Critical Safety Rules**

1. **Never Skip Plan Mode For:**
   - Changes to core configuration files
   - Modifications affecting authentication or security
   - Database schema changes
   - API contract modifications
   - Integration with external systems

2. **Always Verify in Plan Mode:**
   - Alignment with project conventions
   - Impact on existing functionality
   - Test coverage requirements
   - Error handling patterns

3. **Plan Mode Confirmation Checklist:**
   - [ ] Understand the current state
   - [ ] Identify all affected files
   - [ ] Plan test coverage approach
   - [ ] Consider error handling
   - [ ] Verify security implications
   - [ ] Check performance impact

### **Exit Plan Mode Safely**

Before exiting Plan Mode, always:
1. **Summarize your findings** to the user
2. **Present your implementation plan** clearly
3. **Wait for explicit approval** before proceeding
4. **Confirm understanding** of any special requirements

## Project-Specific Plan Mode Integration

### **Context Priming in Plan Mode**

Always start Plan Mode sessions by:
1. **Reading AI_CONTEXT.md** to understand project conventions
2. **Reviewing relevant project documents** in `.project-docs/`
3. **Examining existing code patterns** in `/src`
4. **Understanding test patterns** in `/tests`

### **Architecture Alignment Checks**

In Plan Mode, always verify:
- **Code Structure:** Follows established patterns in `/src/components` and `/src/lib`
- **Naming Conventions:** Aligns with project standards
- **Error Handling:** Matches established patterns
- **Testing Approach:** Follows project test conventions
- **Documentation:** Meets project documentation standards

## Plan Mode Efficiency Tips

### **Maximize Plan Mode Value**

1. **Batch Analysis:** Analyze multiple related files in one Plan Mode session
2. **Documentation Review:** Read relevant documentation during planning phase
3. **Pattern Recognition:** Identify and leverage existing code patterns
4. **Dependency Mapping:** Understand all dependencies before implementation

### **Minimize Plan Mode Overhead**

1. **Clear Objectives:** Know what you're analyzing before entering Plan Mode
2. **Focused Analysis:** Avoid unnecessary exploration
3. **Efficient Exit:** Exit Plan Mode as soon as planning is complete
4. **Structured Thinking:** Use thinking modes appropriately for the task complexity

## Plan Mode Anti-Patterns

### **What NOT to Do in Plan Mode**

1. **Analysis Paralysis:** Don't over-analyze simple tasks
2. **Scope Creep:** Stay focused on the current task
3. **Implementation Details:** Don't dive into detailed code in Plan Mode
4. **Premature Optimization:** Focus on correct implementation first

### **Common Plan Mode Mistakes**

1. **Forgetting to Exit:** Remaining in Plan Mode when ready to implement
2. **Insufficient Analysis:** Exiting Plan Mode before understanding the context
3. **Ignoring Existing Patterns:** Not researching established code patterns
4. **Skipping Safety Checks:** Not verifying security or performance implications

## Plan Mode Success Metrics

### **Quality Indicators**

- **Reduced Iterations:** Fewer back-and-forth corrections
- **Pattern Consistency:** New code follows established patterns
- **Fewer Bugs:** Better understanding leads to more robust implementations
- **Faster Implementation:** Less time spent on rework

### **Process Indicators**

- **Clear Plans:** Comprehensive implementation strategies
- **Informed Decisions:** Better architectural choices
- **Risk Mitigation:** Early identification of potential issues
- **Stakeholder Confidence:** Clear communication of proposed changes

## Integration with AI Rules

### **Plan Mode in Other Rules**

- **00_project-initialization.md:** Plan Mode for safe project exploration
- **01_create-prd.md:** Plan Mode for understanding feature context
- **02_generate-tasks.md:** Plan Mode for thorough requirement analysis
- **03_execute-tasks.md:** Plan Mode for complex task execution

### **Workflow Enhancement**

Plan Mode enhances every step of the AI-assisted development workflow by:
- **Increasing Safety:** Preventing accidental modifications
- **Improving Quality:** Better planning leads to better implementations
- **Reducing Risk:** Early identification of potential issues
- **Enhancing Understanding:** Deeper codebase comprehension