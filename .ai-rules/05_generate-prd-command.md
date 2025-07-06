# Command: Generate PRD

Create a comprehensive Product Requirements Document (PRD) from user requirements.

## Usage
```
/generate-prd [feature-description]
```

## Process

### Phase 1: Context Loading & Analysis
1. **Enter Plan Mode** (Shift+Tab twice) for safe analysis
2. **Load Project Context:**
   - Read AI_CONTEXT.md for project-specific patterns
   - Review existing codebase structure and conventions
   - Examine similar features for integration patterns
3. **Analyze Requirements:**
   - Parse the feature description provided
   - Identify architectural implications
   - Research relevant documentation and patterns

### Phase 2: Structured Interview
4. **Exit Plan Mode** and conduct clarifying interview based on `.ai-rules/01_create-prd.md`:
   - **Problem/Goal:** "What problem does this feature solve for the user?"
   - **Target User:** "Who is the primary user of this feature?"
   - **Core Functionality:** "What are the key actions a user should perform?"
   - **User Stories:** "Can you provide 2-3 user stories in format: As a [user], I want to [action] so that [benefit]?"
   - **Acceptance Criteria:** "How will we know when this feature is successfully implemented?"
   - **Scope/Boundaries:** "What should this feature NOT do (non-goals)?"
   - **Design/UI:** "Any specific UI/UX requirements or existing patterns to follow?"
   - **Technical Constraints:** "Any integration requirements or technical limitations?"

### Phase 3: PRD Generation
5. **Generate Comprehensive PRD** using this structure:
   ```markdown
   # PRD: [Feature Name]
   
   ## Introduction/Overview
   [Problem statement and feature goal]
   
   ## Goals
   - [Specific, measurable objectives]
   
   ## User Stories
   - **US1:** As a [user], I want to [action] so that [benefit]
   - **US2:** As a [user], I want to [action] so that [benefit]
   
   ## Functional Requirements
   1. The system must [requirement]
   2. The system must [requirement]
   
   ## Non-Goals (Out of Scope)
   - [What this feature will NOT include]
   
   ## Design Considerations
   - [UI/UX requirements, existing patterns to follow]
   
   ## Technical Considerations
   - [Integration points, dependencies, constraints]
   
   ## Success Metrics
   - [How success will be measured]
   
   ## Open Questions
   - [Any remaining clarifications needed]
   ```

6. **Save PRD** as `tasks/prd-[feature-name].md`

## Enhanced PRD Generation (Optional)

**If user has Claude Task Master MCP configured**, you can mention enhanced next steps:

"Your PRD is complete and ready for task generation. You can proceed with:
- **Standard approach:** Use our `/generate-tasks` command for manual task breakdown
- **Enhanced approach:** Use Claude Task Master's `parse_prd` tool for automated task generation with dependency analysis

Both approaches work with the PRD I've created. Which would you prefer?"

## Command-Driven Benefits
- **Clear Phase Boundaries:** Explicit Plan Mode usage for analysis
- **Context Convergence:** Multiple context sources feed into PRD creation
- **Human Approval Gate:** User reviews PRD before proceeding to task generation
- **Streamlined Transition:** Ready for `/generate-tasks` command

## Next Step
After PRD is approved, user can run: `/generate-tasks tasks/prd-[feature-name].md`