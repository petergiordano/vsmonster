# AI Context - Project Knowledge Base

**Project**: [PROJECT NAME]  
**Last Updated**: [DATE]  
**Context Version**: 1.0

This document serves as the single source of truth for AI assistants working on this project. It contains accumulated knowledge, patterns, and context that should persist across development sessions.

## Project Overview

### Core Purpose
[CUSTOMIZE: Brief description of what this project does and why it exists]

### Success Metrics
- [CUSTOMIZE: Primary success metric]
- [CUSTOMIZE: Secondary success metric]
- [CUSTOMIZE: Quality/performance target]

### Architecture Summary
This project follows a [N]-component pipeline architecture:
1. **[Component 1]**: [Brief purpose]
2. **[Component 2]**: [Brief purpose]
3. **[Component 3]**: [Brief purpose]
4. **[Component 4]**: [Brief purpose]
[Add/remove as needed]

## Current Project Context State

### Active Development
- **Current Phase**: [Planning/Implementation/Testing/Complete]
- **Active Component**: [Which component is being worked on]
- **Development Branch**: [Current feature branch]
- **Last Major Milestone**: [Recent achievement]

### Completed Features
- ✅ **[Component/Feature 1]**: [Completion date] - [Brief status]
- ✅ **[Component/Feature 2]**: [Completion date] - [Brief status]
[Add completed items here]

### Planned Features
- 📝 **[Component/Feature A]**: [Target timeline] - [Brief description]
- 📝 **[Component/Feature B]**: [Target timeline] - [Brief description]
[Add planned items here]

## Architecture Decisions Made

### Technology Stack Choices
- **Primary Language**: [Language] - [Reason for choice]
- **Key Dependencies**: [List critical dependencies]
- **External Services**: [APIs, services used]
- **Development Tools**: [Testing framework, linting, etc.]

### Design Patterns Established
- **[Pattern 1]**: [Description and rationale]
- **[Pattern 2]**: [Description and rationale]
- **Error Handling**: [Standard approach]
- **Configuration Management**: [How config is handled]

### Component Architecture
- **Data Flow**: [How data moves through the system]
- **Interface Standards**: [How components communicate]
- **Testing Strategy**: [How components are validated]
- **Integration Points**: [Key integration decisions]

## Known Patterns & Conventions Discovered

### Code Organization
```
[PROJECT_ROOT]/
├── src/                    # [Purpose]
├── tests/                  # [Testing approach]
├── config/                 # [Configuration files]
├── docs/                   # [Documentation structure]
└── [other directories]     # [Purpose]
```

### Naming Conventions
- **Files**: [Convention used, e.g., snake_case, kebab-case]
- **Functions/Methods**: [Convention used]
- **Variables**: [Convention used]
- **Components**: [Convention used]

### Development Workflow
- **Branch Strategy**: [How branches are managed]
- **Commit Messages**: [Format and conventions]
- **Testing Requirements**: [What must be tested]
- **Review Process**: [How code is reviewed]

## Dependencies & Integration Points

### External Services
- **[Service 1]**: [Purpose, API key requirements, rate limits]
- **[Service 2]**: [Purpose, configuration needs]

### Internal Dependencies
- **[Component A] → [Component B]**: [Data format, interface]
- **[Component B] → [Component C]**: [Data format, interface]

### Configuration Requirements
- **Environment Variables**: [List required vars]
- **Config Files**: [Location and format]
- **Secrets Management**: [How sensitive data is handled]

## Testing & Validation Approach

### Reference Test Case
- **Primary Test Case**: [Description of main validation scenario]
- **Location**: [File path to reference data]
- **Success Criteria**: [How to know if it passes]

### Testing Strategy
- **Unit Tests**: [Coverage expectations, tools used]
- **Integration Tests**: [Component interaction testing]
- **End-to-End Tests**: [Full pipeline validation]
- **Performance Tests**: [Speed/resource requirements]

### Quality Gates
- **Code Quality**: [Linting, formatting requirements]
- **Test Coverage**: [Minimum coverage percentage]
- **Performance**: [Speed/memory targets]
- **Integration**: [Component compatibility requirements]

## Lessons Learned & Best Practices

### Development Insights
- **[Insight 1]**: [What was learned and how it applies]
- **[Insight 2]**: [What was learned and how it applies]

### Common Pitfalls Avoided
- **[Pitfall 1]**: [What to watch out for and why]
- **[Pitfall 2]**: [What to watch out for and why]

### Optimization Opportunities
- **[Opportunity 1]**: [Potential improvement identified]
- **[Opportunity 2]**: [Potential improvement identified]

### Technical Debt
- **[Debt Item 1]**: [Description and priority]
- **[Debt Item 2]**: [Description and priority]

## AI Assistant Guidance

### Code Style Preferences
- **Readability**: [Prioritize clarity over cleverness]
- **Error Handling**: [Be explicit about error conditions]
- **Documentation**: [Comment non-obvious logic]
- **Testing**: [Write tests first, implementation second]

### Implementation Approach
- **Component Development**: [One component at a time, test thoroughly]
- **Integration**: [Test interfaces early and often]
- **Performance**: [Measure first, optimize second]
- **Refactoring**: [Safe, incremental changes]

### Quality Standards
- **Functional Requirements**: [Must meet all feature spec criteria]
- **Performance Requirements**: [Must meet speed/resource targets]
- **Reliability Requirements**: [Must handle errors gracefully]
- **Maintainability**: [Must be readable and modifiable]

## Project-Specific Context

### Domain Knowledge
[CUSTOMIZE: Add domain-specific information that AI assistants need to know]

### Business Rules
[CUSTOMIZE: Add any business logic or constraints specific to your project]

### User Workflow
[CUSTOMIZE: Describe how users interact with your system]

### Success Stories
[CUSTOMIZE: Examples of what success looks like in your domain]

---

## Context Maintenance Protocol

### When to Update This Document
- After completing major components or features
- When architectural decisions are made
- When new patterns or conventions are established
- When lessons are learned from implementation challenges
- When dependencies or integrations change

### Update Triggers for AI Assistants
1. **Task Completion**: After using `@finalize-task`, review if context needs updates
2. **Architectural Changes**: When making design decisions that affect other components
3. **Pattern Discovery**: When establishing new coding patterns or conventions
4. **Integration Changes**: When modifying how components interact
5. **Performance Insights**: When discovering optimization opportunities

### Maintenance Checklist
- [ ] Update completion status for finished components
- [ ] Record any new architectural decisions
- [ ] Document new patterns or conventions discovered
- [ ] Update dependency information
- [ ] Record lessons learned and best practices
- [ ] Update AI guidance based on project evolution

---

*This document should be the first thing AI assistants read when starting work on this project. It provides the essential context needed to understand the project's current state, architecture, and development approach.*