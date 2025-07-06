# AI-Assisted Project Template

### **Purpose: A streamlined workflow for developing with AI assistance.**

This repository is a template for starting new software projects using a structured, AI-assisted workflow. It provides a simple command-driven process that guides you from project idea to implementation.

## 🚀 Getting Started (2 minutes)

### **Step 1: Use This Template**

**Create your project repository on GitHub:**

1. **Use this template:**
   - Click the **"Use this template"** button at the top of this GitHub page
   - Choose **"Create a new repository"**
   - Select your GitHub account as the owner
   - Name your repository (this becomes your project name)
   - Choose public or private as needed
   - Click **"Create repository"**

2. **Clone YOUR new repository locally:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-PROJECT-NAME.git
   cd YOUR-PROJECT-NAME
   ```

3. **Open in VS Code:**
   ```bash
   code .
   ```
4. **Save workspace for your project:**
   - In VS Code: File → Save Workspace As...
   - Name it: `your-project-name.code-workspace` (e.g., `test2.code-workspace`)
   - Save it in your project root directory
   - When prompted, choose "Open Workspace"
  
5. **Import Claude Desktop MCP Servers:**
   - Do this on the terminal, NOT within Claude Code!
```bash
claude mcp add-from-claude-desktop
```

### **Step 2: Essential Setup**

**Open terminal in VS Code and run these commands:**

```bash
# Start Claude Code CLI (make sure you're in YOUR project directory)
claude

# Set up your project workspace (one-time only)
/project-setup

# Begin feature development 
/start-coding
```

**What `/project-setup` does for you:**
1. **Validates workspace safety** - Checks if setup was already completed to prevent double-execution
2. **Configures git remotes** - Adds template remote pointing to `ai-new-project-template` for inheriting updates
3. **Copies essential workflow files** - Moves `.ai-rules/` and `.project-docs/` from scaffolding to your project root (`.claude/` already available for immediate use)
4. **Creates project documentation** - Transforms template files into your project's `README.md` and `TODO.md`
5. **Sets up source directory** - Creates `src/` folder for your application code
6. **Cleans up scaffolding** - Removes `_project-scaffolding/` directory (contents now in proper locations)
7. **Commits setup changes** - Creates a clean git commit documenting the workspace transformation
8. **Enables template inheritance** - Shows you can now get template improvements with `git pull template main`

**✅ Benefits of Template Approach:**
- **Clean GitHub workflow** - Purpose-built for template usage
- **Template inheritance** - Get improvements via template remote
- **Independent repository** - Your project owns its own git history
- **Professional setup** - GitHub's recommended template pattern

## 🎯 Complete User Journey

```
1. Use template on GitHub → your-username/your-project-name
2. Clone YOUR repository → local development
3. cd your-project-name (CRITICAL!)
4. /project-setup (one-time workspace setup + template remote)
5. Setup Chat AI Strategist (recommended)
6. /start-coding (foundation → PRD → tasks → implementation)
7. /start-coding (next feature: PRD → tasks → implementation)
8. /orient (anytime navigation)
```

### **What Each Command Does:**

- **`/project-setup`** - Transform template files, configure template remote, setup workspace
- **`/start-coding`** - Intelligent feature development orchestrator  
- **`/orient`** - Check current state and get guidance anytime

## 🧠 How It Works

### **3-Party Collaboration Model**
- **You:** Project director making decisions
- **Chat AI:** Strategic planning and context preparation
- **CLI AI:** Technical implementation and file operations

### **5-Step Workflow (Automated)**
1. **Project Foundation** - AI interview creates project context
2. **Dynamic Context** - Automatic context loading for AI assistants  
3. **Feature Planning** - PRD creation with validation criteria
4. **Task Generation** - Detailed implementation breakdown
5. **Quality Implementation** - Code execution with progressive validation

## 📂 Template Structure

After `/setup-project`, your workspace will look like:

```
your-project/
├── .claude/                    # Claude Code configuration
├── .ai-rules/                  # AI workflow instructions
├── .project-docs/              # Project planning documents
├── src/                        # Your application source code
├── tasks/                      # Feature PRDs and task lists
├── setup-claude-chat-ai/       # Chat AI Strategist setup instructions
├── README.md                   # Your project's README (this gets replaced)
├── TODO.md                     # Development task tracking
├── AI_CONTEXT.md              # AI assistant briefing
└── WORKFLOW_GUIDE.md          # Complete workflow documentation
```

## ⚡ Advanced Features

- **Template Inheritance** - Pull improvements from template via `git pull template main`
- **Smart State Detection** - Commands know where you are in the workflow
- **Progressive Validation** - 4-level quality gates prevent error accumulation
- **Context Engineering** - AI assistants get comprehensive project context
- **Plan Mode Integration** - Safe exploration with Claude Code CLI
- **Multi-Feature Support** - Handle multiple features in same project
- **Recovery Handling** - Resume work after interruptions
- **Clean Git Workflow** - Template → develop → independent project evolution

## 🔄 Getting Template Updates

### **Pull Latest Template Improvements:**
```bash
# Your /project-setup command configures this automatically
git pull template main

# Resolve any conflicts with your project-specific changes
# Your project customizations remain intact
```

**Benefits:**
- Get new AI rules and workflow improvements
- Enhanced commands and better error handling  
- New features and capabilities added to template
- Maintain your project's custom changes

## 🆘 Need Help?

### **Common Questions:**

**"What if I mess something up?"**
- Use `/orient` to check current state
- Commands include recovery guidance
- GitHub fork makes it easy to reset: re-clone your fork

**"Can I use different AI assistants?"**
- Yes! Works with Claude, ChatGPT, Gemini
- Template provides context for any AI assistant
- CLI AI gets automatic project context

**"How do I add multiple features?"**
- Run `/start-coding` for each new feature
- System tracks multiple PRDs and task lists
- Maintains project-wide context

**"I'm getting git errors or wrong directory issues"**
- Make sure you're in YOUR project directory: `pwd`
- Should show `your-project-name`, not `ai-new-project-template`
- Run `/project-setup` to fix workspace configuration
- Check GitHub remote: `git remote -v` should show YOUR repository + template

**"How do I get template updates?"**
- Use `git pull template main` to get latest improvements
- `/project-setup` configures template remote automatically
- Resolve conflicts to keep your customizations

### **If You Get Stuck:**
1. Try `/orient` for current state and next steps
2. Check `WORKFLOW_GUIDE.md` for detailed explanations
3. Ensure you're in YOUR project directory: `pwd`
4. Verify git remotes: `git remote -v` (should show your repository + template)
5. Create fresh repository from template if needed

## 📚 Learn More

- **Complete Guide:** See `WORKFLOW_GUIDE.md` for detailed workflow
- **AI Instructions:** Explore `.ai-rules/` for AI command details
- **Context Engineering:** Built on proven AI collaboration principles
- **Template Evolution:** This template continuously improves - use template updates to benefit!

---

**Ready to build? Use Template → Clone → `/project-setup` → `/start-coding`**

## 🎯 Why This Template Works

### **Context Engineering Excellence**
- AI assistants get comprehensive project context automatically
- Context accumulates across workflow steps for consistency
- Eliminates repetitive explanations and reduces errors

### **Professional Development Workflow**  
- GitHub template pattern follows recommended practices
- Independent repository ownership
- Clean git history focused on your project

### **Simple, Lovable, Complete Framework**
- **Simple:** One command to start, clear next steps always
- **Lovable:** Delightful AI collaboration, minimal friction
- **Complete:** Production-ready implementations, not prototypes

**Start building with AI assistance that actually works.**