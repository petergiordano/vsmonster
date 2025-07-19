#!/bin/bash

# AI-Powered Development Cycle - Project Initialization Script
# This script sets up the complete AI development workflow in a new project

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to prompt for user input with default
prompt_with_default() {
    local prompt="$1"
    local default="$2"
    local var_name="$3"
    
    echo -n "$prompt [$default]: "
    read -r input
    if [[ -z "$input" ]]; then
        eval "$var_name='$default'"
    else
        eval "$var_name='$input'"
    fi
}

# Function to validate required tools
check_dependencies() {
    print_status "Checking required dependencies..."
    
    local missing_tools=()
    
    # Check for git
    if ! command -v git &> /dev/null; then
        missing_tools+=("git")
    fi
    
    # Check for VS Code (optional but recommended)
    if ! command -v code &> /dev/null; then
        print_warning "VS Code not found. Some features may not work optimally."
    fi
    
    if [[ ${#missing_tools[@]} -gt 0 ]]; then
        print_error "Missing required tools: ${missing_tools[*]}"
        print_error "Please install missing tools and try again."
        exit 1
    fi
    
    print_success "All required dependencies found"
}

# Function to collect project information
collect_project_info() {
    print_status "Collecting project information..."
    echo
    
    # Get current directory name as default project name
    current_dir=$(basename "$PWD")
    
    prompt_with_default "Project name" "$current_dir" PROJECT_NAME
    prompt_with_default "Project description" "AI-powered automated system" PROJECT_DESCRIPTION
    prompt_with_default "Primary programming language" "python" PRIMARY_LANGUAGE
    prompt_with_default "Number of pipeline components" "6" COMPONENT_COUNT
    
    # Convert project name to valid identifier
    PROJECT_ID=$(echo "$PROJECT_NAME" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/_/g')
    
    echo
    print_status "Project Configuration:"
    echo "  Name: $PROJECT_NAME"
    echo "  ID: $PROJECT_ID"
    echo "  Description: $PROJECT_DESCRIPTION"
    echo "  Language: $PRIMARY_LANGUAGE"
    echo "  Components: $COMPONENT_COUNT"
    echo
    
    echo -n "Proceed with this configuration? [Y/n]: "
    read -r confirm
    if [[ "$confirm" =~ ^[Nn]$ ]]; then
        print_error "Initialization cancelled by user"
        exit 1
    fi
}

# Function to set up directory structure
setup_directory_structure() {
    print_status "Setting up project directory structure..."
    
    # Create standard directories if they don't exist
    mkdir -p src tests config docs/implementation-logs
    
    # Language-specific setup
    case "$PRIMARY_LANGUAGE" in
        python)
            mkdir -p src/utils tests/unit tests/integration
            if [[ ! -f "requirements.txt" ]]; then
                touch requirements.txt
            fi
            if [[ ! -f "pyproject.toml" ]]; then
                cat > pyproject.toml << EOF
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "$PROJECT_ID"
version = "0.1.0"
description = "$PROJECT_DESCRIPTION"
readme = "README.md"
requires-python = ">=3.8"
dependencies = []

[tool.black]
line-length = 88
target-version = ['py38']

[tool.isort]
profile = "black"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
EOF
            fi
            ;;
        javascript|node|nodejs)
            mkdir -p src/utils tests/unit tests/integration
            if [[ ! -f "package.json" ]]; then
                cat > package.json << EOF
{
  "name": "$PROJECT_ID",
  "version": "0.1.0",
  "description": "$PROJECT_DESCRIPTION",
  "main": "src/index.js",
  "scripts": {
    "test": "jest",
    "lint": "eslint src/",
    "format": "prettier --write src/"
  },
  "devDependencies": {
    "jest": "^29.0.0",
    "eslint": "^8.0.0",
    "prettier": "^2.0.0"
  },
  "dependencies": {}
}
EOF
            fi
            ;;
        go)
            mkdir -p cmd pkg internal tests
            if [[ ! -f "go.mod" ]]; then
                go mod init "$PROJECT_ID" 2>/dev/null || true
            fi
            ;;
        *)
            print_warning "Unknown language '$PRIMARY_LANGUAGE', using generic structure"
            ;;
    esac
    
    print_success "Directory structure created"
}

# Function to customize templates
customize_templates() {
    print_status "Customizing templates for your project..."
    
    # Get current date
    current_date=$(date +"%Y-%m-%d")
    
    # Customize PRD template
    if [[ -f "docs/specifications/PRD_TEMPLATE.md" ]]; then
        sed -i.bak \
            -e "s/\[PROJECT NAME\]/$PROJECT_NAME/g" \
            -e "s/\[DATE\]/$current_date/g" \
            docs/specifications/PRD_TEMPLATE.md
        mv docs/specifications/PRD_TEMPLATE.md docs/specifications/PRD.md
        rm docs/specifications/PRD_TEMPLATE.md.bak
    fi
    
    # Customize AI Context template
    if [[ -f ".ai-context/AI_CONTEXT_TEMPLATE.md" ]]; then
        sed -i.bak \
            -e "s/\[PROJECT NAME\]/$PROJECT_NAME/g" \
            -e "s/\[DATE\]/$current_date/g" \
            .ai-context/AI_CONTEXT_TEMPLATE.md
        mv .ai-context/AI_CONTEXT_TEMPLATE.md .ai-context/AI_CONTEXT.md
        rm .ai-context/AI_CONTEXT_TEMPLATE.md.bak
    fi
    
    # Create basic config file
    if [[ ! -f "config/project-config.json" ]]; then
        cat > config/project-config.json << EOF
{
  "project": {
    "name": "$PROJECT_NAME",
    "id": "$PROJECT_ID",
    "description": "$PROJECT_DESCRIPTION",
    "language": "$PRIMARY_LANGUAGE",
    "component_count": $COMPONENT_COUNT
  },
  "development": {
    "test_command": "$(get_test_command)",
    "lint_command": "$(get_lint_command)",
    "format_command": "$(get_format_command)"
  },
  "ai_workflow": {
    "enabled": true,
    "reference_test_case": "tests/reference/",
    "validation_required": true
  }
}
EOF
    fi
    
    print_success "Templates customized for $PROJECT_NAME"
}

# Helper functions for language-specific commands
get_test_command() {
    case "$PRIMARY_LANGUAGE" in
        python) echo "pytest tests/ -v" ;;
        javascript|node|nodejs) echo "npm test" ;;
        go) echo "go test ./..." ;;
        *) echo "# Add your test command here" ;;
    esac
}

get_lint_command() {
    case "$PRIMARY_LANGUAGE" in
        python) echo "flake8 src/" ;;
        javascript|node|nodejs) echo "eslint src/" ;;
        go) echo "golint ./..." ;;
        *) echo "# Add your lint command here" ;;
    esac
}

get_format_command() {
    case "$PRIMARY_LANGUAGE" in
        python) echo "black src/" ;;
        javascript|node|nodejs) echo "prettier --write src/" ;;
        go) echo "gofmt -w ." ;;
        *) echo "# Add your format command here" ;;
    esac
}

# Function to set up git repository
setup_git_repository() {
    print_status "Setting up git repository..."
    
    # Initialize git if not already done
    if [[ ! -d ".git" ]]; then
        git init
        print_success "Git repository initialized"
    else
        print_warning "Git repository already exists"
    fi
    
    # Create .gitignore if it doesn't exist
    if [[ ! -f ".gitignore" ]]; then
        cat > .gitignore << EOF
# Language-specific ignores
$(get_gitignore_patterns)

# Development tools
.vscode/
.idea/
*.swp
*.swo
*~

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Environment and secrets
.env
.env.local
.env.*.local
*.key
*.pem

# Logs and databases
*.log
*.sqlite
*.db

# Temporary files
tmp/
temp/
.tmp/
EOF
        print_success "Created .gitignore file"
    fi
    
    # Create initial commit if no commits exist
    if ! git rev-parse --verify HEAD &> /dev/null; then
        git add .
        git commit -m "Initial commit: AI-powered development workflow setup

- Configured project structure for $PROJECT_NAME
- Set up AI coordination templates and documentation
- Initialized $PRIMARY_LANGUAGE development environment
- Created $COMPONENT_COUNT-component pipeline architecture

🤖 Generated with AI Development Cycle Template"
        print_success "Initial commit created"
    fi
}

get_gitignore_patterns() {
    case "$PRIMARY_LANGUAGE" in
        python) cat << 'EOF'
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.pytest_cache/
.coverage
htmlcov/
.mypy_cache/
.dmypy.json
dmypy.json
EOF
            ;;
        javascript|node|nodejs) cat << 'EOF'
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.npm
.eslintcache
.yarn-integrity
.env.local
.env.development.local
.env.test.local
.env.production.local
coverage/
.nyc_output/
EOF
            ;;
        go) cat << 'EOF'
*.exe
*.exe~
*.dll
*.so
*.dylib
*.test
*.out
go.work
EOF
            ;;
        *) echo "# Add language-specific ignores here" ;;
    esac
}

# Function to create README
create_readme() {
    if [[ ! -f "README.md" ]]; then
        print_status "Creating README.md..."
        
        cat > README.md << EOF
# $PROJECT_NAME

$PROJECT_DESCRIPTION

## Overview

This project implements an AI-powered development workflow with a $COMPONENT_COUNT-component pipeline architecture. It follows the Simple, Lovable, Complete (SLC) design principles and uses AI assistants for development coordination.

## Architecture

### Component Pipeline
1. **Component 1**: [Customize: Brief description]
2. **Component 2**: [Customize: Brief description]
3. **Component 3**: [Customize: Brief description]
4. **Component 4**: [Customize: Brief description]
5. **Component 5**: [Customize: Brief description]
6. **Component 6**: [Customize: Brief description]

### Development Workflow
- **PRD-Driven**: \`docs/specifications/PRD.md\` is the source of truth
- **AI-Assisted**: Claude Code and other AI tools coordinate development
- **Component-Based**: Build and test one component at a time
- **Quality-Focused**: Comprehensive testing and validation at each step

## Getting Started

### Prerequisites
- $PRIMARY_LANGUAGE development environment
- Git for version control
- VS Code with Claude Code extension (recommended)

### Development Commands
\`\`\`bash
# Run tests
$(get_test_command)

# Code quality checks
$(get_lint_command)
$(get_format_command)

# AI workflow commands (in Claude Code)
@orient          # Get project status and next actions
@next-task       # Select and plan next component
@finalize-task   # Complete current work
@update-prd      # Sync project status
\`\`\`

## Project Structure

\`\`\`
$PROJECT_ID/
├── docs/
│   ├── specifications/        # PRD and feature specs
│   └── architecture/          # Design principles
├── src/                       # Main implementation
├── tests/                     # Test suite
├── config/                    # Configuration files
├── .ai-context/              # AI coordination docs
├── .claude/                  # Claude Code commands
└── scripts/                  # Automation scripts
\`\`\`

## Documentation

- **[PRD](docs/specifications/PRD.md)**: Project requirements and component status
- **[Development Workflow](docs/specifications/dev-cycle.md)**: AI-assisted development process
- **[Architecture Principles](docs/architecture/)**: SLC principles and design guidelines
- **[AI Context](\.ai-context/AI_CONTEXT.md)**: Project knowledge base for AI assistants

## Contributing

This project uses an AI-powered development workflow:

1. Review \`docs/specifications/PRD.md\` for current status
2. Use \`@orient\` in Claude Code to understand next steps
3. Use \`@next-task\` to select and plan work
4. Implement using AI assistance and SLC principles
5. Use \`@finalize-task\` to complete and validate work
6. Use \`@update-prd\` to sync project status

## License

[Add your license here]
EOF
        
        print_success "README.md created"
    fi
}

# Function to create Claude settings template
setup_claude_settings() {
    if [[ ! -f ".claude/settings.template.json" ]]; then
        print_status "Creating Claude Code settings template..."
        
        cat > .claude/settings.template.json << EOF
{
  "name": "$PROJECT_NAME",
  "description": "$PROJECT_DESCRIPTION",
  "claude": {
    "contextFiles": [
      ".ai-context/AI_CONTEXT.md",
      "docs/specifications/PRD.md",
      ".ai-context/WORKFLOW_GUIDE.md"
    ],
    "persona": ".claude/persona.md",
    "commands": [
      ".claude/commands/orient.md",
      ".claude/commands/next-task.md",
      ".claude/commands/finalize-task.md",
      ".claude/commands/update-prd.md"
    ]
  },
  "project": {
    "language": "$PRIMARY_LANGUAGE",
    "testCommand": "$(get_test_command)",
    "lintCommand": "$(get_lint_command)",
    "formatCommand": "$(get_format_command)"
  }
}
EOF
        
        print_success "Claude settings template created"
    fi
}

# Function to validate setup
validate_setup() {
    print_status "Validating project setup..."
    
    local validation_errors=()
    
    # Check required files exist
    local required_files=(
        "docs/specifications/PRD.md"
        ".ai-context/AI_CONTEXT.md"
        ".ai-context/WORKFLOW_GUIDE.md"
        ".claude/persona.md"
        "config/project-config.json"
        "README.md"
    )
    
    for file in "${required_files[@]}"; do
        if [[ ! -f "$file" ]]; then
            validation_errors+=("Missing file: $file")
        fi
    done
    
    # Check required directories exist
    local required_dirs=(
        "src"
        "tests"
        "docs/specifications"
        "docs/architecture"
        ".claude/commands"
        ".ai-context"
    )
    
    for dir in "${required_dirs[@]}"; do
        if [[ ! -d "$dir" ]]; then
            validation_errors+=("Missing directory: $dir")
        fi
    done
    
    # Report validation results
    if [[ ${#validation_errors[@]} -eq 0 ]]; then
        print_success "Project setup validation passed"
        return 0
    else
        print_error "Project setup validation failed:"
        for error in "${validation_errors[@]}"; do
            echo "  - $error"
        done
        return 1
    fi
}

# Function to display next steps
show_next_steps() {
    print_success "Project initialization complete!"
    echo
    print_status "Your AI-powered development workflow is now set up."
    echo
    echo "📋 Next Steps:"
    echo "1. Customize your PRD: Edit docs/specifications/PRD.md"
    echo "2. Define your components: Update the component pipeline"
    echo "3. Set up development environment: Install dependencies"
    echo "4. Start Claude Code: Use 'code .' and install Claude Code extension"
    echo "5. Begin development: Use @orient command to get started"
    echo
    echo "🔧 Key Commands in Claude Code:"
    echo "  @orient          Get project status and next actions"
    echo "  @next-task       Select and plan next component"
    echo "  @finalize-task   Complete current work"
    echo "  @update-prd      Sync project status"
    echo
    echo "📚 Documentation:"
    echo "  docs/specifications/PRD.md           Project requirements"
    echo "  docs/specifications/dev-cycle.md     Development workflow"
    echo "  .ai-context/AI_CONTEXT.md           AI knowledge base"
    echo "  docs/architecture/                   Design principles"
    echo
    print_status "Happy coding with AI assistance! 🤖"
}

# Main execution
main() {
    echo "🤖 AI-Powered Development Cycle - Project Initialization"
    echo "========================================================"
    echo
    
    # Run initialization steps
    check_dependencies
    collect_project_info
    setup_directory_structure
    customize_templates
    setup_git_repository
    create_readme
    setup_claude_settings
    
    # Validate setup
    if validate_setup; then
        show_next_steps
    else
        print_error "Setup validation failed. Please check the errors above."
        exit 1
    fi
}

# Run main function
main "$@"