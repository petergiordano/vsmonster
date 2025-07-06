# Rule: Validation Loops Framework

## Goal
Implement systematic, executable validation loops that enable AI to self-correct and achieve working code through iterative refinement, similar to context engineering approaches but adapted for our human-guided workflow.

## Progressive Validation Architecture

### **Level 1: Syntax & Style Validation**
**Trigger:** After any code generation or modification
**Executable Commands:** AI must provide and run these commands

```bash
# Example validation commands (adapt to your project)
# Python projects:
black --check .                    # Code formatting
flake8 .                           # Style checking
mypy .                             # Type checking

# JavaScript/TypeScript projects:
npm run lint                       # ESLint
npm run prettier --check           # Code formatting
npm run type-check                 # TypeScript validation

# General:
# [Your project-specific linting commands]
```

**Success Criteria:**
- [ ] No syntax errors
- [ ] Code follows project formatting standards
- [ ] Type checking passes (if applicable)
- [ ] Linting rules satisfied

**AI Self-Correction Protocol:**
1. Run validation commands
2. If failures detected, read error output
3. Identify specific issues (syntax, style, types)
4. Apply targeted fixes
5. Re-run validation until clean
6. Only proceed after Level 1 passes

### **Level 2: Unit Test Validation**
**Trigger:** After implementing new functionality
**Executable Commands:**

```bash
# Test execution commands (adapt to your project)
# Python projects:
pytest tests/test_[module].py -v   # Specific module tests
pytest tests/ --cov=[module]       # Coverage checking

# JavaScript/TypeScript projects:
npm test [module]                  # Jest/Vitest specific tests
npm run test:coverage              # Coverage reporting

# [Your project-specific test commands]
```

**Success Criteria Checklist:**
- [ ] All new functionality has corresponding unit tests
- [ ] All existing tests continue to pass
- [ ] New tests cover happy path, edge cases, and error scenarios
- [ ] Test coverage meets project standards (typically 80%+)
- [ ] Test isolation is maintained (no test interdependencies)

**AI Test Creation Protocol:**
1. For each new function/class/component, create tests covering:
   ```python
   # Example test structure
   def test_[function_name]_happy_path():
       """Test normal operation with valid inputs"""
       pass
   
   def test_[function_name]_edge_case():
       """Test boundary conditions and edge cases"""
       pass
   
   def test_[function_name]_error_handling():
       """Test error conditions and exception handling"""
       pass
   ```
2. Run tests and verify they pass
3. If tests fail, debug code (not tests) until passing
4. Verify test quality and coverage

### **Level 3: Integration Validation**
**Trigger:** After implementing features that interact with existing systems
**Executable Commands:**

```bash
# Integration test commands
# Python projects:
pytest tests/integration/ -v       # Integration test suite
python -m [module] --test         # Module self-test

# JavaScript/TypeScript projects:
npm run test:integration          # Integration test suite
npm run start --test-mode         # Application test mode

# API/Service testing:
curl -X POST http://localhost:8000/api/test
# [Your project-specific integration commands]
```

**Success Criteria Checklist:**
- [ ] New features integrate correctly with existing components
- [ ] API endpoints respond correctly (if applicable)
- [ ] Database operations work as expected (if applicable)
- [ ] External service integrations function properly
- [ ] End-to-end user workflows complete successfully

**AI Integration Validation Protocol:**
1. Identify all integration points for new feature
2. Create/run integration tests for each point
3. Verify data flows correctly between components
4. Test error handling in integration scenarios
5. Validate performance impact is acceptable

### **Level 4: Feature Completion Validation**
**Trigger:** When all tasks for a feature are marked complete
**Executable Commands:**

```bash
# Full system validation
# Run complete test suite
pytest tests/ -v                  # Python full suite
npm test                          # JavaScript full suite

# System health checks
# [Your project-specific health check commands]

# Performance validation
# [Your project-specific performance tests]
```

**Success Criteria Checklist (PRD Alignment):**
- [ ] All PRD functional requirements are implemented
- [ ] All user stories can be completed successfully
- [ ] All acceptance criteria are met
- [ ] Non-functional requirements satisfied (performance, security, etc.)
- [ ] Integration with existing features is seamless
- [ ] Documentation is updated appropriately

## Validation Loop Error Correction Protocol

### **Error Analysis Framework**
When validation fails, AI must follow this systematic approach:

1. **Error Classification:**
   ```
   - Syntax Error: Code structure issues
   - Logic Error: Incorrect implementation
   - Integration Error: Component interaction issues
   - Test Error: Test setup or assertion issues
   - Configuration Error: Environment or setup issues
   ```

2. **Root Cause Analysis:**
   - Read complete error message and stack trace
   - Identify the exact line/function causing failure
   - Understand why the error occurred
   - Consider impact on other components

3. **Targeted Fix Strategy:**
   - Apply minimal fix that addresses root cause
   - Avoid over-engineering or unnecessary changes
   - Preserve existing functionality
   - Maintain code patterns and conventions

4. **Validation Re-run:**
   - Re-execute the same validation level
   - Confirm fix resolves the specific issue
   - Verify no new errors were introduced
   - Proceed to next validation level only after success

### **Multi-Level Validation Flow**
```
Code Implementation
        ↓
Level 1: Syntax & Style ← Fix errors and retry
        ↓ (if pass)
Level 2: Unit Tests ← Fix code (not tests) and retry
        ↓ (if pass)
Level 3: Integration ← Fix integration issues and retry
        ↓ (if pass)
Level 4: Feature Complete ← Address gaps and retry
        ↓ (if pass)
Feature Approved for Completion
```

## Success Criteria Templates

### **For PRD Validation**
Create this checklist during PRD creation:

```markdown
## Feature Success Criteria (Executable Validation)

### Functional Validation
- [ ] Requirement 1: [Specific test command to verify]
- [ ] Requirement 2: [Specific test command to verify]
- [ ] User Story 1: [Step-by-step validation process]

### Technical Validation
- [ ] Code quality: `[linting command]` passes
- [ ] Type safety: `[type check command]` passes
- [ ] Test coverage: `[coverage command]` shows ≥80%
- [ ] Integration: `[integration test command]` passes

### Performance Validation
- [ ] Load time: [Specific performance metric]
- [ ] Memory usage: [Specific performance metric]
- [ ] API response time: [Specific performance metric]

### User Experience Validation
- [ ] Workflow 1: [Manual test steps]
- [ ] Workflow 2: [Manual test steps]
- [ ] Error scenarios: [Error handling test steps]
```

### **For Task-Level Validation**
Add to each task in task lists:

```markdown
- [ ] 1.1 Implement user authentication
  **Validation:**
  - Syntax: `npm run lint` passes
  - Tests: `npm test auth` passes
  - Integration: Login flow works end-to-end
  - Success: User can login/logout successfully
```

## Implementation in Existing Rules

### **Integration with `/generate-prd` Command**
- Add success criteria generation to PRD creation
- Include executable validation commands in PRD
- Create feature-specific validation checklist

### **Integration with `/generate-tasks` Command**
- Add validation steps to each generated task
- Include specific commands for each validation level
- Create task-level success criteria

### **Integration with `/execute-tasks` Command**
- Run validation loops after each sub-task completion
- Require validation success before proceeding
- Implement error correction protocol for failures

## Project-Specific Validation Configuration

### **Validation Commands Configuration**
Document your project's specific validation commands:

```markdown
## Project Validation Commands

### Level 1 (Syntax & Style):
- Formatting: `[your formatting command]`
- Linting: `[your linting command]`
- Type checking: `[your type checking command]`

### Level 2 (Unit Tests):
- Test execution: `[your test command]`
- Coverage check: `[your coverage command]`

### Level 3 (Integration):
- Integration tests: `[your integration test command]`
- API testing: `[your API test command]`

### Level 4 (Feature Complete):
- Full test suite: `[your full test command]`
- Health checks: `[your health check command]`
```

This configuration gets added to your project-specific AI_CONTEXT.md file.