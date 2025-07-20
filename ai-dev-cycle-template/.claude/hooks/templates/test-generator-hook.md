# Test Generator Hook Template

**Purpose**: Automatically generate test files with appropriate structure and boilerplate for new source files.

**Trigger**: File creation events for source code files, triggered by `on-create.md` hook.

## Test Generation Strategy

### Language-Specific Templates

#### Python Test Generation
```python
# Template for Python test files
def generate_python_test(source_file_path, class_name=None, functions=None):
    """Generate pytest-compatible test file."""
    
    test_template = '''
import pytest
from unittest.mock import Mock, patch
from {module_path} import {imports}


class Test{class_name}:
    """Test suite for {class_name} class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Initialize test data and mock objects
        pass
    
    def teardown_method(self):
        """Clean up after each test method."""
        # Clean up resources
        pass
{test_methods}

{function_tests}


# Integration tests
class Test{class_name}Integration:
    """Integration tests for {class_name}."""
    
    def test_integration_workflow(self):
        """Test complete workflow integration."""
        # Test end-to-end functionality
        assert True  # Replace with actual integration test
        
        
# Performance tests  
class Test{class_name}Performance:
    """Performance tests for {class_name}."""
    
    @pytest.mark.performance
    def test_performance_benchmark(self):
        """Test performance benchmarks."""
        import time
        start_time = time.time()
        
        # Execute performance-critical code
        
        execution_time = time.time() - start_time
        assert execution_time < 1.0  # Performance threshold
'''
    
    # Generate test methods for each function
    method_tests = []
    if functions:
        for func in functions:
            method_tests.append(f'''
    def test_{func}_success(self):
        """Test {func} with valid input."""
        # Arrange
        # Act
        # Assert
        assert True  # Replace with actual test
        
    def test_{func}_invalid_input(self):
        """Test {func} with invalid input."""
        with pytest.raises(ValueError):
            # Test error handling
            pass
''')
    
    return test_template.format(
        module_path=get_module_path(source_file_path),
        imports=get_imports(source_file_path),
        class_name=class_name or get_class_name(source_file_path),
        test_methods=''.join(method_tests),
        function_tests=generate_function_tests(functions or [])
    )
```

#### JavaScript/TypeScript Test Generation
```javascript
// Template for Jest test files
function generateJavaScriptTest(sourceFilePath, componentName, functions) {
    const testTemplate = `
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { jest } from '@jest/globals';
import ${componentName} from './${getRelativePath(sourceFilePath)}';

describe('${componentName}', () => {
    // Setup and teardown
    beforeEach(() => {
        // Initialize test environment
        jest.clearAllMocks();
    });
    
    afterEach(() => {
        // Clean up after each test
    });
    
    // Component rendering tests
    describe('Component Rendering', () => {
        it('should render without crashing', () => {
            render(<${componentName} />);
            expect(screen.getByRole('main')).toBeInTheDocument();
        });
        
        it('should render with required props', () => {
            const props = {
                // Define required props
            };
            render(<${componentName} {...props} />);
            // Assertions
        });
    });
    
    // Interaction tests
    describe('User Interactions', () => {
        it('should handle user input correctly', async () => {
            render(<${componentName} />);
            
            const input = screen.getByRole('textbox');
            fireEvent.change(input, { target: { value: 'test' } });
            
            await waitFor(() => {
                expect(input.value).toBe('test');
            });
        });
    });
    
    // Props validation tests
    describe('Props Validation', () => {
        it('should handle missing props gracefully', () => {
            const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});
            render(<${componentName} />);
            expect(consoleSpy).not.toHaveBeenCalled();
            consoleSpy.mockRestore();
        });
    });
    
    // Accessibility tests
    describe('Accessibility', () => {
        it('should be accessible', () => {
            const { container } = render(<${componentName} />);
            // Add accessibility assertions
        });
    });
});

${generateFunctionTests(functions)}

// Performance tests
describe('${componentName} Performance', () => {
    it('should render efficiently', () => {
        const startTime = performance.now();
        render(<${componentName} />);
        const endTime = performance.now();
        
        expect(endTime - startTime).toBeLessThan(100); // 100ms threshold
    });
});
`;

    return testTemplate;
}
```

#### Go Test Generation
```go
// Template for Go test files
func generateGoTest(sourceFilePath, packageName, functions []string) string {
    testTemplate := `
package %s

import (
    "testing"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/mock"
    "github.com/stretchr/testify/suite"
)

// Test suite for %s
type %sTestSuite struct {
    suite.Suite
    // Add test fixtures here
}

func (suite *%sTestSuite) SetupTest() {
    // Set up test fixtures
}

func (suite *%sTestSuite) TearDownTest() {
    // Clean up after test
}

%s

// Benchmark tests
func Benchmark%s(b *testing.B) {
    for i := 0; i < b.N; i++ {
        // Benchmark code here
    }
}

// Example tests
func Example%s() {
    // Example usage
    // Output: expected output
}

func Test%sSuite(t *testing.T) {
    suite.Run(t, new(%sTestSuite))
}
`
    
    return fmt.Sprintf(testTemplate, 
        packageName, 
        packageName,
        strings.Title(packageName),
        strings.Title(packageName),
        strings.Title(packageName),
        generateGoFunctionTests(functions),
        strings.Title(packageName),
        strings.Title(packageName),
        strings.Title(packageName),
        strings.Title(packageName))
}
```

### Test Content Analysis

#### Source Code Analysis
```bash
# Analyze source file to generate appropriate tests
analyze_source_file() {
    local source_file="$1"
    local file_ext="${source_file##*.}"
    
    echo "🔍 Analyzing source file: $source_file"
    
    case $file_ext in
        "py")
            analyze_python_file "$source_file"
            ;;
        "js"|"ts"|"jsx"|"tsx")
            analyze_javascript_file "$source_file"
            ;;
        "go")
            analyze_go_file "$source_file"
            ;;
        *)
            echo "   ⚠️  Unsupported file type: $file_ext"
            return 1
            ;;
    esac
}

# Python file analysis
analyze_python_file() {
    local python_file="$1"
    
    echo "🐍 Analyzing Python file..."
    
    # Extract classes and functions using AST
    python << EOF
import ast
import json

with open('$python_file', 'r') as f:
    tree = ast.parse(f.read())

classes = []
functions = []

for node in ast.walk(tree):
    if isinstance(node, ast.ClassDef):
        methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
        classes.append({
            'name': node.name,
            'methods': methods,
            'line': node.lineno
        })
    elif isinstance(node, ast.FunctionDef) and node.col_offset == 0:
        functions.append({
            'name': node.name,
            'args': [arg.arg for arg in node.args.args],
            'line': node.lineno
        })

analysis = {
    'classes': classes,
    'functions': functions,
    'imports': []  # Could be extracted similarly
}

print(json.dumps(analysis, indent=2))
EOF
}

# JavaScript/TypeScript file analysis
analyze_javascript_file() {
    local js_file="$1"
    
    echo "🟨 Analyzing JavaScript/TypeScript file..."
    
    # Basic analysis using grep and sed
    local components=$(grep -n "^export.*function\|^function\|^const.*=.*=>" "$js_file" | head -10)
    local classes=$(grep -n "^class\|^export class" "$js_file")
    local hooks=$(grep -n "use[A-Z]" "$js_file")
    
    echo "   📊 Analysis results:"
    [ -n "$components" ] && echo "      Components/Functions found"
    [ -n "$classes" ] && echo "      Classes found"
    [ -n "$hooks" ] && echo "      React hooks detected"
    
    # Store analysis for test generation
    cat > "${js_file}.analysis.json" << EOF
{
    "type": "$([ -n "$hooks" ] && echo "react-component" || echo "javascript-module")",
    "components": $(echo "$components" | wc -l),
    "classes": $(echo "$classes" | wc -l),
    "hasHooks": $([ -n "$hooks" ] && echo "true" || echo "false")
}
EOF
}
```

### Test Structure Templates

#### Test Categories
```bash
# Generate different categories of tests
generate_test_categories() {
    local source_file="$1"
    local test_file="$2"
    
    echo "📝 Generating test categories for $source_file..."
    
    # Unit tests (always generated)
    generate_unit_tests "$source_file" "$test_file"
    
    # Integration tests (for API/service files)
    if [[ "$source_file" == *api* ]] || [[ "$source_file" == *service* ]]; then
        generate_integration_tests "$source_file" "$test_file"
    fi
    
    # Component tests (for UI components)
    if [[ "$source_file" == *component* ]] || [[ "$source_file" == *.jsx ]] || [[ "$source_file" == *.vue ]]; then
        generate_component_tests "$source_file" "$test_file"
    fi
    
    # Performance tests (for critical paths)
    if [[ "$source_file" == *core* ]] || [[ "$source_file" == *engine* ]]; then
        generate_performance_tests "$source_file" "$test_file"
    fi
    
    # Security tests (for auth/security modules)
    if [[ "$source_file" == *auth* ]] || [[ "$source_file" == *security* ]]; then
        generate_security_tests "$source_file" "$test_file"
    fi
}

# Unit test generation
generate_unit_tests() {
    local source_file="$1"
    local test_file="$2"
    
    cat >> "$test_file" << 'EOF'

// Unit Tests
describe('Unit Tests', () => {
    // Test individual functions and methods
    // Mock external dependencies
    // Focus on business logic
});
EOF
}

# Integration test generation
generate_integration_tests() {
    local source_file="$1"
    local test_file="$2"
    
    cat >> "$test_file" << 'EOF'

// Integration Tests
describe('Integration Tests', () => {
    // Test component interactions
    // Use real database/API calls where appropriate
    // Test data flow between components
});
EOF
}
```

### Domain-Specific Test Generation

#### Data Processing Tests
```python
def generate_data_processing_tests(source_file):
    """Generate tests specific to data processing modules."""
    
    template = '''
import pandas as pd
import numpy as np
from unittest.mock import patch
import tempfile
import os

class TestDataProcessing:
    """Tests for data processing functionality."""
    
    def setup_method(self):
        """Set up test data."""
        self.sample_data = pd.DataFrame({
            'column1': [1, 2, 3, 4, 5],
            'column2': ['a', 'b', 'c', 'd', 'e']
        })
        
        # Create temporary files for testing
        self.temp_dir = tempfile.mkdtemp()
        self.test_csv = os.path.join(self.temp_dir, 'test.csv')
        self.sample_data.to_csv(self.test_csv, index=False)
    
    def teardown_method(self):
        """Clean up test files."""
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)
        os.rmdir(self.temp_dir)
    
    def test_data_validation(self):
        """Test data validation rules."""
        # Test valid data
        assert validate_data(self.sample_data) == True
        
        # Test invalid data
        invalid_data = self.sample_data.copy()
        invalid_data.loc[0, 'column1'] = None
        assert validate_data(invalid_data) == False
    
    def test_data_transformation(self):
        """Test data transformation operations."""
        transformed = transform_data(self.sample_data)
        
        # Check output structure
        assert isinstance(transformed, pd.DataFrame)
        assert len(transformed) > 0
        
        # Check data quality
        assert not transformed.isnull().any().any()
    
    def test_edge_cases(self):
        """Test edge cases and error handling."""
        # Empty data
        empty_df = pd.DataFrame()
        with pytest.raises(ValueError):
            process_data(empty_df)
        
        # Malformed data
        bad_data = pd.DataFrame({'col': ['not', 'numeric', 'data']})
        with pytest.raises(TypeError):
            process_numeric_data(bad_data)
    
    @pytest.mark.performance
    def test_large_dataset_performance(self):
        """Test performance with large datasets."""
        large_data = pd.DataFrame({
            'col1': np.random.randn(100000),
            'col2': np.random.choice(['A', 'B', 'C'], 100000)
        })
        
        start_time = time.time()
        result = process_data(large_data)
        execution_time = time.time() - start_time
        
        assert execution_time < 10.0  # Should complete within 10 seconds
        assert len(result) == len(large_data)
'''
    
    return template
```

#### API Integration Tests
```javascript
function generateApiIntegrationTests(sourceFile) {
    return `
import request from 'supertest';
import app from '../app';
import { jest } from '@jest/globals';

describe('API Integration Tests', () => {
    beforeAll(async () => {
        // Set up test database
        await setupTestDatabase();
    });
    
    afterAll(async () => {
        // Clean up test database
        await cleanupTestDatabase();
    });
    
    beforeEach(async () => {
        // Reset test data
        await resetTestData();
    });
    
    describe('Authentication', () => {
        it('should require authentication', async () => {
            const response = await request(app)
                .get('/api/protected')
                .expect(401);
            
            expect(response.body.error).toBe('Authentication required');
        });
        
        it('should accept valid tokens', async () => {
            const token = await getValidTestToken();
            
            const response = await request(app)
                .get('/api/protected')
                .set('Authorization', \`Bearer \${token}\`)
                .expect(200);
        });
    });
    
    describe('API Endpoints', () => {
        it('should handle CRUD operations', async () => {
            const token = await getValidTestToken();
            
            // Create
            const createResponse = await request(app)
                .post('/api/items')
                .set('Authorization', \`Bearer \${token}\`)
                .send({ name: 'Test Item' })
                .expect(201);
            
            const itemId = createResponse.body.id;
            
            // Read
            await request(app)
                .get(\`/api/items/\${itemId}\`)
                .set('Authorization', \`Bearer \${token}\`)
                .expect(200);
            
            // Update
            await request(app)
                .put(\`/api/items/\${itemId}\`)
                .set('Authorization', \`Bearer \${token}\`)
                .send({ name: 'Updated Item' })
                .expect(200);
            
            // Delete
            await request(app)
                .delete(\`/api/items/\${itemId}\`)
                .set('Authorization', \`Bearer \${token}\`)
                .expect(204);
        });
        
        it('should handle error scenarios', async () => {
            const token = await getValidTestToken();
            
            // Not found
            await request(app)
                .get('/api/items/nonexistent')
                .set('Authorization', \`Bearer \${token}\`)
                .expect(404);
            
            // Bad request
            await request(app)
                .post('/api/items')
                .set('Authorization', \`Bearer \${token}\`)
                .send({ invalid: 'data' })
                .expect(400);
        });
    });
    
    describe('Rate Limiting', () => {
        it('should enforce rate limits', async () => {
            const token = await getValidTestToken();
            
            // Make multiple requests rapidly
            const promises = Array(20).fill().map(() =>
                request(app)
                    .get('/api/items')
                    .set('Authorization', \`Bearer \${token}\`)
            );
            
            const responses = await Promise.all(promises);
            
            // Some requests should be rate limited
            const rateLimitedResponses = responses.filter(r => r.status === 429);
            expect(rateLimitedResponses.length).toBeGreaterThan(0);
        });
    });
});
`;
}
```

### Test Quality Assurance

#### Test Completeness Validation
```bash
# Validate generated test completeness
validate_test_completeness() {
    local test_file="$1"
    local source_file="$2"
    
    echo "✅ Validating test completeness..."
    
    # Check for essential test patterns
    local has_setup=$(grep -c "setup\|beforeEach\|SetupTest" "$test_file")
    local has_teardown=$(grep -c "teardown\|afterEach\|TeardownTest" "$test_file")
    local has_assertions=$(grep -c "assert\|expect\|Assert" "$test_file")
    local has_error_handling=$(grep -c "raises\|throw\|Error" "$test_file")
    
    echo "   📊 Test completeness check:"
    echo "      Setup/teardown: $([ "$has_setup" -gt 0 ] && [ "$has_teardown" -gt 0 ] && echo "✅" || echo "⚠️")"
    echo "      Assertions: $([ "$has_assertions" -gt 3 ] && echo "✅" || echo "⚠️")"
    echo "      Error handling: $([ "$has_error_handling" -gt 0 ] && echo "✅" || echo "⚠️")"
    
    # Generate test quality report
    cat > "${test_file}.quality-report.json" << EOF
{
    "generated_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
    "source_file": "$source_file",
    "test_file": "$test_file",
    "completeness": {
        "has_setup_teardown": $([ "$has_setup" -gt 0 ] && [ "$has_teardown" -gt 0 ] && echo "true" || echo "false"),
        "assertion_count": $has_assertions,
        "has_error_handling": $([ "$has_error_handling" -gt 0 ] && echo "true" || echo "false")
    },
    "recommendations": [
        $([ "$has_assertions" -lt 3 ] && echo "\"Add more test assertions\"," || echo "")
        $([ "$has_error_handling" -eq 0 ] && echo "\"Add error handling tests\"," || echo "")
        $([ "$has_setup" -eq 0 ] && echo "\"Add test setup methods\"," || echo "")
        "\"Review generated tests and customize for specific requirements\""
    ]
}
EOF
}
```

## Integration with Steering System

### Context-Aware Test Generation
```bash
# Apply steering system context to test generation
apply_steering_context() {
    local source_file="$1"
    local project_context="$2"
    
    echo "🧭 Applying steering system context..."
    
    # Load project-specific test requirements
    if [ -f ".claude/steering/testing.md" ]; then
        echo "   📋 Loading project testing standards..."
        
        # Extract testing requirements from steering
        local coverage_requirement=$(grep -o "coverage.*[0-9]*%" .claude/steering/testing.md | head -1)
        local test_framework=$(grep -o "pytest\|jest\|mocha\|go test" .claude/steering/testing.md | head -1)
        
        echo "      Coverage requirement: ${coverage_requirement:-"80%"}"
        echo "      Test framework: ${test_framework:-"auto-detect"}"
    fi
    
    # Apply domain-specific test patterns
    case "$project_context" in
        "data_processing")
            echo "   🔬 Applying data processing test patterns"
            add_data_validation_tests "$source_file"
            ;;
        "api_integration")
            echo "   🌐 Applying API integration test patterns"
            add_api_contract_tests "$source_file"
            ;;
        "web_application")
            echo "   🌍 Applying web application test patterns"
            add_accessibility_tests "$source_file"
            ;;
    esac
}
```

## AI Behavior Guidelines

### Test Generation Strategy
- Analyze source code structure to generate appropriate tests
- Include multiple test categories (unit, integration, performance)
- Follow project-specific testing conventions and frameworks
- Generate meaningful test names and descriptions

### Quality Standards
- Ensure comprehensive test coverage for generated tests
- Include error handling and edge case testing
- Add performance benchmarks for critical code
- Follow testing best practices and patterns

### Customization and Adaptation
- Adapt to project-specific testing frameworks
- Integrate with existing test infrastructure
- Respect project coding standards and conventions
- Generate tests that integrate with CI/CD pipelines

---

**This test generator hook template provides comprehensive, intelligent test generation that adapts to different programming languages, project contexts, and quality requirements while maintaining consistency with project standards.**