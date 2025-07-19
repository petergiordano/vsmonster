# Project Structure Steering Guide

**Purpose**: Define file organization, naming conventions, and architectural patterns to ensure consistent project structure throughout development.

**Inclusion Mode**: `always` - This file is loaded in every AI interaction to maintain structural consistency.

## Project Organization Philosophy

### Hierarchical Structure
The project follows a hierarchical organization that mirrors the logical architecture:
- **Top Level**: Configuration, documentation, and entry points
- **Source Level**: Organized by functional areas and components
- **Component Level**: Self-contained modules with clear interfaces
- **Feature Level**: Specific functionality within components

### Separation of Concerns
- **Business Logic**: Core application functionality
- **Infrastructure**: Technical concerns (logging, config, database)
- **Interfaces**: External communication (APIs, CLIs, UIs)
- **Tests**: Validation and quality assurance
- **Documentation**: Project knowledge and guidance

## Directory Structure

### Root Level Organization
```
project-root/
├── README.md                    # Project overview and quick start
├── LICENSE                      # License information
├── .gitignore                  # Git ignore patterns
├── .env.example                # Environment variables template
├── src/                        # Source code
├── tests/                      # Test suites
├── docs/                       # Documentation
├── config/                     # Configuration files
├── scripts/                    # Build and utility scripts
├── .claude/                    # AI coordination files
├── .ai-context/               # AI knowledge base
├── .github/                   # GitHub workflows (if using GitHub)
└── deploy/                    # Deployment configurations
```

### Source Code Organization (`src/`)
```
src/
├── components/                 # Main application components
│   ├── component1/            # First pipeline component
│   │   ├── __init__.py        # Component package init
│   │   ├── processor.py       # Main processing logic
│   │   ├── validator.py       # Input/output validation
│   │   ├── config.py          # Component configuration
│   │   ├── models.py          # Data models
│   │   └── exceptions.py      # Component-specific exceptions
│   ├── component2/            # Second pipeline component
│   │   └── [similar structure]
│   └── componentN/            # Additional components
├── shared/                    # Shared utilities and interfaces
│   ├── __init__.py           # Shared package init
│   ├── interfaces.py         # Common interfaces and protocols
│   ├── exceptions.py         # Application-wide exceptions
│   ├── utils.py              # Utility functions
│   ├── constants.py          # Application constants
│   └── types.py              # Common type definitions
├── pipeline/                  # Pipeline orchestration
│   ├── __init__.py           # Pipeline package init
│   ├── orchestrator.py       # Main pipeline coordinator
│   ├── monitor.py            # Pipeline monitoring
│   ├── scheduler.py          # Task scheduling (if needed)
│   └── recovery.py           # Error recovery logic
├── config/                   # Configuration management
│   ├── __init__.py          # Config package init
│   ├── settings.py          # Settings management
│   ├── validation.py        # Configuration validation
│   └── defaults.py          # Default configuration values
├── interfaces/              # External interfaces
│   ├── cli/                 # Command-line interface
│   │   ├── __init__.py     # CLI package init
│   │   ├── main.py         # CLI entry point
│   │   ├── commands.py     # CLI command definitions
│   │   └── utils.py        # CLI utilities
│   ├── api/                # REST API (if applicable)
│   │   ├── __init__.py     # API package init
│   │   ├── app.py          # API application
│   │   ├── routes.py       # API route definitions
│   │   └── models.py       # API data models
│   └── web/                # Web interface (if applicable)
│       ├── static/         # Static assets
│       ├── templates/      # HTML templates
│       └── app.py          # Web application
└── infrastructure/         # Technical infrastructure
    ├── __init__.py         # Infrastructure package init
    ├── logging.py          # Logging configuration
    ├── monitoring.py       # Monitoring and metrics
    ├── database.py         # Database connections
    └── cache.py            # Caching implementation
```

### Test Organization (`tests/`)
```
tests/
├── unit/                      # Unit tests
│   ├── components/           # Component unit tests
│   │   ├── test_component1.py
│   │   ├── test_component2.py
│   │   └── test_componentN.py
│   ├── shared/               # Shared utilities tests
│   │   ├── test_utils.py
│   │   └── test_interfaces.py
│   └── pipeline/             # Pipeline unit tests
│       ├── test_orchestrator.py
│       └── test_monitor.py
├── integration/              # Integration tests
│   ├── test_component_integration.py
│   ├── test_pipeline_integration.py
│   └── test_api_integration.py
├── system/                   # System/end-to-end tests
│   ├── test_full_pipeline.py
│   └── test_reference_cases.py
├── reference/                # Reference test cases
│   ├── input/               # Reference input data
│   ├── expected/            # Expected output data
│   └── test_reference_validation.py
├── fixtures/                 # Test fixtures and data
│   ├── __init__.py
│   ├── sample_data.py
│   └── mock_services.py
└── conftest.py               # Pytest configuration
```

### Documentation Organization (`docs/`)
```
docs/
├── specifications/           # Project specifications
│   ├── PRD.md               # Product Requirements Document
│   ├── requirements.md      # Detailed requirements
│   ├── design.md           # Technical design
│   ├── tasks.md            # Implementation tasks
│   └── dev-cycle.md        # Development workflow
├── architecture/            # Architecture documentation
│   ├── SLC_Principles.md   # Design principles
│   ├── ComponentLibrary.md # Design patterns
│   └── Experience_Goals.md # User experience targets
├── api/                    # API documentation
│   ├── components.md       # Component APIs
│   ├── pipeline.md         # Pipeline APIs
│   └── rest-api.md         # REST API (if applicable)
├── deployment/             # Deployment documentation
│   ├── setup.md           # Setup instructions
│   ├── configuration.md   # Configuration guide
│   └── troubleshooting.md # Common issues
├── implementation-logs/    # Development logs
│   ├── component1-log.md
│   ├── component2-log.md
│   └── integration-log.md
└── assets/                # Documentation assets
    ├── diagrams/          # Architecture diagrams
    └── screenshots/       # UI screenshots
```

### Configuration Organization (`config/`)
```
config/
├── project-config.json      # Main project configuration
├── development.json         # Development environment config
├── testing.json            # Testing environment config
├── production.json         # Production environment config
├── logging.yaml            # Logging configuration
└── secrets.json.example    # Secrets template (not in git)
```

## Naming Conventions

### File and Directory Naming

#### General Rules
- **Directories**: Use lowercase with underscores (`component_name/`)
- **Python Files**: Use lowercase with underscores (`file_name.py`)
- **JavaScript Files**: Use camelCase (`fileName.js`)
- **Go Files**: Use lowercase with underscores (`file_name.go`)
- **Configuration Files**: Use lowercase with hyphens (`config-name.json`)
- **Documentation Files**: Use PascalCase with hyphens (`Feature-Name.md`)

#### Specific Patterns
```
# Component naming
component_[number]/           # component_1/, component_2/
component_[name]/            # component_data_processor/

# Test file naming
test_[module_name].py        # test_processor.py
test_[module_name]_integration.py  # test_processor_integration.py

# Configuration naming
[environment].json           # development.json, production.json
[service]-config.yaml        # database-config.yaml

# Documentation naming
[Type]-[Name].md            # API-Reference.md, Setup-Guide.md
```

### Code Element Naming

#### Python Conventions
```python
# Classes: PascalCase
class DataProcessor:
    pass

class ValidationError(Exception):
    pass

# Functions and variables: snake_case
def process_data(input_data):
    processed_result = transform_input(input_data)
    return processed_result

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# Private methods: leading underscore
def _internal_helper(self):
    pass

# Module-level "private": leading underscore
_internal_cache = {}
```

#### JavaScript/TypeScript Conventions
```javascript
// Classes: PascalCase
class DataProcessor {
}

class ValidationError extends Error {
}

// Functions and variables: camelCase
function processData(inputData) {
    const processedResult = transformInput(inputData);
    return processedResult;
}

// Constants: UPPER_SNAKE_CASE or camelCase
const MAX_RETRIES = 3;
const defaultTimeout = 30;

// Private methods: leading underscore or # (private fields)
class Example {
    #privateField;
    
    _internalHelper() {
    }
}
```

#### Go Conventions
```go
// Exported types: PascalCase
type DataProcessor struct {
    config Config
}

// Unexported types: camelCase
type internalState struct {
    data []byte
}

// Exported functions: PascalCase
func ProcessData(inputData []byte) ([]byte, error) {
    result, err := transformInput(inputData)
    return result, err
}

// Unexported functions: camelCase
func transformInput(data []byte) ([]byte, error) {
    // implementation
}

// Constants: Mixed case or UPPER_SNAKE_CASE
const MaxRetries = 3
const DEFAULT_TIMEOUT = 30 * time.Second
```

## Architectural Patterns

### Component Architecture

#### Component Structure Pattern
Each component follows a consistent internal structure:
```
component_name/
├── __init__.py              # Package interface
├── processor.py             # Main business logic
├── validator.py             # Input/output validation
├── models.py                # Data models and types
├── config.py                # Component configuration
├── exceptions.py            # Component-specific exceptions
├── utils.py                 # Component utilities
└── interfaces.py            # External interfaces
```

#### Component Interface Pattern
```python
# Standard component interface
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class ComponentInterface(ABC):
    """Standard interface for all pipeline components."""
    
    @abstractmethod
    def process(self, input_data: Any, config: Dict[str, Any]) -> Any:
        """Process input data and return results."""
        pass
    
    @abstractmethod
    def validate_input(self, input_data: Any) -> bool:
        """Validate input data format and content."""
        pass
    
    @abstractmethod
    def validate_output(self, output_data: Any) -> bool:
        """Validate output data format and content."""
        pass
    
    def health_check(self) -> Dict[str, Any]:
        """Return component health status."""
        return {"status": "healthy", "component": self.__class__.__name__}
```

### Error Handling Patterns

#### Exception Hierarchy
```python
# Base application exception
class ApplicationError(Exception):
    """Base exception for all application errors."""
    pass

# Category-specific exceptions
class ValidationError(ApplicationError):
    """Raised when data validation fails."""
    pass

class ProcessingError(ApplicationError):
    """Raised when processing fails."""
    pass

class ConfigurationError(ApplicationError):
    """Raised when configuration is invalid."""
    pass

# Component-specific exceptions
class ComponentError(ApplicationError):
    """Base exception for component errors."""
    def __init__(self, component_name: str, message: str):
        self.component_name = component_name
        super().__init__(f"[{component_name}] {message}")
```

### Configuration Patterns

#### Hierarchical Configuration
```python
# Configuration loading pattern
import json
import os
from typing import Dict, Any

class ConfigurationManager:
    def __init__(self, config_dir: str = "config"):
        self.config_dir = config_dir
        self.config = self._load_configuration()
    
    def _load_configuration(self) -> Dict[str, Any]:
        # Load base configuration
        base_config = self._load_config_file("project-config.json")
        
        # Load environment-specific overrides
        env = os.getenv("ENVIRONMENT", "development")
        env_config = self._load_config_file(f"{env}.json")
        
        # Merge configurations
        return self._merge_configs(base_config, env_config)
    
    def _load_config_file(self, filename: str) -> Dict[str, Any]:
        file_path = os.path.join(self.config_dir, filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}
    
    def _merge_configs(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        # Deep merge configuration dictionaries
        result = base.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_configs(result[key], value)
            else:
                result[key] = value
        return result
```

### Testing Patterns

#### Test Organization Pattern
```python
# Test base class
import unittest
from typing import Any, Dict

class ComponentTestBase(unittest.TestCase):
    """Base class for component tests."""
    
    def setUp(self):
        self.config = self._get_test_config()
        self.component = self._create_component()
    
    def _get_test_config(self) -> Dict[str, Any]:
        """Return test configuration."""
        return {
            "test_mode": True,
            "log_level": "DEBUG"
        }
    
    def _create_component(self):
        """Create component instance for testing."""
        raise NotImplementedError("Subclasses must implement _create_component")
    
    def test_component_health_check(self):
        """Test component health check."""
        health = self.component.health_check()
        self.assertEqual(health["status"], "healthy")
```

#### Reference Test Pattern
```python
# Reference test validation
class ReferenceTestCase(unittest.TestCase):
    """Test component with reference test case."""
    
    @classmethod
    def setUpClass(cls):
        cls.reference_input = cls._load_reference_input()
        cls.expected_output = cls._load_expected_output()
    
    def test_reference_case_processing(self):
        """Test component with reference test case."""
        component = self._create_component()
        actual_output = component.process(self.reference_input)
        
        # Validate output matches expected results
        self.assertEqual(actual_output, self.expected_output)
    
    @classmethod
    def _load_reference_input(cls):
        """Load reference input data."""
        # Implementation to load reference data
        pass
    
    @classmethod
    def _load_expected_output(cls):
        """Load expected output data."""
        # Implementation to load expected results
        pass
```

## Integration Guidelines

### Component Integration
- **Loose Coupling**: Components communicate through well-defined interfaces
- **Data Contracts**: Clear data format contracts between components
- **Error Propagation**: Consistent error handling across component boundaries
- **Configuration Isolation**: Each component manages its own configuration

### External Service Integration
- **Adapter Pattern**: Wrap external services with internal interfaces
- **Circuit Breaker**: Prevent cascade failures from external dependencies
- **Retry Logic**: Implement retry patterns for transient failures
- **Health Monitoring**: Monitor external service health and availability

### Database Integration (if applicable)
- **Repository Pattern**: Abstract database operations behind repositories
- **Connection Pooling**: Manage database connections efficiently
- **Migration Scripts**: Version-controlled database schema changes
- **Query Optimization**: Monitor and optimize database queries

## Development Workflow Integration

### Git Integration
- **Branch Naming**: `feature/component-name`, `bugfix/issue-description`
- **Commit Messages**: `feat(component): add new processing logic`
- **Pull Request Structure**: Clear description linking to requirements
- **Review Process**: Code review checklist including structure validation

### Documentation Integration
- **Code Documentation**: Inline documentation following conventions
- **API Documentation**: Auto-generated from code annotations
- **Architecture Decision Records**: Document significant structural decisions
- **Change Documentation**: Update documentation with structural changes

### Continuous Integration
- **Structure Validation**: Automated checks for naming conventions
- **Dependency Analysis**: Validate component dependencies
- **Test Organization**: Ensure tests follow organizational patterns
- **Documentation Updates**: Verify documentation stays current

## AI Behavior Guidelines

### Structure Enforcement
- **Follow Conventions**: Always use established naming and organization patterns
- **Validate Placement**: Ensure new files are placed in appropriate directories
- **Maintain Consistency**: Keep consistent patterns across similar components
- **Document Deviations**: Clearly document any necessary deviations from patterns

### Code Organization
- **Logical Grouping**: Group related functionality together
- **Clear Interfaces**: Define clear boundaries between modules
- **Minimize Dependencies**: Reduce coupling between components
- **Promote Reusability**: Identify and extract reusable patterns

### Quality Assurance
- **Structure Validation**: Validate structural decisions against requirements
- **Pattern Consistency**: Ensure consistent application of patterns
- **Documentation Currency**: Keep documentation synchronized with structure
- **Refactoring Guidance**: Suggest structural improvements when appropriate

---

**This structure steering guide ensures consistent project organization and architectural patterns throughout development, making the codebase maintainable and navigable for all team members.**