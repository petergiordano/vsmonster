# versusMonster AVPS (Automated Video Podcast System)

**Transform markdown scripts into complete YouTube-ready podcast episodes**

- Repository: https://github.com/petergiordano/vsmonster
- Target: 104 episodes/year (2 episodes/week)
- Philosophy: "Function Over Fashion" - iterative build with compound value

## 🚀 Quick Start

### **Development Workflow**
```bash
# Start Claude Code in project directory
claude

# Get next Notion task and create implementation plan
@next-task

# Complete current task and update Notion
@finalize-task
```

### **Task Management**
- **System**: Notion Database (vmonster-dev-backlog)
- **Schema**: `config/notion-database-schema.json`
- **Commands**: `@next-task`, `@finalize-task`
- **Database ID**: `22f859c6-e596-8007-86c6-c1df9f865855`

---

## 📋 Current Status

**Phase**: Component 2 (Voice Generation)  
**Progress**: 1 of 8 components complete  
**Next Priority**: ElevenLabs API integration

### ✅ Completed
- **Component 1**: Script Parser (100% Episode 7 validation)
- Command: `python parser.py episode_007.md`

### 🔄 In Progress  
- **Component 2**: Voice Generation (VSM-6 through VSM-30)
- Target: `python voice_gen.py episode_007.json`

---

## Architecture: 8-Component Pipeline

Sequential pipeline where each component delivers independent value:

1. **Script Parser** ✅ - Markdown → structured JSON (`parser.py`)
2. **Voice Generation** 🔄 - JSON → character voice files (`voice_gen.py`) 
3. **Audio Assembly** 📝 - Voice files → complete audio track
4. **Static Video** 📝 - Audio + image → YouTube video
5. **Image Transitions** 📝 - Multiple images → dynamic video
6. **Sound Effects** 📝 - Add SFX layer
7. **Background Music** 📝 - Complete audio production
8. **Batch Processing** 📝 - Automate multiple episodes

## Commands Reference

```bash
# Current components
python parser.py episode_007.md          # Component 1 (Complete)
python voice_gen.py episode_007.json     # Component 2 (Target)

# Development
@next-task                               # Get next Notion task
@finalize-task                          # Complete and update Notion
@orient                                 # Check current state

# Testing
pytest tests/ -v --cov=src
black src/ --check
flake8 src/
```

## Getting Started

### Prerequisites
- Python 3.11+
- FFmpeg (via Homebrew)
- ElevenLabs API key
- Virtual environment

### Installation
```bash
# Clone and setup
git clone https://github.com/petergiordano/vsmonster.git
cd vsmonster
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Add your ELEVENLABS_API_KEY to .env
```

### Usage
```bash
# Process Episode 7 (reference implementation)
python parser.py scripts/episode_007.md
# Output: output/json/episode_007.json

# Next: Voice generation (in development)
python voice_gen.py output/json/episode_007.json
# Target: output/voices/ with 69 voice files
```

---

## Project Structure (After Setup)

After running `/setup-project`, your workspace becomes:

```
[project-name]/
├── docs/                   # Project documentation
│   ├── architecture/       # Project foundation documents  
│   ├── specifications/     # Technical specifications
│   └── setup/              # Development setup guides
├── config/                 # Configuration files
├── src/                    # Source code
├── tasks/                  # Feature PRDs and task lists
├── tests/                  # Test files
├── setup-claude-chat-ai/   # Chat AI Strategist setup (optional)
├── .ai-context/           # AI assistant documentation
│   ├── AI_CONTEXT.md      # Master project context file
│   └── WORKFLOW_GUIDE.md  # Multi-agent workflow guide
├── README.md              # This file - project documentation
├── TODO.md                # Development task tracking
├── WORKFLOW_GUIDE.md      # Complete development workflow (template)
```

## Development

### **AI-Assisted Development**

This project uses a structured AI collaboration workflow:

- **Chat AI (Strategy):** Claude/ChatGPT/Gemini for planning and context
- **CLI AI (Implementation):** Claude Code/Gemini CLI for technical execution
- **Progressive Validation:** 4-level quality gates ensure reliable code

### **Adding New Features**

```bash
# Start feature development workflow
/start-coding

# The system will guide you through:
# 1. Feature definition (PRD creation)
# 2. Task breakdown (implementation planning)
# 3. Code execution (with validation)
```

### **Project State Management**

```bash
# Check where you are and what's next
/orient

# Examples of what you might see:
# "Foundation complete → Ready for first feature"
# "PRD exists → Generate task list"
# "Tasks ready → Begin implementation"
```

### Running Tests

```bash
[test commands - will be defined during development]
```

### Building

```bash
[build commands - will be defined during development]
```

## AI Development Context

Your project's AI context is maintained in `.ai-context/AI_CONTEXT.md` and includes:
- Project goals and technical approach
- Coding conventions and architecture patterns
- Dependencies and constraints
- Testing requirements

This context automatically loads when using Claude Code or Gemini CLI.

## Contributing

[How others can contribute to your project]

### For Contributors Using AI Assistance

1. **Read the project context:** Check `.ai-context/AI_CONTEXT.md` and `CLAUDE.md`
2. **Use the workflow:** Follow the `/start-coding` process for new features
3. **Maintain quality:** Leverage the built-in validation systems

## License

[Your license - e.g., MIT, Apache 2.0, etc.]

---

**🎯 Ready to build?** Start with `/setup-project` then `/start-coding`

Built using the AI-Assisted Development Framework for efficient, high-quality development.