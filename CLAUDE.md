# Claude Code Context

**Primary Context Source:** Read the complete project context from `AI_CONTEXT.md` - it contains all project-specific guidelines, patterns, and context needed for this project.

## Quick Reference
- **Always read AI_CONTEXT.md completely before starting any work**
- **Project Type:** [Determined from AI_CONTEXT.md Tech Stack section]
- **Key Patterns:** Follow existing patterns in `/src` directory
- **Testing:** All new features require corresponding unit tests
- **File Structure:** Maintain organization defined in AI_CONTEXT.md Section 3

## Claude Code Workflow Integration
1. **Use Plan Mode (Shift+Tab twice)** for complex tasks and initial analysis
2. **Read AI_CONTEXT.md** to understand current project state and active features
3. **Check Section 7** for active features and their current status
4. **Follow established patterns** documented in Section 8 (Known Patterns)
5. **Use validation commands** from Section 11 after each change

## Validation Commands Reference
See `AI_CONTEXT.md Section 11` for complete project-specific validation commands including:
- Level 1: Syntax & Style validation
- Level 2: Unit test execution
- Level 3: Integration testing
- Level 4: Full validation suite

## Context Handoff Protocol
- **From Chat AI:** You should receive context-rich prompts that include relevant sections from AI_CONTEXT.md
- **Confirm Understanding:** Always verify you have adequate context before beginning implementation
- **Update Context:** After completing features, note any new patterns or lessons learned for AI_CONTEXT.md updates

## Key Reminders
- **Never skip validation:** Run validation commands after each significant change
- **Follow existing conventions:** Check AI_CONTEXT.md Section 4 for coding standards
- **Plan before implementing:** Use Plan Mode for architectural decisions
- **Ask for clarification:** If context seems incomplete or unclear
- **Update task progress:** Mark tasks complete and provide commit messages when requested