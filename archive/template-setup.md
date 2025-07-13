# Project Setup

One-time project workspace setup after creating project from ai-new-project-template.

## Command Purpose

Run **once only** after creating and cloning a project from the ai-new-project-template to convert scaffolding into a clean project workspace. Includes template remote configuration, file transformation, and safety checks to prevent accidental re-execution.

## Execution Process

### Phase 1: Safety Validation

First, check if this project has already been set up:

```bash
# Check for scaffolding directory (indicates fresh template)
if [ ! -d "_project-scaffolding/" ]; then
    echo "❌ This project appears to already be set up."
    echo ""
    echo "🔍 Current project state:"
    ls -la | grep -E "(README\.md|TODO\.md|\.project-docs)"
    echo ""
    echo "💡 Next steps:"
    echo "   • Use /orient to check your current state"
    echo "   • Use /start-coding to develop features"
    echo "   • Get template updates: git pull template main"
    exit 1
fi

echo "✅ Fresh template detected - proceeding with setup..."
```

### Phase 2: Smart Git Configuration

Configure git remotes properly for template workflow with template updates:

```bash
echo "🔧 Configuring git for template updates..."

# Check current git status
CURRENT_REMOTE=$(git remote get-url origin 2>/dev/null || echo "none")
echo "   📡 Current origin: $CURRENT_REMOTE"

# Add template remote to original template (if not already exists)
if ! git remote get-url template 2>/dev/null; then
    echo "   🔗 Adding template remote for template updates..."
    git remote add template https://github.com/petergiordano/ai-new-project-template.git
    echo "   ✅ Template remote added: ai-new-project-template"
else
    echo "   ✅ Template remote already configured"
fi

# Verify remote configuration
echo "   📋 Git remote configuration:"
git remote -v | sed 's/^/      /'

# Fetch template to enable template updates
echo "   ⬇️  Fetching template for future updates..."
git fetch template --quiet
echo "   ✅ Template update capability configured"
```

### Phase 3: File Management Operations

Execute these file operations in order:

1. **Copy scaffolding contents to project root:**
   ```bash
   echo "📁 Setting up project workspace..."
   
   # Copy essential scaffolding directories to root
   cp -r "_project-scaffolding/.ai-rules" ".ai-rules"
   echo "   ✅ Copied .ai-rules/ (AI workflow instructions)"
   
   cp -r "_project-scaffolding/.project-docs" ".project-docs"
   echo "   ✅ Copied .project-docs/ (planning templates)"
   
   # Note: .claude/ is already at root level in template for immediate access
   echo "   ✅ .claude/ (Claude Code commands already available)"
   
   # Create src directory if it doesn't exist
   mkdir -p "src"
   echo "   ✅ Created src/ (source code directory)"
   
   # Transform specific project files
   cp "_project-scaffolding/README-project-template.md" "README.md"
   cp "_project-scaffolding/TODO-template.md" "TODO.md"
   echo "   ✅ Created README.md (project-focused)"
   echo "   ✅ Created TODO.md (project task tracking)"
   ```

2. **Clean up scaffolding directory only:**
   ```bash
   echo "🧹 Cleaning up scaffolding..."
   # Remove scaffolding directory (contents now copied to root)
   rm -rf "_project-scaffolding/"
   echo "   ✅ Removed _project-scaffolding/ (contents copied to root)"
   
   # Keep setup-claude-chat-ai/ directory for user to configure Chat AI Strategist
   echo "   ✅ Preserved setup-claude-chat-ai/ (Chat AI setup instructions)"
   
   # Keep all other template files for template merging capability
   echo "   ✅ Preserved template files (enables template updates)"
   ```

3. **Commit the project setup:**
   ```bash
   echo "💾 Creating setup commit..."
   git add README.md TODO.md .ai-rules/ .project-docs/ src/
   git add -u  # Add removal of _project-scaffolding/
   git commit -m "feat: convert template to project workspace

- Copy .ai-rules/, .project-docs/ to root
- Transform README-project-template.md → README.md
- Transform TODO-template.md → TODO.md
- Create src/ directory for source code
- Remove _project-scaffolding/ (contents copied)
- Configure template remote for updates
- .claude/ already available at root for immediate command access

Template source: $(git remote get-url template)
Setup date: $(date '+%Y-%m-%d %H:%M:%S')"
   echo "   ✅ Project setup committed to git history"
   ```

### Phase 4: Template Update Instructions & Success Message

```bash
echo ""
echo "🎉 Project workspace setup complete!"
echo ""
echo "📁 Your clean project structure:"
echo "   ✅ README.md (your project documentation)"
echo "   ✅ TODO.md (development task tracking)"  
echo "   ✅ AI_CONTEXT.md (ready for project context)"
echo "   ✅ .ai-rules/ (workflow instructions)"
echo "   ✅ .project-docs/ (planning templates)"
echo "   ✅ .claude/ (Claude Code commands)"
echo "   ✅ src/ (source code directory)"
echo "   📋 setup-claude-chat-ai/ (Chat AI setup instructions)"
echo "   🔗 Git remotes configured (origin + template)"
echo ""
echo "🔄 Template Update Capability:"
echo "   📡 Origin: $(git remote get-url origin)"
echo "   🔗 Template: $(git remote get-url template)"
echo "   💡 Get updates anytime: git pull template main"
echo ""
echo "🚀 Your Development Journey:"
echo ""
echo "   1. ✅ Use template on GitHub → your-username/your-project-name"
echo "   2. ✅ Clone YOUR repository → local development"
echo "   3. ✅ /setup-project (workspace setup + template remote) ← YOU ARE HERE"
echo "   4. 🔄 Setup Chat AI Strategist (see setup-claude-chat-ai/)"
echo "   5. 🔄 /start-coding (foundation → PRD → tasks → implementation)"
echo "   6. 🔄 /start-coding (next feature: PRD → tasks → implementation)"
echo "   7. 🧭 /orient (anytime navigation)"
echo ""
echo "💡 Next Steps:"
echo "   • RECOMMENDED: Set up Chat AI Strategist (see setup-claude-chat-ai/)"
echo "   • Run /start-coding to begin feature development"
echo "   • Run /orient anytime to check current state"
echo ""
echo "🔄 Getting Template Updates:"
echo "   • New AI rules: git pull template main"
echo "   • Enhanced commands: git pull template main"  
echo "   • Workflow improvements: git pull template main"
echo "   • Resolve conflicts to keep your customizations"
echo ""
echo "Ready to start building with continuous template updates! 🚀"
```

## Template Update Workflow

### **How Users Get Template Updates:**

1. **Automatic upstream configuration** - `/setup-project` adds upstream remote
2. **Simple update command** - `git pull upstream main` 
3. **Smart conflict resolution** - Git preserves user customizations
4. **Selective updates** - Users can review changes before merging

### **What Gets Updated:**
- **AI rule files** (`.ai-rules/`) - Improved workflow instructions
- **Command enhancements** (`.claude/commands/`) - Better automation
- **Template files** (`.project-docs/`) - Enhanced planning documents
- **Documentation** (`WORKFLOW_GUIDE.md`) - Latest best practices

### **What Stays Custom:**
- **Project files** (`README.md`, `TODO.md`) - User's specific content
- **Source code** (`src/`) - User's application
- **Project context** (`AI_CONTEXT.md`) - User's project specifics
- **Tasks and PRDs** (`tasks/`) - User's feature work

### **Conflict Resolution Example:**
```bash
# User gets template updates
git pull upstream main

# If conflicts exist, git will prompt
# User resolves conflicts keeping their customizations
# Template improvements merge with user's project
```

## Safety Features

### **Prevents Double Execution**
- Checks for `_project-scaffolding/` directory existence
- Clear error message if already setup
- Guides user to appropriate next commands including update instructions

### **Git Safety & Fork Preservation**
- **Preserves fork relationship** - Keeps connection to user's GitHub repo
- **Adds upstream remote** - Enables template updates via upstream
- **Maintains git history** - Proper fork lineage for GitHub
- **Smart remote detection** - Verifies and reports git configuration

### **Template Update Safety**
- **Preserves user changes** - Git merge respects customizations
- **Clear update instructions** - Users know exactly how to get updates
- **Conflict resolution** - Standard git workflow for handling conflicts
- **Selective updates** - Users can review before accepting changes

### **Enhanced State Detection**
When already setup, shows current project state and update capability:
```
❌ This project appears to already be set up.

🔍 Current project state:
-rw-r--r--  README.md
-rw-r--r--  TODO.md
drwxr-xr-x  .project-docs

💡 Next steps:
   • Use /orient to check your current state
   • Use /start-coding to develop features  
   • Get template updates: git pull upstream main
```

## Error Handling

### **Git Configuration Validation**
```bash
# Verify git repository exists
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository"
    echo "Make sure you cloned your fork: git clone [your-fork-url]"
    exit 1
fi

# Verify we're in a fork (has origin remote)
if ! git remote get-url origin 2>/dev/null; then
    echo "❌ Error: No origin remote found" 
    echo "Make sure you cloned your fork properly"
    exit 1
fi
```

### **Template Remote Handling**
```bash
# Safe template remote addition
if ! git remote get-url template 2>/dev/null; then
    git remote add template https://github.com/petergiordano/ai-new-project-template.git
    echo "✅ Template remote added"
else
    echo "ℹ️ Template remote already exists"
fi

# Verify template fetch capability
if ! git fetch template --dry-run 2>/dev/null; then
    echo "⚠️ Warning: Could not fetch from template"
    echo "Template updates may not work - check internet connection"
fi
```

### **File Operation Validation**
```bash
# Verify file transformation succeeded
if [ ! -f "README.md" ] || [ ! -f "TODO.md" ]; then
    echo "❌ Error: File transformation failed"
    echo "Check file permissions and template integrity"
    exit 1
fi

# Verify scaffolding cleanup
if [ -d "_project-scaffolding/" ]; then
    echo "⚠️ Warning: Scaffolding directory still exists"
    echo "Setup may be incomplete"
fi
```

### **Recovery Guidance**
If setup fails or user needs template updates:
```
🔄 Template Update Recovery:
1. Check remotes: git remote -v
2. Add template if missing: git remote add template [template-url] 
3. Fetch updates: git fetch template
4. Merge updates: git pull template main
5. Resolve conflicts keeping your customizations
```

## Command Positioning

### **Template-Aware Setup Command**
- Works with GitHub template-created repositories
- Configures template remote for continuous template improvements
- Maintains git history for proper project lineage
- **Enables template evolution inheritance**

### **Workflow Integration**
```
User journey:
Use template → Clone YOUR repository → cd your-project → /setup-project → /start-coding
                                                        ↓
                                            Configures template updates
```

### **Template Evolution Support**
- **`/setup-project`** = One-time workspace preparation + upstream configuration
- **`git pull upstream main`** = Get latest template improvements
- **`/start-coding`** = Feature development workflow (Steps 1-5)
- **`/orient`** = Navigation and state checking

## Key Benefits

### **Continuous Template Improvement**
- Users get AI rule enhancements automatically
- Command improvements flow to existing projects  
- Workflow optimizations benefit all users
- Bug fixes reach users without manual intervention

### **Professional Git Workflow**
- Proper fork relationship maintained
- GitHub integration preserved
- Standard open-source contribution model
- Clean git history with template attribution

### **User Customization Protection**
- Project-specific files remain untouched by updates
- Git merge preserves user modifications
- Conflict resolution for overlapping changes
- User maintains full control over their project