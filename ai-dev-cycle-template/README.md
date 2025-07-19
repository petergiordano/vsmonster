# AI-Powered Development Cycle Template

A complete, production-ready template for implementing AI-assisted development workflows in any VS Code project.

## 🎯 What This Template Provides

This template packages a complete AI-powered development methodology that transforms how you build software:

- **PRD-Driven Development**: Single source of truth for project requirements and progress
- **Component-Based Architecture**: Break complex projects into manageable, testable components  
- **AI Coordination**: Claude Code, Gemini CLI, and Codex working together seamlessly
- **SLC Principles**: Simple, Lovable, Complete design framework for quality outcomes
- **Automated Workflows**: Commands that handle routine development tasks

## ⚡ Quick Start

### 1. Clone and Initialize
```bash
# Clone the template (or download as ZIP)
git clone [your-template-repo] my-project
cd my-project

# Run the setup script
./scripts/initialize-project.sh

# Validate setup
python scripts/validate-setup.py
```

### 2. Customize for Your Project  
```bash
# Edit the PRD template for your domain
code docs/specifications/PRD.md

# Configure your development environment
code config/project-config.json
```

### 3. Start Developing with AI
```bash
# Open in VS Code with Claude Code extension
code .

# Use AI workflow commands:
@orient          # Get project status and next steps
@next-task       # Select and plan next component  
@finalize-task   # Complete current work
@update-prd      # Sync project progress
```

## 🏗️ Architecture

### Component Pipeline Approach
Every project is structured as a sequential pipeline of 4-8 components:
```
Input → Component 1 → Component 2 → Component 3 → ... → Final Output
```

Each component follows SLC principles:
- **Simple**: Does one job exceptionally well
- **Lovable**: Provides clear feedback and user confidence
- **Complete**: Produces output ready for the next component

### AI Coordination Framework
- **Claude Code**: Complex problem-solving, architecture decisions, code review
- **Specialized AIs**: Domain-specific tasks (Codex for implementation, Gemini for file operations)
- **Human Oversight**: Strategic decisions, quality gates, final approval

### Development Workflow
1. **PRD Review** → Identify next component from requirements
2. **Feature Spec** → Create detailed specification using template
3. **AI Implementation** → Assisted development with quality gates
4. **Integration** → Component testing and pipeline validation
5. **Progress Update** → Update PRD and prepare for next iteration

## 📁 Template Structure

```
ai-dev-cycle-template/
├── README.md                           # This file
├── TEMPLATE_SETUP.md                   # Detailed setup instructions
├── TEST_PLAN.md                        # Standalone testing guide
├── docs/
│   ├── architecture/                   # Design principles and patterns
│   │   ├── SLC_Principles.md           # Simple, Lovable, Complete framework
│   │   ├── ComponentLibrary.md         # Reusable design patterns
│   │   └── Experience_Goals.md         # User experience guidelines
│   └── specifications/                 # Project planning templates
│       ├── PRD_TEMPLATE.md             # Product requirements template
│       ├── FEATURE_SPEC_TEMPLATE.md    # Component specification template
│       └── dev-cycle.md                # Development workflow guide
├── .claude/                            # Claude Code integration
│   ├── persona.md                      # AI development expert persona
│   ├── settings.template.json          # Claude settings template
│   └── commands/                       # Workflow automation commands
│       ├── orient.md                   # Project orientation
│       ├── next-task.md                # Task selection and planning
│       ├── finalize-task.md            # Work completion and validation
│       └── update-prd.md               # Progress synchronization
├── .ai-context/                        # AI coordination documentation
│   ├── AI_CONTEXT_TEMPLATE.md          # Project knowledge base
│   └── WORKFLOW_GUIDE.md               # Implementation coordination
├── config/                             # Configuration templates
│   ├── project-config.template.json    # Project settings
│   └── notion-schema.template.json     # Optional task management
└── scripts/                            # Automation tools
    ├── initialize-project.sh           # Automated setup
    └── validate-setup.py               # Environment validation
```

## 🎛️ Key Features

### AI Workflow Commands
- **@orient**: Get project status and recommended next actions
- **@next-task**: Automatically select and plan the highest priority component
- **@finalize-task**: Complete current work with testing and documentation
- **@update-prd**: Synchronize project progress and status

### Quality Assurance
- **Comprehensive Testing**: Unit, integration, and end-to-end validation
- **Reference Test Cases**: Validate every component against real-world scenarios
- **Performance Monitoring**: Track speed, resource usage, and user satisfaction
- **Code Quality Gates**: Automated linting, formatting, and style checking

### Documentation Automation
- **Living Documentation**: PRD updates automatically with development progress
- **Implementation Logs**: Detailed records of development decisions and learnings
- **Architecture Decision Records**: Persistent record of design choices
- **AI Context Management**: Knowledge base that grows with your project

## 🌟 Domain Examples

### Data Processing Pipeline
```
Raw Data → Validation → Transformation → Analysis → Visualization → Export
```
- Focus on data accuracy and processing speed
- Emphasize error handling and data quality
- Include cost monitoring for cloud processing

### Content Generation System
```
Input → Parsing → Generation → Quality Check → Formatting → Output
```
- Prioritize output quality and consistency
- Include API cost tracking and optimization
- Focus on user experience and content standards

### API Integration Project
```
Config → Authentication → Data Mapping → Processing → Validation → Response
```
- Emphasize reliability and error handling
- Include rate limiting and timeout management
- Focus on data transformation accuracy

## 🚀 Getting Started

### Prerequisites
- **Git**: Version control and template management
- **VS Code**: Primary development environment
- **Claude Code Extension**: AI coordination and assistance
- **Programming Language**: Python, JavaScript, Go, or your preferred language

### Installation Steps

1. **Get the Template**
   ```bash
   # Option 1: Clone from repository
   git clone [template-repo-url] my-new-project
   
   # Option 2: Download as ZIP and extract
   # Download from GitHub releases page
   ```

2. **Initialize Your Project**
   ```bash
   cd my-new-project
   ./scripts/initialize-project.sh
   ```

3. **Validate Setup**
   ```bash
   python scripts/validate-setup.py
   ```

4. **Customize for Your Domain**
   - Edit `docs/specifications/PRD.md` with your project requirements
   - Update component pipeline for your specific use case
   - Configure development environment settings

5. **Start AI-Assisted Development**
   ```bash
   code .
   # Install Claude Code extension if needed
   # Use @orient to get started
   ```

## 📖 Documentation

### Essential Reading
- **[TEMPLATE_SETUP.md](TEMPLATE_SETUP.md)**: Detailed setup and customization guide
- **[PRD Template](docs/specifications/PRD_TEMPLATE.md)**: Project requirements structure
- **[SLC Principles](docs/architecture/SLC_Principles.md)**: Core design philosophy
- **[Development Workflow](docs/specifications/dev-cycle.md)**: AI-assisted development process

### Reference Documentation
- **[Feature Spec Template](docs/specifications/FEATURE_SPEC_TEMPLATE.md)**: Component specification format
- **[Component Library](docs/architecture/ComponentLibrary.md)**: Design patterns and standards
- **[Experience Goals](docs/architecture/Experience_Goals.md)**: User experience guidelines
- **[Workflow Guide](.ai-context/WORKFLOW_GUIDE.md)**: AI coordination details

## 🤝 Contributing

This template is designed to evolve based on real-world usage:

1. **Use the template** in your own projects
2. **Document learnings** and improvements
3. **Share feedback** on what works and what doesn't
4. **Contribute improvements** back to the template

### Template Development
- Keep the core principles intact
- Make customization easy and obvious
- Provide clear examples for different domains
- Maintain compatibility with AI tools

## 📜 License

[Add your license here - MIT, Apache 2.0, etc.]

## 🆘 Support

### Common Issues
- **Setup Problems**: Run `python scripts/validate-setup.py` for diagnostics
- **AI Integration**: Check Claude Code extension installation and settings
- **Customization Questions**: See TEMPLATE_SETUP.md for detailed guidance

### Getting Help
- Check the documentation in `docs/` directory
- Review examples in the template files
- Use the validation script to identify setup issues
- Create issues in the template repository

---

**Transform your development workflow with AI assistance. Build faster, build better, build with confidence.** 🤖✨