# Pre-Commit Hook

**Purpose**: Comprehensive validation and quality assurance before code commits.

**Trigger**: Git pre-commit event or manual pre-commit validation request.

## Validation Pipeline

### Stage 1: Code Quality and Standards
```bash
# Python code quality
validate_python_code() {
    echo "🐍 Validating Python code quality..."
    
    # Format check with black
    black --check --diff src/ tests/ || {
        echo "❌ Code formatting issues found"
        echo "   Run: black src/ tests/ to auto-format"
        return 1
    }
    
    # Linting with flake8
    flake8 src/ tests/ || {
        echo "❌ Linting issues found"
        echo "   Review flake8 output and fix issues"
        return 1
    }
    
    # Type checking with mypy
    mypy src/ || {
        echo "❌ Type checking failed"
        echo "   Add type annotations and fix type errors"
        return 1
    }
    
    echo "✅ Python code quality validation passed"
}

# JavaScript/TypeScript code quality
validate_js_code() {
    echo "🟨 Validating JavaScript/TypeScript code quality..."
    
    # Format check with prettier
    prettier --check "src/**/*.{js,ts,jsx,tsx}" || {
        echo "❌ Code formatting issues found"
        echo "   Run: prettier --write \"src/**/*.{js,ts,jsx,tsx}\""
        return 1
    }
    
    # Linting with eslint
    eslint "src/**/*.{js,ts,jsx,tsx}" || {
        echo "❌ ESLint issues found"
        echo "   Run: eslint --fix \"src/**/*.{js,ts,jsx,tsx}\""
        return 1
    }
    
    # TypeScript compilation check
    if [ -f "tsconfig.json" ]; then
        tsc --noEmit || {
            echo "❌ TypeScript compilation failed"
            echo "   Fix TypeScript errors before committing"
            return 1
        }
    fi
    
    echo "✅ JavaScript/TypeScript code quality validation passed"
}
```

### Stage 2: Security Scanning
```bash
# Security vulnerability scanning
security_scan() {
    echo "🔒 Performing security scan..."
    
    # Python security with bandit
    if [ -d "src" ] && find src -name "*.py" | grep -q .; then
        bandit -r src/ -f json -o security-report.json || {
            echo "⚠️  Security vulnerabilities detected"
            echo "   Review security-report.json for details"
        }
    fi
    
    # Secrets detection
    check_secrets() {
        echo "🔍 Checking for secrets and sensitive data..."
        
        # Check for common secret patterns
        if grep -r -E "(api_key|password|secret|token|private_key)" \
           --include="*.py" --include="*.js" --include="*.ts" \
           --include="*.json" --include="*.yaml" src/ 2>/dev/null; then
            echo "❌ Potential secrets detected in source code"
            echo "   Remove hardcoded secrets before committing"
            echo "   Use environment variables or secure configuration"
            return 1
        fi
        
        # Check for development/test URLs in production code
        if grep -r -E "(localhost|127\.0\.0\.1|test\.com|dev\.)" \
           --include="*.py" --include="*.js" --include="*.ts" src/ 2>/dev/null; then
            echo "⚠️  Development URLs found in source code"
            echo "   Ensure no hardcoded development endpoints"
        fi
        
        echo "✅ No obvious secrets detected"
    }
    
    check_secrets || return 1
}
```

### Stage 3: Test Validation
```bash
# Comprehensive test execution
run_tests() {
    echo "🧪 Running test suite..."
    
    # Python tests with pytest
    if [ -f "pytest.ini" ] || [ -f "pyproject.toml" ] || [ -d "tests" ]; then
        pytest tests/ -v --tb=short --cov=src --cov-report=term-missing || {
            echo "❌ Python tests failed"
            echo "   Fix failing tests before committing"
            return 1
        }
        
        # Coverage threshold check
        coverage report --fail-under=80 || {
            echo "⚠️  Test coverage below 80%"
            echo "   Add tests to improve coverage"
        }
    fi
    
    # JavaScript tests with npm/yarn
    if [ -f "package.json" ]; then
        if command -v npm >/dev/null 2>&1; then
            npm test -- --passWithNoTests --watchAll=false || {
                echo "❌ JavaScript tests failed"
                echo "   Fix failing tests before committing"
                return 1
            }
        fi
    fi
    
    echo "✅ Test suite validation passed"
}
```

### Stage 4: Documentation Validation
```bash
# Documentation and API validation
validate_documentation() {
    echo "📖 Validating documentation..."
    
    # Check README.md exists and is up to date
    if [ ! -f "README.md" ]; then
        echo "⚠️  README.md not found"
        echo "   Create a README.md file documenting your project"
    fi
    
    # Validate markdown files
    if command -v markdownlint >/dev/null 2>&1; then
        markdownlint "**/*.md" || {
            echo "⚠️  Markdown formatting issues found"
            echo "   Fix markdown formatting before committing"
        }
    fi
    
    # Check for broken links in documentation
    check_doc_links() {
        echo "🔗 Checking documentation links..."
        
        # Basic link validation (can be enhanced with tools like markdown-link-check)
        if grep -r "\[.*\](.*)" --include="*.md" . 2>/dev/null | grep -E "\[.*\]\(http"; then
            echo "ℹ️  External links found - consider validating manually"
        fi
    }
    
    check_doc_links
    echo "✅ Documentation validation completed"
}
```

### Stage 5: Dependency and Configuration Validation
```bash
# Dependency and configuration checks
validate_dependencies() {
    echo "📦 Validating dependencies and configuration..."
    
    # Python dependency validation
    if [ -f "requirements.txt" ]; then
        # Check for security vulnerabilities in dependencies
        if command -v safety >/dev/null 2>&1; then
            safety check || {
                echo "⚠️  Security vulnerabilities in Python dependencies"
                echo "   Update vulnerable packages"
            }
        fi
        
        # Check for unused dependencies
        if command -v pip-audit >/dev/null 2>&1; then
            pip-audit || {
                echo "⚠️  Dependency audit issues found"
            }
        fi
    fi
    
    # JavaScript dependency validation
    if [ -f "package.json" ]; then
        # Check for vulnerabilities
        if command -v npm >/dev/null 2>&1; then
            npm audit --audit-level=high || {
                echo "⚠️  High-severity vulnerabilities in JavaScript dependencies"
                echo "   Run: npm audit fix"
            }
        fi
    fi
    
    # Configuration file validation
    validate_config_files() {
        echo "⚙️  Validating configuration files..."
        
        # JSON syntax validation
        for json_file in $(find . -name "*.json" -not -path "./node_modules/*" -not -path "./.git/*"); do
            if ! python -m json.tool "$json_file" >/dev/null 2>&1; then
                echo "❌ Invalid JSON syntax in $json_file"
                return 1
            fi
        done
        
        # YAML syntax validation
        if command -v yamllint >/dev/null 2>&1; then
            yamllint . || {
                echo "⚠️  YAML formatting issues found"
            }
        fi
        
        echo "✅ Configuration files are valid"
    }
    
    validate_config_files || return 1
}
```

## Integration with Steering System

### Context-Aware Validation
```bash
# Apply domain-specific validation rules
apply_context_validation() {
    local project_type=$(detect_project_type)
    
    case $project_type in
        "data_processing")
            echo "🔬 Applying data processing validations..."
            validate_data_schemas
            check_data_quality_tests
            ;;
        "api_integration")
            echo "🌐 Applying API integration validations..."
            validate_api_contracts
            check_integration_tests
            ;;
        "web_application")
            echo "🌍 Applying web application validations..."
            validate_accessibility_tests
            check_security_headers
            ;;
    esac
}

# Detect project type from steering configuration
detect_project_type() {
    if [ -f ".claude/steering-config.json" ]; then
        # Extract project type from steering configuration
        python -c "
import json
with open('.claude/steering-config.json', 'r') as f:
    config = json.load(f)
    # Logic to determine project type based on configuration
"
    fi
}
```

### Quality Gate Configuration
```json
{
  "pre_commit_gates": {
    "mandatory": [
      "code_quality",
      "security_scan",
      "test_execution"
    ],
    "recommended": [
      "documentation_validation",
      "dependency_check"
    ],
    "context_specific": {
      "data_processing": ["data_quality_validation"],
      "api_integration": ["api_contract_validation"],
      "web_application": ["accessibility_validation"]
    }
  }
}
```

## Error Handling and Recovery

### Graceful Failure Handling
```bash
# Handle validation failures gracefully
handle_validation_failure() {
    local validation_step="$1"
    local exit_code="$2"
    
    echo "❌ Pre-commit validation failed at: $validation_step"
    echo ""
    echo "🔧 Recovery actions:"
    
    case $validation_step in
        "code_quality")
            echo "   1. Run auto-formatters: black src/ && prettier --write \"src/**/*.js\""
            echo "   2. Fix linting issues: flake8 src/ && eslint src/"
            echo "   3. Add type annotations if using TypeScript/mypy"
            ;;
        "security_scan")
            echo "   1. Remove hardcoded secrets and credentials"
            echo "   2. Use environment variables for configuration"
            echo "   3. Update vulnerable dependencies"
            ;;
        "test_execution")
            echo "   1. Fix failing tests"
            echo "   2. Add tests for new functionality"
            echo "   3. Ensure test coverage meets requirements"
            ;;
        "documentation")
            echo "   1. Update README.md with recent changes"
            echo "   2. Add documentation for new features"
            echo "   3. Fix markdown formatting issues"
            ;;
    esac
    
    echo ""
    echo "Run 'git commit' again after addressing the issues."
    exit $exit_code
}
```

### Bypass Mechanism
```bash
# Emergency bypass for critical commits
check_bypass_flag() {
    if git log -1 --pretty=%B | grep -q "BYPASS_HOOKS"; then
        echo "⚠️  Pre-commit hooks bypassed - use with caution"
        echo "   Ensure manual validation before pushing"
        exit 0
    fi
}
```

## Performance Optimization

### Parallel Execution
```bash
# Run independent validations in parallel
run_parallel_validations() {
    echo "🚀 Running parallel validations..."
    
    # Start background processes
    validate_python_code &
    PID_PYTHON=$!
    
    validate_js_code &
    PID_JS=$!
    
    security_scan &
    PID_SECURITY=$!
    
    # Wait for all processes to complete
    wait $PID_PYTHON $PID_JS $PID_SECURITY
    
    # Check exit codes
    if [ $? -ne 0 ]; then
        echo "❌ One or more validations failed"
        return 1
    fi
    
    echo "✅ Parallel validations completed successfully"
}
```

### Incremental Validation
```bash
# Only validate changed files for performance
validate_changed_files_only() {
    local changed_files=$(git diff --cached --name-only)
    
    echo "📝 Validating only changed files for performance..."
    
    # Filter by file type and validate accordingly
    echo "$changed_files" | grep "\.py$" | xargs -r flake8
    echo "$changed_files" | grep "\.js$\|\.ts$" | xargs -r eslint
    
    echo "✅ Changed files validation completed"
}
```

## Integration with CI/CD

### CI Environment Detection
```bash
# Adjust validation for CI environment
if [ "$CI" = "true" ]; then
    echo "🤖 Running in CI environment - full validation mode"
    VALIDATION_MODE="full"
else
    echo "💻 Running in local environment - optimized validation mode"
    VALIDATION_MODE="incremental"
fi
```

### Pre-Push Validation
```bash
# Additional checks before pushing to remote
pre_push_validation() {
    echo "🚀 Running pre-push validation..."
    
    # Check branch naming convention
    current_branch=$(git branch --show-current)
    if [[ ! "$current_branch" =~ ^(feature|bugfix|hotfix|release)/.+ ]]; then
        echo "⚠️  Branch naming convention: use feature/, bugfix/, hotfix/, or release/"
    fi
    
    # Check commit message format
    commit_msg=$(git log -1 --pretty=%B)
    if [[ ! "$commit_msg" =~ ^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+ ]]; then
        echo "⚠️  Consider using conventional commit format"
    fi
    
    echo "✅ Pre-push validation completed"
}
```

## AI Behavior Guidelines

### Validation Strategy
- Prioritize security and correctness over style
- Provide clear, actionable error messages
- Suggest automatic fixes when possible
- Balance thoroughness with performance

### User Experience
- Clear progress indicators during validation
- Helpful recovery guidance for failures
- Option to bypass in emergency situations
- Integration with development workflow

### Continuous Improvement
- Learn from common validation failures
- Update rules based on project evolution
- Suggest process improvements
- Track validation effectiveness

---

**This comprehensive pre-commit hook ensures code quality, security, and reliability while providing clear feedback and recovery guidance for development teams.**