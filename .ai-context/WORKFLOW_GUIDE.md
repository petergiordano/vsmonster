# VSMonster AVPS Development Workflow

### **Purpose: Development workflow for versusMonster AVPS using Notion-based task management**

This document outlines the Notion-based task management system and development process for the versusMonster AVPS (Automated Video Podcast System) project.

---

## 🎯 VSMonster Workflow Overview

VSMonster uses a streamlined Notion-based workflow that replaces complex template systems with production-ready task management.

### **Core Commands**
```bash
@next-task      # Get next priority task from Notion
@finalize-task  # Complete task + update PRD + commit
@update-prd     # Sync Notion progress to PRD.md
@orient         # Check current project state
```

### **Notion Database Integration**
- **Database**: vmonster-dev-backlog
- **Database ID**: `22f859c6-e596-8007-86c6-c1df9f865855`
- **Schema**: `config/notion-database-schema.json`
- **Task Prefix**: VSM-1, VSM-2, etc.
- **PRD Sync**: Auto-updates `docs/specifications/PRD.md`

---

## 🔄 Development Process

### **1. Task Selection**
```bash
@next-task
```
- Queries Notion for Critical/New status tasks
- Prioritizes by component dependencies (Component 2 → 3 → 4...)
- Updates selected task to "In Progress"
- Shows implementation plan with files and approach

### **2. Implementation**
- Follow the implementation plan from `@next-task`
- Use existing validation commands:
  ```bash
  python parser.py episode_007.md    # Component 1 validation
  pytest tests/ -v                   # Unit tests
  black src/ --check                 # Code formatting
  ```

### **3. Task Completion**
```bash
@finalize-task
```
- Tests implementation
- Generates commit message with VSM-XX reference
- Updates Notion task to "Done" with GitHub link
- Auto-updates PRD.md component progress
- Commits PRD changes
- Suggests next available task

---

## 📋 Component-Based Development

### **8-Component Pipeline Progress**
1. **Script Parser** ✅ Complete (VSM-1 to VSM-6)
2. **Voice Generation** 🚧 In Progress (VSM-31 to VSM-39)
3. **Audio Assembly** 📝 Planned (VSM-40+)
4. **Static Video** 📝 Planned
5. **Image Transitions** 📝 Planned
6. **Sound Effects** 📝 Planned
7. **Background Music** 📝 Planned
8. **Batch Processing** 📝 Planned

### **Current Focus: Component 2 (Voice Generation)**
**Critical Tasks:**
- VSM-31: Add ElevenLabs API key to .env
- VSM-32: Implement ElevenLabs SDK wrapper
- VSM-33: Create THORAK voice mapping
- VSM-34: Create ZARA voice mapping
- VSM-35: Build voice direction processor

**Success Criteria:**
```bash
python voice_gen.py episode_007.json
# Target: 69 voice files in output/voices/, <5min processing, $3.06 cost
```

---

## 🔧 Claude Code Integration

### **Context Loading**
Claude Code automatically loads project context via:
- `CLAUDE.md` → `AI_CONTEXT.md` (complete project state)
- `config/notion-database-schema.json` (task management schema)

### **Plan Mode Usage**
Use Plan Mode (Shift+Tab twice) for:
- Complex component integration planning
- Episode 7 structure analysis
- API cost estimation
- Asset library design decisions

### **Validation Commands**
```bash
# Component validation
python parser.py episode_007.md
python voice_gen.py episode_007.json  # Target command

# Code quality
black src/ --check && flake8 src/
pytest tests/ -v --cov=src

# Environment check
python tools/setup_validation.py
```

---

## 📝 PRD Source of Truth

### **Automated PRD Updates**
The `docs/specifications/PRD.md` file serves as definitive source of truth and is automatically maintained:

- **Component Status**: Auto-updated via `@finalize-task`
- **Validation Commands**: Added when components complete
- **Progress Tracking**: Synced from Notion VSM task completion

### **Manual Update Rules**
- **Never Change**: Core requirements, success criteria, architecture
- **Always Update**: Status markers, completion dates, validation results

### **PRD Maintenance Commands**
```bash
@finalize-task     # Completes task + updates PRD component status
@update-prd        # Sync all component progress from Notion
```

---

## 🎯 Success Metrics

### **Component Success Criteria**
Each component must achieve:
1. **Command Execution**: Single command operation (`python component.py episode_007.json`)
2. **Episode 7 Validation**: 100% success with reference test case
3. **Performance**: Meet timing requirements (<5min for voice generation)
4. **Cost**: Stay within budget ($3.06/episode for Component 2)

### **Quality Gates**
1. **Syntax**: Code formatting and linting pass
2. **Unit Tests**: All component tests pass
3. **Integration**: Works with Episode 7 test case
4. **Feature**: Meets all PRD success criteria

---

## 🚀 Quick Start

### **New Development Session**
```bash
cd /Users/petergiordano/Documents/GitHub/vsmonster
claude                    # Start Claude Code with auto-context loading
@next-task               # Get highest priority task
# Implement the task
@finalize-task           # Complete and update everything
```

### **Check Project Status**
```bash
@orient                  # Current state and next steps
@update-prd             # Sync latest Notion progress to PRD
```

### **Component 2 Development**
```bash
@next-task              # Should return VSM-31 (ElevenLabs API key)
# Add API key to .env file
@finalize-task VSM-31   # Complete and move to VSM-32
```

This streamlined workflow eliminates template complexity while maintaining systematic development and automatic progress tracking through Notion integration.
