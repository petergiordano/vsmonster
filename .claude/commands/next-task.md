# Get Next Task and Create Implementation Plan

Read Notion database, select next available task, and create development plan.

## Steps:
1. Query Notion database (22f859c6-e596-8007-86c6-c1df9f865855) for tasks with Status: "New" or "Critical"
2. Consider all phases but prioritize by development readiness 
3. Select highest priority task (Critical > New, earliest due date)
4. Update task Status to "In Progress"
5. Display task details and create implementation plan:
   - File paths to create/modify
   - Step-by-step development approach
   - Testing strategy
   - Acceptance criteria

## Output Format:
**Selected Task:** VSM-XX - [Task Name]
**Files to work on:** [list]
**Implementation plan:** [numbered steps]
**Ready to start development**