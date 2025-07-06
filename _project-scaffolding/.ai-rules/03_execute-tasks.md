# Rule: Task List Execution

## Goal

You are an AI assistant helping me implement a feature by following a provided task list. Your role is to provide the code for each sub-task. When a parent task is complete, you will **compose a detailed commit message** for me to use in my GitHub Desktop app.

## Task Execution Options

### **Standard Approach (Default)**
Use the manual task tracking process outlined below.

### **Enhanced Approach (Optional - Claude Task Master)**
If the user has Claude Task Master MCP configured, you can offer enhanced task execution:

**When to Suggest Enhanced Approach:**
- Complex projects with task dependencies
- Projects requiring systematic progress tracking
- Features with multiple interdependent components

**Enhanced Task Master Tools:**
- `next_task` - Get dependency-aware task recommendations
- `get_task` - Understand task context and requirements  
- `set_task_status` - Track progress systematically
- `update_task` - Modify tasks based on implementation learnings
- `analyze_project_complexity` - Identify bottlenecks before they occur

**Example Enhanced Workflow:**
```
User: "Let's start implementing the tasks"
AI: "I can guide you through manual task execution, or if you have Claude Task Master configured, I can use smart task selection with `next_task` and systematic progress tracking. Which approach would you prefer?"
```

### **Framework Compatibility**
Both approaches maintain our framework's core principles:
- Progressive validation loops and error correction
- Human approval gates and decision points
- Context accumulation and commit message generation
- Plan Mode integration for complex analysis

## Enhanced Process (Command-Driven with Validation Loops)

### Phase 1: Context Loading & Validation
1. **Load Task List:** Read the specified task list file completely
2. **Enter Plan Mode** (Shift+Tab twice) for initial analysis:
   - Understand all context and requirements from task list
   - Review existing codebase patterns mentioned in tasks
   - Analyze integration points and dependencies
   - Validate that all referenced files and patterns exist
3. **Context Validation Checkpoint:**
   - Confirm all necessary context is available
   - Identify any missing information or unclear requirements
   - Ask clarifying questions if context is insufficient

### Phase 2: Strategic Planning
4. **Plan Implementation Strategy:**
   - Create comprehensive plan addressing all requirements
   - Use TodoWrite tool to track implementation steps
   - Identify potential challenges and solutions
   - Plan validation approach for each task
5. **Exit Plan Mode** and present strategy to user for approval

### Phase 3: Iterative Task Execution
6. **Execute Next Sub-Task:**
   - Find the next uncompleted sub-task (`[ ]`)
   - Provide code or instructions for **only that single sub-task**
   - Include relevant validation steps for the specific task
7. **Validation Loop for Each Sub-Task:**
   - Provide validation command(s) specific to the sub-task
   - Wait for user to implement and test
   - If validation fails, analyze error and provide fix
   - Repeat until sub-task validation passes
8. **Parent Task Completion Check:**
   - After completing a sub-task, check if it was the final sub-task for a parent item
   - If parent task is complete, provide formatted commit message:
     ```
     type: Short summary of the parent task
     
     - Detail of the first key change
     - Detail of the second key change
     - Add more details as needed
     
     Related to Task #[TaskNumber]
     ```

### Phase 4: Continuous Validation
9. **Progressive Validation Gates:**
   - **Syntax Level:** Code compiles, no syntax errors
   - **Unit Test Level:** New functionality passes unit tests
   - **Integration Level:** Changes work with existing system
   - **Feature Level:** Complete feature meets PRD success criteria
10. **Error Correction Protocol:**
    - Read and analyze any error messages
    - Identify root cause (syntax, logic, integration, etc.)
    - Provide specific fix with explanation
    - Re-run validation until passing

### Phase 5: Workflow Control
11. **PAUSE and WAIT:** After each sub-task implementation and validation
12. **User Signal:** Wait for "Go", "Proceed", "y", or "yes" to continue
13. **Plan Mode Re-entry:** Use Plan Mode again for complex debugging or architectural decisions
14. **Completion Verification:** Ensure all success criteria are met before marking feature complete

## Validation Loop Integration in Task Execution

### **Enhanced Sub-Task Execution with Validation**

Replace the existing "Execute Next Sub-Task" step with this validation-integrated approach:

#### **Sub-Task Execution Protocol:**

1. **Implement Sub-Task:**
   - Provide code or instructions for the specific sub-task
   - Include relevant patterns from existing codebase
   - Follow established conventions from AI_CONTEXT.md

2. **Immediate Validation Loop:**
   - **Level 1 - Syntax & Style:**
     ```bash
     # Provide specific commands for user to run
     [formatting command]  # e.g., black . or npm run prettier
     [linting command]     # e.g., flake8 . or npm run lint
     [type check command]  # e.g., mypy . or npm run type-check
     ```
   - **Expected Result:** All commands pass with no errors
   - **If Failures:** AI analyzes error output and provides targeted fixes

3. **Sub-Task Specific Validation:**
   - **Level 2 - Unit Tests (if new functionality):**
     ```bash
     # Test commands specific to the sub-task
     [unit test command]   # e.g., pytest tests/test_module.py
     [coverage command]    # e.g., pytest --cov=module
     ```
   - **Level 3 - Integration Tests (if applicable):**
     ```bash
     # Integration validation for sub-task
     [integration command] # e.g., npm run test:integration
     ```

4. **Success Confirmation:**
   - User reports validation results: "Level 1 ✅, Level 2 ✅" or "Level 1 ❌ [error details]"
   - If validation fails, AI enters error correction mode
   - Only proceed to next sub-task after validation success

#### **Error Correction Mode:**

When validation fails, AI follows this protocol:

1. **Error Analysis:**
   ```
   AI: "I see the validation failed with: [error summary]. 
        Let me analyze the root cause..."
   ```

2. **Root Cause Identification:**
   - Read complete error message
   - Identify specific code/configuration issue
   - Understand why the error occurred

3. **Targeted Fix:**
   - Provide minimal, specific fix
   - Explain what the fix addresses
   - Maintain existing patterns and conventions

4. **Re-validation:**
   - User runs same validation commands
   - AI confirms fix worked or provides additional corrections
   - Continue until validation passes

#### **Parent Task Completion with Feature Validation:**

When completing the final sub-task of a parent task:

1. **Feature-Level Validation:**
   ```bash
   # Complete feature validation commands
   [full test suite]     # e.g., pytest tests/ or npm test
   [integration check]   # e.g., end-to-end workflow test
   [performance check]   # e.g., load time or memory usage
   ```

2. **PRD Success Criteria Check:**
   - Review original PRD success criteria
   - Confirm each criterion is met
   - Validate user stories can be completed

3. **Commit Message Generation:**
   - Only generate commit message after full validation success
   - Include validation status in commit details:
   ```
   feat: implement user authentication system
   
   - Add JWT-based authentication middleware
   - Implement login/logout endpoints  
   - Add password hashing and validation
   - Include comprehensive test coverage (95%)
   
   Validation: ✅ All tests pass, ✅ Integration verified, ✅ PRD criteria met
   Related to Task #[TaskNumber]
   ```

### **Validation Status Tracking**

Throughout task execution, maintain validation status:

```
Current Sub-Task: 2.3 Implement password validation
Validation Status:
├── Level 1 (Syntax): ✅ Passed
├── Level 2 (Unit Tests): 🔄 Running  
├── Level 3 (Integration): ⏳ Pending
└── Feature Complete: ⏳ Pending

Ready for next step: Waiting for Level 2 validation results
```

### **Integration with Context Accumulation**

After each successful validation:

1. **Update AI_CONTEXT.md:**
   - Record successful patterns discovered
   - Document validation approaches that work
   - Note any architectural decisions made

2. **Accumulate Validation Knowledge:**
   - Add project-specific validation commands
   - Record common error patterns and solutions
   - Update best practices based on validation results

### **Enhanced User Communication**

Clear communication about validation expectations:

```
AI: "I've implemented the user authentication middleware. 
     Please run these validation commands:
     
     Level 1 - Code Quality:
     ✓ npm run lint
     ✓ npm run prettier --check  
     ✓ npm run type-check
     
     Level 2 - Unit Tests:
     ✓ npm test auth.middleware
     ✓ npm run test:coverage
     
     Expected: All commands should pass with no errors.
     Please share the results so I can proceed or fix any issues."

User: "Level 1 ✅, Level 2 ❌ - coverage is only 60%"

AI: "I see the coverage issue. Let me add the missing test cases 
     for error scenarios and edge cases..."
```

This validation loop integration ensures that every sub-task is properly validated before proceeding, preventing issues from accumulating and ensuring high-quality code throughout the development process.

## Command-Driven Benefits
- **Clear Phase Boundaries:** Explicit transitions between planning and execution
- **Built-in Validation:** Progressive validation prevents downstream errors
- **Context Preservation:** Plan Mode usage maintains comprehensive understanding
- **Human Control Points:** User approval at key decision points
- **Error Recovery:** Systematic approach to identifying and fixing issues

## Claude Code Plan Mode Integration

For enhanced task execution, leverage Plan Mode strategically:

### **When to Use Plan Mode During Execution:**

**Always Use Plan Mode For:**
- **Complex Parent Tasks:** Before starting any parent task with multiple sub-tasks
- **Architecture Changes:** Tasks that modify core structure or patterns
- **Integration Points:** Tasks that touch multiple files or systems
- **Debugging Issues:** When implementation doesn't work as expected

**Optional Plan Mode For:**
- **Simple Sub-Tasks:** Straightforward code additions or modifications
- **Repetitive Patterns:** Tasks following established patterns in the codebase

### **Recommended Plan Mode Workflow for Complex Tasks:**

1. **Enter Plan Mode:** Press Shift+Tab twice
2. **Analyze Current State:** 
   - Read relevant files mentioned in the task
   - Understand existing code patterns and architecture
   - Review any dependencies or integration points
3. **Plan Implementation Strategy:**
   - Determine the best approach for the specific sub-task
   - Identify potential issues or edge cases
   - Consider how this change fits with existing code
4. **Present Implementation Plan:** Exit Plan Mode and explain your approach before providing code
5. **Implement:** Provide the actual code implementation

### **Example Plan Mode Usage:**

```
# User provides task list with complex parent task
# AI enters Plan Mode first

[In Plan Mode - Analysis Phase]
"Let me analyze the codebase structure and understand how to implement the user authentication system..."

[Exits Plan Mode - Implementation Phase]
"Based on my analysis, I'll implement the authentication middleware by creating a new file at `src/middleware/auth.ts` that integrates with your existing Express setup..."
```

## Commit Message Protocol

When I complete the final sub-task of a parent task, you must generate a commit message for me to copy and paste into GitHub Desktop. The message should be formatted like this:

**Subject Line:**
`type: A short summary of the parent task`

**Body:**

- Detail of the first key change.
- Detail of the second key change.
- Add more details as needed.

Related to Task #[TaskNumber]

## Enhanced Workflow for Complex Features

For parent tasks with significant complexity, use this enhanced workflow:

### **Phase 1: Plan Mode Analysis**
1. Enter Plan Mode (Shift+Tab twice)
2. Analyze the entire parent task and its sub-tasks
3. Review existing codebase for patterns and integration points
4. Create implementation strategy
5. Exit Plan Mode

### **Phase 2: Structured Implementation**
1. Present overall strategy to user for approval
2. Implement sub-tasks one by one
3. Use Plan Mode again if unexpected complexity arises
4. Provide commit message when parent task is complete

### **Benefits of This Approach:**
- **Reduced Errors:** Better understanding before implementation
- **Consistent Patterns:** Alignment with existing codebase conventions
- **Fewer Iterations:** More thoughtful initial implementations
- **Better Integration:** Understanding of how changes affect the broader system

## My Role (The User)

-   I will tell you when to proceed.
-   I will handle all Git operations (staging, committing, pushing) using the **GitHub Desktop app**.
-   **I am responsible for updating the task list file and marking tasks as complete (`[x]`).**

Your job is to focus on one sub-task at a time, provide the code, provide a commit message when necessary, and then wait for my signal.

## Plan Mode Best Practices for Task Execution

- **Use "think harder" or "ultrathink"** in Plan Mode for complex architectural decisions
- **Read relevant documentation** in Plan Mode before implementing unfamiliar patterns
- **Examine test files** in Plan Mode to understand expected behavior
- **Check for existing utilities** that could be reused rather than rebuilding
- **Consider error handling patterns** established in the codebase
- **Verify security implications** for authentication, data handling, or API endpoints

## Enhanced Task Execution with Claude Task Master Integration

*This section applies when users choose the enhanced approach with Task Master tools.*

### **Enhanced Task Selection**
Instead of manually scanning task lists:
```
Standard: "Find the next uncompleted sub-task ([   ])"
Enhanced: Use `next_task` tool to get dependency-aware recommendations
```

### **Enhanced Progress Tracking**
Instead of manual status updates:
```
Standard: User manually marks tasks complete with [x]
Enhanced: Use `set_task_status` to systematically track progress and dependencies
```

### **Enhanced Context Understanding**
For complex tasks:
```
Standard: Read task description from list
Enhanced: Use `get_task` to get detailed context, requirements, and relationships
```

### **Enhanced Complexity Management**
For identifying bottlenecks:
```
Standard: Recognize complexity issues during implementation
Enhanced: Use `analyze_project_complexity` to identify issues proactively
```

### **Hybrid Workflow Example**
```
1. AI: "Starting task execution. Using `next_task` to find optimal starting point..."
2. AI: "Task Master recommends starting with Task #3 (authentication setup) as it has no dependencies. Proceeding with implementation..."
3. AI: [Provides code for Task #3 using standard validation loops]
4. User: [Tests and approves]
5. AI: "Using `set_task_status` to mark Task #3 complete and update dependencies..."
6. AI: "Ready for next sub-task. Using `next_task` again..."
```

### **Commit Message Enhancement**
Task Master provides additional context for commit messages:
```
Standard Commit:
feat: implement user authentication
- Add login endpoint
- Add JWT validation
Related to Task #3

Enhanced Commit (with Task Master context):
feat: implement user authentication
- Add login endpoint with bcrypt hashing
- Add JWT validation middleware
- Completed dependency for Tasks #4, #7, #9
Related to Task #3 | Next: Task #4 (user profile endpoints)
```

### **When to Use Enhanced vs Standard**
- **Use Enhanced:** Complex features, multiple dependencies, team coordination needed
- **Use Standard:** Simple features, linear development, learning the workflow
- **Switch Mid-Project:** Can transition between approaches as project complexity changes