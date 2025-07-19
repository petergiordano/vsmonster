# Product Steering Guide

**Purpose**: Define product purpose, target users, and key features to guide AI decision-making throughout development.

**Inclusion Mode**: `always` - This file is loaded in every AI interaction to provide consistent product context.

## Product Overview

### Product Purpose
[CUSTOMIZE: Replace with your specific product purpose]

This system serves as an AI-powered development framework that transforms high-level requirements into production-ready software through systematic, component-based implementation. The product eliminates manual development overhead by providing:

- Structured specification workflow (Requirements → Design → Tasks)
- AI-guided implementation with persistent project knowledge
- Automated quality gates and validation
- Production-ready deployment patterns

### Core Value Proposition
**For**: Development teams and individual developers  
**Who**: Need to build reliable, maintainable software systems  
**The product**: Provides AI-assisted development with structured methodology  
**That**: Reduces development time while improving code quality  
**Unlike**: Unstructured AI coding or traditional manual development  
**Our solution**: Combines AI intelligence with proven software engineering practices

## Target Users

### Primary Users

#### 1. Solo Developers
**Profile**: Individual developers building personal or small business projects
**Goals**: 
- Rapid prototyping with production readiness
- Consistent code quality without team oversight
- Learning and applying best practices
**Pain Points**:
- Maintaining discipline in solo development
- Ensuring comprehensive testing and documentation
- Managing technical debt

**AI Behavior Guidelines**:
- Emphasize simplicity and maintainability
- Provide detailed explanations for learning
- Include comprehensive testing and documentation
- Suggest refactoring opportunities

#### 2. Small Development Teams (2-5 developers)
**Profile**: Startup teams or small company development groups
**Goals**:
- Consistent development practices across team
- Efficient onboarding of new team members
- Rapid iteration with quality control
**Pain Points**:
- Maintaining code consistency across developers
- Balancing speed with quality
- Documentation and knowledge sharing

**AI Behavior Guidelines**:
- Focus on team consistency and patterns
- Emphasize code review and collaboration
- Provide clear documentation standards
- Support knowledge transfer

#### 3. Enterprise Development Teams
**Profile**: Larger organizations with complex compliance and quality requirements
**Goals**:
- Governance and audit trail compliance
- Integration with existing enterprise systems
- Risk mitigation and quality assurance
**Pain Points**:
- Complex approval processes
- Integration with legacy systems
- Compliance and security requirements

**AI Behavior Guidelines**:
- Emphasize documentation and traceability
- Include security and compliance considerations
- Support integration patterns
- Provide audit trail capabilities

### Secondary Users

#### 4. Technical Leads and Architects
**Profile**: Senior developers responsible for technical direction
**Goals**:
- Ensuring architectural consistency
- Mentoring team members
- Long-term maintainability
**Use Cases**:
- Architectural decision guidance
- Code review assistance
- Team mentoring support

#### 5. Product Managers
**Profile**: Non-technical stakeholders tracking development progress
**Goals**:
- Understanding development progress
- Managing scope and timeline
- Communicating with stakeholders
**Use Cases**:
- Progress reporting and visualization
- Requirement validation and feedback
- Stakeholder communication support

## Key Features and Capabilities

### Core Features

#### 1. Specification-Driven Development
**Purpose**: Structure development process through formal specifications
**User Value**: Ensures clear requirements and reduces miscommunication
**Implementation Priority**: Critical
**Quality Standards**: 
- All specifications traceable to business requirements
- Validation against reference test cases
- Automated consistency checking

#### 2. AI-Powered Component Implementation
**Purpose**: Generate production-ready code following established patterns
**User Value**: Accelerates development while maintaining quality
**Implementation Priority**: Critical
**Quality Standards**:
- Code follows established patterns and conventions
- Comprehensive test coverage (>80%)
- Documentation generated with code

#### 3. Automated Quality Assurance
**Purpose**: Continuous validation of code quality and functionality
**User Value**: Reduces bugs and improves maintainability
**Implementation Priority**: High
**Quality Standards**:
- Automated testing at multiple levels
- Code quality metrics tracking
- Security vulnerability scanning

#### 4. Production Deployment Support
**Purpose**: Streamlined path from development to production
**User Value**: Reduces deployment risks and operational overhead
**Implementation Priority**: High
**Quality Standards**:
- Comprehensive deployment documentation
- Monitoring and logging setup
- Rollback and recovery procedures

### Advanced Features

#### 5. Agent Steering and Context Management
**Purpose**: Maintain project-specific AI behavior and knowledge
**User Value**: Consistent AI assistance throughout project lifecycle
**Implementation Priority**: Medium
**Quality Standards**:
- Context accuracy and relevance
- Steering file maintenance
- Knowledge base synchronization

#### 6. Multi-AI Coordination
**Purpose**: Orchestrate multiple AI tools for complex tasks
**User Value**: Leverage specialized AI capabilities
**Implementation Priority**: Medium
**Quality Standards**:
- Seamless tool integration
- Consistent data flow between tools
- Error handling across tool boundaries

## Success Metrics

### User Success Metrics

#### Development Velocity
- **Time to First Working Prototype**: < 4 hours for simple projects
- **Feature Implementation Speed**: 50% faster than traditional development
- **Bug Fix Time**: 70% reduction in average fix time

#### Code Quality
- **Test Coverage**: >80% for all components
- **Code Review Comments**: 60% reduction in review iterations
- **Production Bugs**: 75% reduction in post-deployment issues

#### User Satisfaction
- **Developer Experience Rating**: >4.0/5.0 in user surveys
- **Feature Adoption Rate**: >70% of users use advanced features
- **Retention Rate**: >85% monthly active users

### Business Success Metrics

#### Project Success
- **On-Time Delivery**: >90% of projects meet original timelines
- **Budget Adherence**: >85% of projects stay within budget
- **Scope Creep Reduction**: 50% less scope expansion during development

#### Quality Outcomes
- **Production Incidents**: 80% reduction in severity 1-2 incidents
- **Security Vulnerabilities**: 90% reduction in high-risk vulnerabilities
- **Performance Issues**: 70% fewer performance-related problems

## Product Principles

### 1. Simple, Lovable, Complete (SLC)
**Simple**: Minimize complexity while meeting requirements
- Prefer straightforward solutions over clever ones
- Eliminate unnecessary abstractions
- Optimize for readability and understanding

**Lovable**: Optimize for developer and user experience
- Prioritize developer happiness and productivity
- Create intuitive interfaces and workflows
- Provide helpful error messages and guidance

**Complete**: Include all necessary functionality for production use
- Don't leave gaps that require manual intervention
- Include monitoring, logging, and error handling
- Provide comprehensive documentation

### 2. AI-First Development
**Principle**: Leverage AI capabilities while maintaining human control
- AI suggests, human decides
- Transparent AI decision-making
- Fallback to manual processes when AI fails

### 3. Quality by Default
**Principle**: Build quality into the development process
- Testing is not optional
- Documentation is generated with code
- Security and performance considered from the start

### 4. Iterative Improvement
**Principle**: Continuous learning and adaptation
- Learn from each project implementation
- Refine patterns and practices based on outcomes
- Update steering based on project learnings

## Domain-Specific Considerations

### Data Processing Projects
**Focus Areas**: Data quality, performance, scalability
**Success Criteria**: Accuracy, processing speed, error handling
**Special Considerations**: Memory usage, data lineage, validation

### Content Generation Projects
**Focus Areas**: Output quality, consistency, cost efficiency
**Success Criteria**: Content quality, brand compliance, API costs
**Special Considerations**: Content review workflows, version control

### API Integration Projects
**Focus Areas**: Reliability, error handling, data consistency
**Success Criteria**: Uptime, error recovery, data integrity
**Special Considerations**: Rate limiting, authentication, monitoring

### Web Applications
**Focus Areas**: User experience, performance, accessibility
**Success Criteria**: Page load times, accessibility compliance, user engagement
**Special Considerations**: Mobile responsiveness, SEO, security

## AI Behavior Guidelines

### Communication Style
- **Clarity**: Use clear, precise language
- **Context**: Always reference project context and goals
- **Actionability**: Provide specific, actionable recommendations
- **Education**: Explain reasoning behind suggestions

### Decision Making
- **Requirements First**: Always validate against product requirements
- **User Impact**: Consider impact on target users
- **Quality Standards**: Never compromise on quality standards
- **Traceability**: Maintain links between decisions and requirements

### Code Generation
- **Pattern Consistency**: Follow established project patterns
- **Documentation**: Include comprehensive documentation
- **Testing**: Generate tests with code
- **Security**: Apply security best practices by default

### Problem Solving
- **Root Cause**: Address root causes, not just symptoms
- **Multiple Solutions**: Present options when appropriate
- **Trade-offs**: Clearly explain trade-offs in recommendations
- **Learning**: Capture learnings for future reference

---

**This product steering guide ensures AI assistance remains aligned with product goals, user needs, and quality standards throughout the development process.**