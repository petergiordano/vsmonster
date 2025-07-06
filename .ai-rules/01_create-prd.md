# Rule: Generating a Product Requirements Document (PRD)

## Goal

To guide an AI assistant in creating a detailed Product Requirements Document (PRD) in Markdown format, based on an initial user prompt. The PRD should be clear, actionable, and suitable for a junior developer to understand and implement the feature.

## Process

1.  **Receive Initial Prompt:** The user provides a brief description or request for a new feature or functionality.
2.  **Ask Clarifying Questions:** Before writing the PRD, you *must* ask me clarifying questions to gather sufficient detail. The goal is to understand the "what" and "why" of the feature, not necessarily the "how".
3.  **Generate PRD:** Based on my answers to your clarifying questions, generate a PRD using the structure outlined below.
4.  **Save PRD:** I will save the generated document as `prd-[feature-name].md`.

## Clarifying Questions (Examples)

Adapt your questions based on the prompt, but here are some common areas to explore:

* **Problem/Goal:** "What problem does this feature solve for the user?" or "What is the main goal we want to achieve with this feature?"
* **Target User:** "Who is the primary user of this feature?"
* **Core Functionality:** "Can you describe the key actions a user should be able to perform with this feature?"
* **User Stories:** "Could you provide a few user stories? (e.g., As a [type of user], I want to [perform an action] so that [benefit].)"
* **Acceptance Criteria:** "How will we know when this feature is successfully implemented? What are the key success criteria?"
* **Scope/Boundaries:** "Are there any specific things this feature *should not* do (non-goals)?"
* **Data Requirements:** "What kind of data does this feature need to display or manipulate?"
* **Design/UI:** "Are there any existing design mockups or UI guidelines to follow?" or "Can you describe the desired look and feel?"
* **Edge Cases:** "Are there any potential edge cases or error conditions we should consider?"

## PRD Structure

The generated PRD should include the following sections:

1.  **Introduction/Overview:** Briefly describe the feature and the problem it solves. State the goal.
2.  **Goals:** List the specific, measurable objectives for this feature.
3.  **User Stories:** Detail the user narratives describing feature usage and benefits.
4.  **Functional Requirements:** List the specific functionalities the feature must have. Use clear, concise language (e.g., "The system must allow users to upload a profile picture."). Number these requirements.
5.  **Non-Goals (Out of Scope):** Clearly state what this feature will *not* include to manage scope.
6.  **Design Considerations (Optional):** Link to mockups, describe UI/UX requirements, or mention relevant components/styles if applicable.
7.  **Technical Considerations (Optional):** Mention any known technical constraints, dependencies, or suggestions (e.g., "Should integrate with the existing Auth module").
8.  **Success Metrics:** How will the success of this feature be measured? (e.g., "Increase user engagement by 10%").
9.  **Open Questions:** List any remaining questions or areas needing further clarification.

## Enhanced PRD Structure with Executable Success Criteria

Update the PRD generation to include this additional section after "Success Metrics":

### **9. Executable Success Criteria (Validation Framework)**

This section provides specific, testable criteria that can be validated during implementation:

```markdown
## Executable Success Criteria

### Functional Validation Checklist
- [ ] **Requirement 1:** [Specific functional requirement]
  - **Test Command:** `[specific command to verify this works]`
  - **Expected Result:** [what should happen when test passes]
  - **Manual Verification:** [step-by-step user workflow to test]

- [ ] **Requirement 2:** [Specific functional requirement]  
  - **Test Command:** `[specific command to verify this works]`
  - **Expected Result:** [what should happen when test passes]
  - **Manual Verification:** [step-by-step user workflow to test]

### Technical Validation Checklist
- [ ] **Code Quality Standards:**
  - Linting passes: `[project linting command]`
  - Type checking passes: `[project type check command]`
  - Formatting standards met: `[project formatting command]`

- [ ] **Test Coverage Requirements:**
  - Unit test coverage ≥ 80%: `[coverage command]`
  - All new functions have tests: Manual review required
  - Integration tests included: `[integration test command]`

- [ ] **Performance Requirements:**
  - Feature loads within [X] seconds: `[performance test command]`
  - Memory usage within acceptable limits: `[memory test command]`
  - API response time < [X]ms: `[API test command]`

### User Experience Validation Checklist
- [ ] **User Story 1:** [User story from earlier in PRD]
  - **Validation Steps:**
    1. [Step 1 of user workflow]
    2. [Step 2 of user workflow]  
    3. [Step 3 of user workflow]
  - **Success Criteria:** User can complete workflow without errors

- [ ] **User Story 2:** [User story from earlier in PRD]
  - **Validation Steps:**
    1. [Step 1 of user workflow]
    2. [Step 2 of user workflow]
    3. [Step 3 of user workflow]
  - **Success Criteria:** User achieves intended outcome

### Integration Validation Checklist  
- [ ] **Existing Feature Compatibility:**
  - Feature works with [existing feature 1]: `[integration test]`
  - Feature works with [existing feature 2]: `[integration test]`
  - No regressions in existing functionality: `[regression test suite]`

- [ ] **Data Flow Validation:**
  - Data persists correctly: `[data persistence test]`
  - Data retrieval works: `[data retrieval test]`
  - Error handling works: `[error scenario test]`

### Security & Error Handling Validation
- [ ] **Security Requirements:**
  - Input validation prevents injection: `[security test command]`
  - Authentication/authorization works: `[auth test command]`
  - Sensitive data is protected: Manual security review

- [ ] **Error Handling:**
  - Invalid inputs handled gracefully: `[error handling test]`
  - Network failures handled appropriately: `[network error test]`
  - User receives helpful error messages: Manual UX review

## Validation Command Reference

Document the specific commands that will be used during implementation:

### Project-Specific Validation Commands:
```bash
# Code Quality (Level 1):
[Your linting command]     # e.g., npm run lint
[Your formatting command]  # e.g., black .
[Your type check command] # e.g., mypy .

# Testing (Level 2):
[Your unit test command]   # e.g., pytest tests/
[Your coverage command]    # e.g., npm run test:coverage

# Integration (Level 3):
[Your integration command] # e.g., npm run test:integration
[Your e2e test command]   # e.g., npm run test:e2e

# Feature Complete (Level 4):
[Your full test suite]    # e.g., npm test
[Your health check]       # e.g., curl localhost:3000/health
```

### Custom Validation for This Feature:
```bash
# Feature-specific validation commands will be added here
# based on the specific requirements of this feature
```
```

## Updated PRD Generation Process

When generating PRDs, the AI should:

1. **Create Standard PRD Sections** (as existing)
2. **Add Executable Success Criteria Section** (new)
3. **Include Validation Command Reference** (new)
4. **Cross-Reference User Stories with Validation Steps** (enhanced)

This ensures that every PRD includes clear, testable criteria that can be systematically validated during the task execution phase, creating a tight feedback loop between requirements and implementation validation.

## Final instructions

1.  Do NOT start implementing the PRD.
2.  Begin by asking me clarifying questions.
3.  After I answer, take my answers and generate the complete PRD.

## PRD Enhancement for Task Master Integration

**If the user mentions using Claude Task Master for task generation**, ensure your PRD includes:
- Clear dependency relationships between features
- Complexity indicators for features that may need breakdown
- Structured acceptance criteria that Task Master can parse effectively
- Feature scope clearly defined to support automatic task generation

**This enhanced structure supports both:**
- Standard manual task generation (Step 4 of our workflow)
- Enhanced Task Master `parse_prd` automation

**The PRD format remains the same** - these enhancements are about clarity and structure that benefits both approaches.