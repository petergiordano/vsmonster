# Update PRD Component Status

Automatically sync Notion task completion status with PRD.md component progress.

## Steps:
1. Query Notion database for all tasks by component (VSM task ranges)
2. Calculate completion percentages for each component:
   - Component 1: VSM-1 to VSM-6 (Script Parser)
   - Component 2: VSM-31 to VSM-39 (Voice Generation) 
   - Component 3: VSM-40+ (Future components)
3. Update PRD.md "Component Status" section with current progress
4. Add validation timestamps for completed components
5. Update "Current Status" section in PRD
6. Commit changes: "Auto-update PRD.md component status from Notion"

## Component Status Format:
```markdown
### Component Status (Auto-Updated: 2025-07-13)
- **Component 1**: ✅ COMPLETE (2025-01-08) - Script Parser validated with Episode 7
- **Component 2**: 🚧 IN PROGRESS (3/9 tasks) - Voice Generation: ElevenLabs integration
- **Component 3**: 📝 PLANNED - Audio Assembly (pending Component 2)
```

## Validation Commands Added:
For completed components, add validation section:
```markdown
#### Component X Validation
```bash
python component_command.py episode_007.json
```
**Last Validated:** 2025-07-XX ✅ **Status:** All success criteria met
```

## Output Format:
**PRD Updated:** Component status, validation commands, current phase
**Commit:** Auto-generated with Notion sync reference