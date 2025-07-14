# Rule: Generating a Task List from a PRD

## Goal

To guide an AI assistant in creating a detailed, step-by-step task list in Markdown format based on an existing Product Requirements Document (PRD). The task list should guide a developer through implementation.

## Enhanced Task Generation Options

### **Standard Approach (Default)**
Use the process outlined below for AI-guided task generation with manual structuring.

### **Enhanced Approach (Optional - Claude Task Master)**
If the user has Claude Task Master MCP configured, you can offer enhanced task generation:

**When to Suggest Enhanced Approach:**
- Complex projects with many dependencies
- PRDs with sophisticated requirements
- Projects requiring detailed complexity analysis

**Enhanced Task Master Tools:**
- `parse_prd` - Automatically parse PRD into structured tasks with dependencies
- `analyze_project_complexity` - Identify tasks needing further breakdown
- `expand_all` - Break down complex tasks into manageable subtasks

**Example Enhanced Workflow:**
```
User: "Generate tasks from my PRD at tasks/prd-feature-name.md"
AI: "I can create tasks using our standard approach, or if you have Claude Task Master configured, I can use the enhanced `parse_prd` tool for more sophisticated task breakdown with dependency analysis. Which would you prefer?"
```

### **Framework Compatibility**
Regardless of approach chosen, maintain our framework's core principles:
- Human approval gates between phases
- Context accumulation in AI_CONTEXT.md
- Progressive validation integration
- Chat AI ↔ CLI AI collaboration patterns

## Standard Process (Default Approach)

- **Format:** Markdown (`.md`)
- **Location:** `/tasks/`
- **Filename:** `tasks-[prd-file-name].md` (e.g., `tasks-prd-user-profile-editing.md`)

## Process

1.  **Receive PRD Reference:** The user points the AI to a specific PRD file
2.  **Enter Plan Mode:** If using Claude Code CLI, press Shift+Tab twice to enter Plan Mode for safe analysis
3.  **Analyze PRD:** The AI reads and analyzes the functional requirements, user stories, and other sections of the specified PRD. In Plan Mode, this analysis happens without risk of accidental file modifications.
4.  **Phase 1: Generate Parent Tasks:** Based on the PRD analysis, create the file and generate the main, high-level tasks required to implement the feature. Use your judgement on how many high-level tasks to use. It's likely to be about 5. Present these tasks to the user in the specified format (without sub-tasks yet). Inform the user: "I have generated the high-level tasks based on the PRD. Ready to generate the sub-tasks? Respond with 'Go' to proceed."
5.  **Wait for Confirmation:** Pause and wait for the user to respond with "Go".
6.  **Exit Plan Mode (if applicable):** If using Claude Code CLI Plan Mode, exit Plan Mode (Shift+Tab) to enable file creation
7.  **Phase 2: Generate Sub-Tasks:** Once the user confirms, break down each parent task into smaller, actionable sub-tasks necessary to complete the parent task. Ensure sub-tasks logically follow from the parent task and cover the implementation details implied by the PRD.
8.  **Identify Relevant Files:** Based on the tasks and PRD, identify potential files that will need to be created or modified. List these under the `Relevant Files` section, including corresponding test files if applicable.
9.  **Generate Final Output:** Combine the parent tasks, sub-tasks, relevant files, and notes into the final Markdown structure.
10. **Save Task List:** Save the generated document in the `/tasks/` directory with the filename `tasks-[prd-file-name].md`, where `[prd-file-name]` matches the base name of the input PRD file (e.g., if the input was `prd-user-profile-editing.md`, the output is `tasks-prd-user-profile-editing.md`).

## Claude Code Plan Mode Integration

When using Claude Code CLI for this process, leverage Plan Mode for enhanced analysis:

### **Recommended Plan Mode Workflow:**
1. **Enter Plan Mode:** Press Shift+Tab twice
2. **Analyze Context:** Read the PRD file and any related project files
3. **Research Dependencies:** Examine existing codebase structure and patterns
4. **Create Mental Model:** Understand how the new feature fits into the existing architecture
5. **Generate High-Level Plan:** Create the parent tasks structure
6. **Present for Approval:** Show the high-level breakdown to the user
7. **Exit Plan Mode:** After user confirms, exit Plan Mode to create the actual task file

### **Benefits of Using Plan Mode:**
- **Safe Analysis:** Explore the codebase and PRD without accidental modifications
- **Comprehensive Understanding:** Take time to fully understand the requirements before committing to a task structure
- **Better Architecture Alignment:** Ensure tasks align with existing project patterns and conventions
- **Reduced Iterations:** More thorough upfront analysis leads to better initial task breakdowns


## Output Format

The generated task list _must_ follow this structure with integrated validation:

```markdown
## Relevant Files

- `path/to/potential/file1.ts` - Brief description of why this file is relevant
- `path/to/file1.test.ts` - Unit tests for `file1.ts`
- `path/to/another/file.tsx` - Brief description  
- `path/to/another/file.test.tsx` - Unit tests for `another/file.tsx`

### Validation Commands Reference
```bash
# Level 1 - Syntax & Style:
[linting command]         # e.g., npm run lint
[formatting command]      # e.g., prettier --check .
[type checking command]   # e.g., npm run type-check

# Level 2 - Unit Testing:
[unit test command]       # e.g., npm test [module]
[coverage command]        # e.g., npm run test:coverage

# Level 3 - Integration:
[integration command]     # e.g., npm run test:integration
[api test command]        # e.g., curl -X POST localhost:3000/api/test

# Level 4 - Feature Complete:
[full test suite]         # e.g., npm test
[health check]           # e.g., npm run health-check
```

### Notes

- Unit tests should typically be placed alongside the code files they are testing (e.g., `MyComponent.tsx` and `MyComponent.test.tsx` in the same directory).
- Use `npx jest [optional/path/to/test/file]` to run tests. Running without a path executes all tests found by the Jest configuration.

## Tasks with Integrated Validation

- [ ] 1.0 **Setup & Foundation**
  - [ ] 1.1 Create project structure and configuration files
    **Validation:**
    - ✅ Level 1: `[linting command]` passes
    - ✅ Level 1: Project structure matches conventions
    - ✅ Manual: Configuration files are valid
    
  - [ ] 1.2 Set up database schema and migrations
    **Validation:**
    - ✅ Level 1: `[schema validation command]` passes
    - ✅ Level 2: `[migration test command]` passes
    - ✅ Manual: Database setup works correctly

- [ ] 2.0 **Core Functionality Implementation**
  - [ ] 2.1 Implement main business logic module
    **Validation:**
    - ✅ Level 1: `[linting command]` passes
    - ✅ Level 2: `[unit test command for module]` passes
    - ✅ Level 2: Test coverage ≥ 80% for this module
    - ✅ Manual: Business logic works as expected
    
  - [ ] 2.2 Add API endpoints for feature operations
    **Validation:**
    - ✅ Level 1: `[api linting command]` passes
    - ✅ Level 2: `[api unit tests]` pass
    - ✅ Level 3: `[api integration tests]` pass
    - ✅ Manual: API endpoints respond correctly
    
  - [ ] 2.3 Implement data persistence layer
    **Validation:**
    - ✅ Level 1: `[data layer linting]` passes
    - ✅ Level 2: `[data layer unit tests]` pass
    - ✅ Level 3: `[database integration tests]` pass
    - ✅ Manual: Data persists and retrieves correctly

- [ ] 3.0 **User Interface & Experience**
  - [ ] 3.1 Create main UI components
    **Validation:**
    - ✅ Level 1: `[ui linting command]` passes
    - ✅ Level 2: `[component unit tests]` pass
    - ✅ Level 3: `[component integration tests]` pass
    - ✅ Manual: Components render and function correctly
    
  - [ ] 3.2 Implement user workflows and navigation
    **Validation:**
    - ✅ Level 1: `[workflow linting]` passes
    - ✅ Level 3: `[end-to-end workflow tests]` pass
    - ✅ Manual: User can complete intended workflows

- [ ] 4.0 **Testing & Quality Assurance**
  - [ ] 4.1 Create comprehensive test suite
    **Validation:**
    - ✅ Level 2: All test files have valid syntax
    - ✅ Level 2: `[full test suite]` passes
    - ✅ Level 2: Overall coverage ≥ 80%
    - ✅ Manual: Tests cover happy path, edge cases, errors
    
  - [ ] 4.2 Add error handling and validation
    **Validation:**
    - ✅ Level 1: `[error handling linting]` passes
    - ✅ Level 2: `[error handling tests]` pass
    - ✅ Level 3: `[error scenario integration tests]` pass
    - ✅ Manual: Errors are handled gracefully

- [ ] 5.0 **Integration & Polish**
  - [ ] 5.1 Integrate with existing system components
    **Validation:**
    - ✅ Level 3: `[system integration tests]` pass
    - ✅ Level 4: `[full system test suite]` passes
    - ✅ Manual: No regressions in existing features
    
  - [ ] 5.2 Performance optimization and final testing
    **Validation:**
    - ✅ Level 4: `[performance test suite]` passes
    - ✅ Level 4: `[full validation suite]` passes
    - ✅ Manual: Performance meets requirements
    
  - [ ] 5.3 Documentation and deployment preparation
    **Validation:**
    - ✅ Level 1: Documentation linting passes
    - ✅ Manual: Documentation is complete and accurate
    - ✅ Manual: Feature is ready for deployment

## Final Feature Validation Checklist

After completing all tasks, validate against original PRD:

### PRD Success Criteria Validation
- [ ] **Functional Requirements:** All requirements from PRD are implemented
  - **Command:** `[feature validation command]`
  - **Manual Check:** Each requirement can be demonstrated
  
- [ ] **User Stories:** All user stories can be completed successfully
  - **Validation:** Step through each user story manually
  - **Success:** User achieves intended outcome for each story
  
- [ ] **Performance Requirements:** Feature meets performance standards
  - **Command:** `[performance validation command]`
  - **Success:** Metrics meet or exceed PRD requirements

### Technical Quality Validation
- [ ] **Code Quality:** All code meets project standards
  - **Command:** `[full linting and type checking]`
  - **Success:** No linting errors, type checking passes
  
- [ ] **Test Coverage:** Comprehensive test coverage achieved
  - **Command:** `[full coverage report]`
  - **Success:** Coverage ≥ 80%, all critical paths tested
  
- [ ] **Integration:** Feature integrates cleanly with existing system
  - **Command:** `[full integration test suite]`
  - **Success:** All integration tests pass, no regressions

### User Experience Validation
- [ ] **Usability:** Feature is intuitive and user-friendly
  - **Manual Test:** Complete each user workflow
  - **Success:** Users can achieve goals without confusion
  
- [ ] **Error Handling:** Errors are handled gracefully
  - **Manual Test:** Trigger error scenarios
  - **Success:** Users receive helpful feedback for errors
  
- [ ] **Performance:** Feature performs within acceptable limits
  - **Manual Test:** Use feature under normal load
  - **Success:** Responsive performance, no blocking operations

## Validation Integration Guidelines

When generating task lists:

1. **Each Sub-Task Must Include Validation Steps**
   - Specify exact commands to run
   - Define clear success criteria
   - Include both automated and manual validation

2. **Progressive Validation Levels**
   - Level 1 validation for syntax and style
   - Level 2 validation for unit testing
   - Level 3 validation for integration
   - Level 4 validation for feature completion

3. **Clear Success Criteria**
   - Executable commands with expected results
   - Manual verification steps where needed
   - Cross-reference to PRD requirements

4. **Validation Command Specificity**
   - Use actual project commands, not placeholders
   - Include specific file paths where relevant
   - Provide clear error identification guidance

This validation integration ensures that every task includes clear, executable validation steps, enabling the systematic quality assurance approach throughout the development process.

## Interaction Model

The process explicitly requires a pause after generating parent tasks to get user confirmation ("Go") before proceeding to generate the detailed sub-tasks. This ensures the high-level plan aligns with user expectations before diving into details.

## Target Audience

Assume the primary reader of the task list is a **junior developer** who will implement the feature.