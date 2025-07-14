# Complete Task and Update Notion

Mark current in-progress task complete, prepare commit, and sync with Notion.

## Steps:
1. Query Notion database for tasks with Status: "In Progress"
2. If multiple tasks in progress, ask user which to finalize
3. If no tasks in progress, show error message
4. Test implementation (run relevant tests)
5. Generate commit message: "VSM-XX: [brief description]"
6. Show commit command for user to execute
7. After user confirms commit/push:
   - Update Notion task: Status "Done", GitHub link, timestamp
   - Update PRD.md component status automatically
   - Commit PRD.md changes: "Update Component X status - VSM-XX complete"
8. Suggest next available task

## Output Format:
**Commit command:** `git commit -m "VSM-XX: [description]"`
**Push command:** `git push`
**Notion updated:** Task marked complete
**Next task:** VSM-YY is ready