# TODO: versusMonster AVPS

**Current Phase:** Component 2 (Voice Generation)  
**Status:** 1 of 8 components complete  
**Objective:** Generate first complete audio podcast episode

---

## 🎯 Task Management

**All individual tasks are now managed in Notion:**
- **Database:** vmonster-dev-backlog  
- **Database ID:** `22f859c6-e596-8007-86c6-c1df9f865855`
- **Schema File:** `/notion-database-schema.json` (for Claude Code integration)
- **Task Count:** 30 granular tasks imported from previous TODO.md

### Current Sprint Focus (Critical Path)
1. **VSM-6:** Add ElevenLabs API key to .env file (Critical)
2. **VSM-7:** Implement ElevenLabs API client wrapper
3. **VSM-8:** Create character voice mapping - THORAK
4. **VSM-9:** Create character voice mapping - ZARA
5. **VSM-10:** Build voice direction processor

### Key Views in Notion
- **Current Sprint** - Active development tasks
- **Critical Tasks** - Immediate blockers
- **Testing Phase** - Quality assurance items
- **By Phase** - Organized by development phase

---

## 📅 Component Progress

### ✅ Component 1: Script Parser (Complete)
- Completed 2025-01-08 with 100% Episode 7 validation
- Command: `python parser.py episode_2_ex_final.md`
- Output: `output/json/episode_2_ex_final.json`

### 🔄 Component 2: Voice Generation (In Progress)
- **Notion Tasks:** VSM-6 through VSM-30
- **Target Command:** `python voice_gen.py episode_2_ex_final.json`
- **Expected Output:** 69 voice files in `output/voices/`
- **Success Criteria:** Processing in <5 minutes, all dialogues converted

### 📋 Components 3-8: Upcoming
- Component 3: Audio Assembly
- Component 4: Static Video  
- Components 5-8: Production & Automation

---

## 🔧 Development Workflow

### For Claude Code CLI
1. **Read schema:** `notion-database-schema.json`
2. **Update tasks:** Use Notion MCP integration
3. **Track progress:** Update Status and Phase fields
4. **Link code:** Use Relevant Code File Path field

### Commands Reference
```bash
# Development
python parser.py episode_2_ex_final.md          # Component 1 (Complete)
python voice_gen.py episode_2_ex_final.json     # Component 2 (Target)

# Testing
pytest tests/ -v --cov=src
black src/ --check
flake8 src/
mypy src/
```

### Key Files
- `/PRD.md` - Master requirements
- `/AI_CONTEXT.md` - Development context  
- `/notion-database-schema.json` - Database schema for Claude Code
- `output/json/episode_2_ex_final.json` - Parser output
- `output/voices/` - Voice generation target

---

## 📚 Project Context

### Objectives
- **Target:** 104 episodes/year
- **Budget:** <$10/episode ($3.06 for voice generation)
- **Performance:** <30min/episode processing time

### Resources
- **Primary Test Case:** Episode 7
- **Completed Work:** See `archive/COMPLETED_TASKS.md`
- **Documentation:** All tasks and progress tracked in Notion

---

**Last Updated:** 2025-07-13  
**Task Management:** Migrated to Notion Database (vmonster-dev-backlog)