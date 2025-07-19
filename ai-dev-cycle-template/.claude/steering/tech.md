# Technical Steering Guide

**Purpose**: Define technology stack, technical constraints, and engineering standards to guide AI decision-making throughout development.

**Inclusion Mode**: `always` - This file is loaded in every AI interaction to provide consistent technical context.

## Technology Stack

### Primary Language and Runtime
**Language**: [CUSTOMIZE: Replace with your primary language]
- **Python 3.8+**: For data processing and general applications
- **JavaScript/Node.js 16+**: For web applications and APIs
- **Go 1.19+**: For high-performance systems and microservices
- **TypeScript**: For large JavaScript applications requiring type safety

**Runtime Environment**:
- Local development on macOS/Linux/Windows
- Production deployment on [CUSTOMIZE: Cloud provider or on-premises]
- Containerization with Docker (optional)

### Core Dependencies and Libraries

#### Python Stack
```python
# Core libraries (always include)
pydantic>=1.10.0       # Data validation and settings
click>=8.0.0           # CLI interface
pytest>=7.0.0          # Testing framework
black>=22.0.0          # Code formatting
flake8>=4.0.0          # Linting
mypy>=0.990            # Type checking

# Domain-specific libraries
pandas>=1.5.0          # Data processing projects
requests>=2.28.0       # API integration projects
fastapi>=0.85.0        # Web API projects
```

#### JavaScript/Node.js Stack
```javascript
// Core libraries
express                // Web framework
joi                    // Data validation
jest                   // Testing framework
eslint                 // Linting
prettier               // Code formatting

// Domain-specific libraries
axios                  // HTTP client
lodash                 // Utility functions
moment                 // Date/time handling
```

#### Go Stack
```go
// Core libraries
gorilla/mux           // HTTP router
go-playground/validator // Data validation
testify              // Testing framework

// Domain-specific libraries
gin-gonic/gin        // Web framework
gorm                 // ORM
logrus               // Logging
```

### Development Tools and Environment

#### Code Quality Tools
- **Linting**: Language-specific linters (flake8, eslint, golangci-lint)
- **Formatting**: Auto-formatters (black, prettier, gofmt)
- **Type Checking**: Static type analysis where applicable
- **Security Scanning**: Dependency vulnerability scanning

#### Testing Framework
- **Unit Testing**: Language-specific frameworks (pytest, jest, go test)
- **Integration Testing**: API and component integration tests
- **End-to-End Testing**: Full system validation with reference test cases
- **Performance Testing**: Load and stress testing for critical components

#### Development Environment
- **IDE**: VS Code with language-specific extensions
- **Version Control**: Git with conventional commit messages
- **Package Management**: Language-specific (pip, npm, go mod)
- **Environment Management**: Virtual environments or containers

## Technical Constraints and Standards

### Performance Requirements

#### Response Time Standards
- **Interactive Operations**: < 200ms for user-facing actions
- **Processing Operations**: < 30 seconds for typical data processing
- **Batch Operations**: < 5 minutes for large-scale processing
- **System Startup**: < 10 seconds for application initialization

#### Throughput Requirements
- **API Endpoints**: > 100 requests/second for web APIs
- **Data Processing**: > 1000 records/minute for batch processing
- **Concurrent Users**: Support for 10+ simultaneous users
- **Resource Usage**: < 2GB memory, < 80% CPU under normal load

#### Scalability Patterns
- **Horizontal Scaling**: Design for multiple instance deployment
- **Vertical Scaling**: Efficient resource utilization
- **Caching**: Redis or in-memory caching for frequently accessed data
- **Database**: Optimize queries and use connection pooling

### Security Standards

#### Data Protection
- **Input Validation**: Validate all user inputs and external data
- **Output Sanitization**: Sanitize all outputs to prevent injection attacks
- **Encryption**: Use TLS 1.3 for data in transit, AES-256 for data at rest
- **Secrets Management**: Environment variables or dedicated secret stores

#### Authentication and Authorization
- **API Authentication**: JWT tokens or API keys for service authentication
- **User Authentication**: OAuth 2.0 or similar for user-facing applications
- **Role-Based Access**: Implement RBAC where user access control is needed
- **Audit Logging**: Log all security-relevant events

#### Security Practices
- **Dependency Scanning**: Regular vulnerability scans of dependencies
- **Code Analysis**: Static analysis for security vulnerabilities
- **Penetration Testing**: Regular security testing for web applications
- **Incident Response**: Clear procedures for security incident handling

### Code Quality Standards

#### Code Organization
```
project-root/
├── src/                    # Source code
│   ├── components/         # Main application components
│   ├── shared/            # Shared utilities and interfaces
│   ├── config/            # Configuration management
│   └── tests/             # Test files co-located with source
├── tests/                 # Integration and system tests
│   ├── unit/              # Isolated unit tests
│   ├── integration/       # Component integration tests
│   └── reference/         # Reference test cases
├── docs/                  # Documentation
├── config/                # Configuration files
└── scripts/               # Build and deployment scripts
```

#### Naming Conventions
- **Files**: snake_case for Python, camelCase for JavaScript, snake_case for Go
- **Classes**: PascalCase for all languages
- **Functions**: snake_case for Python, camelCase for JavaScript/Go
- **Constants**: UPPER_SNAKE_CASE for all languages
- **Variables**: snake_case for Python, camelCase for JavaScript/Go

#### Documentation Standards
- **Code Comments**: Explain why, not what
- **Function Documentation**: Document parameters, return values, and exceptions
- **API Documentation**: OpenAPI/Swagger for REST APIs
- **README Files**: Clear setup and usage instructions
- **Architecture Documentation**: High-level system design and decisions

### Error Handling Patterns

#### Error Categories
- **Validation Errors**: Input data validation failures
- **Business Logic Errors**: Domain-specific constraint violations
- **Integration Errors**: External service communication failures
- **System Errors**: Infrastructure and runtime failures

#### Error Handling Strategy
```python
# Python example
from enum import Enum
from typing import Optional, Dict, Any

class ErrorSeverity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class ErrorCode(Enum):
    VALIDATION_ERROR = "VALIDATION_ERROR"
    BUSINESS_LOGIC_ERROR = "BUSINESS_LOGIC_ERROR"
    INTEGRATION_ERROR = "INTEGRATION_ERROR"
    SYSTEM_ERROR = "SYSTEM_ERROR"

class ApplicationError(Exception):
    def __init__(
        self, 
        code: ErrorCode, 
        message: str, 
        severity: ErrorSeverity = ErrorSeverity.MEDIUM,
        context: Optional[Dict[str, Any]] = None
    ):
        self.code = code
        self.message = message
        self.severity = severity
        self.context = context or {}
        super().__init__(self.message)
```

#### Logging Standards
```python
# Structured logging format
{
    "timestamp": "2024-01-01T12:00:00Z",
    "level": "ERROR",
    "component": "component_name",
    "operation": "operation_name",
    "message": "Human-readable error message",
    "error_code": "ERROR_CODE",
    "context": {
        "user_id": "user123",
        "request_id": "req-456",
        "additional_data": "relevant_info"
    },
    "stack_trace": "detailed_stack_trace"
}
```

### Testing Standards

#### Test Coverage Requirements
- **Unit Tests**: >80% code coverage for all components
- **Integration Tests**: All component interfaces tested
- **End-to-End Tests**: Complete user journeys validated
- **Reference Test Coverage**: All components tested with reference case

#### Test Organization
```python
# Test file naming convention
test_[component_name].py       # Unit tests
test_[component_name]_integration.py  # Integration tests
test_system_[feature_name].py  # System tests

# Test function naming
def test_should_[expected_behavior]_when_[condition]():
    # Arrange
    # Act  
    # Assert
```

#### Test Data Management
- **Fixtures**: Reusable test data and setup
- **Factories**: Generate test data programmatically
- **Mocking**: Mock external dependencies consistently
- **Reference Data**: Maintain golden reference test cases

### Performance Optimization Guidelines

#### Code Optimization
- **Algorithmic Efficiency**: Choose appropriate algorithms and data structures
- **Memory Management**: Minimize memory allocations and leaks
- **I/O Optimization**: Batch operations and use async patterns where appropriate
- **Caching**: Cache expensive computations and frequently accessed data

#### Database Optimization
- **Query Optimization**: Use indexes and efficient query patterns
- **Connection Pooling**: Reuse database connections
- **Transaction Management**: Minimize transaction scope and duration
- **Data Modeling**: Normalize for consistency, denormalize for performance

#### Monitoring and Profiling
- **Performance Metrics**: Track response times, throughput, and resource usage
- **Profiling Tools**: Use language-specific profilers for optimization
- **Bottleneck Identification**: Identify and address performance bottlenecks
- **Continuous Monitoring**: Monitor performance in production

## Integration Patterns

### Component Integration
- **Interface Contracts**: Clear, versioned interfaces between components
- **Data Flow**: Explicit data transformation and validation between components
- **Error Propagation**: Consistent error handling across component boundaries
- **Configuration**: Centralized configuration management

### External Service Integration
- **Circuit Breaker**: Prevent cascade failures from external service outages
- **Retry Logic**: Exponential backoff with jitter for transient failures
- **Timeout Management**: Appropriate timeouts for external service calls
- **Health Checks**: Monitor external service availability

### API Design Patterns
- **RESTful Design**: Follow REST principles for HTTP APIs
- **Versioning**: Semantic versioning for API changes
- **Rate Limiting**: Protect APIs from abuse and overload
- **Documentation**: Comprehensive API documentation with examples

## Development Workflow

### Git Workflow
- **Branch Strategy**: Feature branches with pull requests
- **Commit Messages**: Conventional commits with clear descriptions
- **Code Review**: All changes reviewed before merge
- **Release Process**: Tagged releases with semantic versioning

### Continuous Integration
- **Automated Testing**: All tests run on every commit
- **Code Quality Gates**: Linting, formatting, and security checks
- **Build Validation**: Ensure code builds successfully
- **Deployment Pipeline**: Automated deployment to staging environments

### Development Process
1. **Requirements Analysis**: Understand requirements and constraints
2. **Design Review**: Validate technical design against requirements
3. **Implementation**: Follow coding standards and patterns
4. **Testing**: Comprehensive testing at all levels
5. **Code Review**: Peer review for quality and consistency
6. **Integration**: Validate integration with other components
7. **Documentation**: Update documentation with changes

## Technology-Specific Guidelines

### Python Development
- **Virtual Environments**: Use venv or conda for dependency isolation
- **Type Hints**: Use type hints for better code documentation and IDE support
- **Async Programming**: Use asyncio for I/O-bound operations
- **Package Structure**: Follow standard Python package organization

### JavaScript/Node.js Development
- **Module System**: Use ES6 modules for modern JavaScript
- **Async Programming**: Use async/await for asynchronous operations
- **Package Management**: Use npm or yarn for dependency management
- **Build Tools**: Use appropriate build tools (webpack, rollup, etc.)

### Go Development
- **Package Organization**: Follow Go package naming conventions
- **Error Handling**: Use explicit error handling patterns
- **Concurrency**: Use goroutines and channels appropriately
- **Build Process**: Use go modules for dependency management

## AI Behavior Guidelines

### Code Generation
- **Follow Standards**: Generate code that follows all technical standards
- **Include Tests**: Always generate tests with implementation code
- **Documentation**: Include appropriate documentation with generated code
- **Error Handling**: Implement comprehensive error handling

### Architecture Decisions
- **Justify Choices**: Explain technology and pattern choices
- **Consider Constraints**: Respect technical constraints and requirements
- **Performance Impact**: Consider performance implications of decisions
- **Maintainability**: Prioritize long-term maintainability

### Problem Solving
- **Technical Accuracy**: Provide technically accurate solutions
- **Best Practices**: Recommend industry best practices
- **Security First**: Consider security implications in all recommendations
- **Performance Aware**: Consider performance impact of suggestions

---

**This technical steering guide ensures all AI-generated code and recommendations align with established technical standards, constraints, and best practices.**