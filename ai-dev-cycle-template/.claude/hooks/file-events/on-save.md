# On File Save Hook

**Purpose**: Automatic validation and quality checks triggered when files are saved.

**Trigger**: File save events in the development environment.

## Hook Configuration

### File Pattern Matching
- **Source Code** (`*.py`, `*.js`, `*.ts`, `*.go`): Run linting, formatting, and security checks
- **Test Files** (`*test*.py`, `*.test.js`, `*_test.go`): Execute test validation and coverage analysis
- **Documentation** (`*.md`, `*.rst`): Check formatting, links, and content validation
- **Configuration** (`*.json`, `*.yaml`, `*.toml`): Validate syntax and schema compliance

## Immediate Validation Actions

### Code Quality Checks
```bash
# Python files
if [[ "$file_path" == *.py ]]; then
    # Format with black
    black "$file_path" --check --quiet
    
    # Lint with flake8
    flake8 "$file_path"
    
    # Type checking with mypy
    mypy "$file_path" --ignore-missing-imports
    
    # Security scanning with bandit
    bandit -r "$file_path" -f json
fi

# JavaScript/TypeScript files
if [[ "$file_path" == *.{js,ts,jsx,tsx} ]]; then
    # Format with prettier
    prettier --check "$file_path"
    
    # Lint with eslint
    eslint "$file_path" --format json
    
    # Type checking for TypeScript
    if [[ "$file_path" == *.{ts,tsx} ]]; then
        tsc --noEmit "$file_path"
    fi
fi
```

### Security Validation
```bash
# Scan for secrets and sensitive data
if [[ "$file_path" == src/*.{py,js,ts,go} ]]; then
    # Check for API keys, passwords, tokens
    grep -E "(api_key|password|secret|token)" "$file_path" && \
        echo "⚠️  Potential secret detected in $file_path"
    
    # Check for hardcoded credentials
    grep -E "(localhost|127\.0\.0\.1):[0-9]+" "$file_path" && \
        echo "⚠️  Hardcoded localhost connection in $file_path"
fi
```

### Documentation Synchronization
```bash
# Update documentation when source files change
if [[ "$file_path" == src/*.{py,js,ts} ]]; then
    # Extract docstrings/comments for API documentation
    # Update README if public API changed
    # Regenerate type definitions if applicable
    echo "📖 Updating documentation for $file_path"
fi
```

## Automated Quality Gates

### Test Execution
```bash
# Run related tests when source files change
if [[ "$file_path" == src/*.py ]]; then
    test_file="tests/unit/${filename%.*}_test.py"
    if [ -f "$test_file" ]; then
        pytest "$test_file" -v --tb=short
        echo "🧪 Tests executed for $file_path"
    else
        echo "⚠️  No test file found for $file_path"
    fi
fi
```

### Performance Monitoring
```bash
# Check file size and complexity
file_size=$(wc -c < "$file_path")
line_count=$(wc -l < "$file_path")

if [ "$file_size" -gt 10000 ]; then
    echo "📏 Large file detected: $file_path ($file_size bytes)"
fi

if [ "$line_count" -gt 500 ]; then
    echo "📏 Long file detected: $file_path ($line_count lines)"
    echo "   Consider refactoring into smaller modules"
fi
```

## Hook Templates to Execute

### Always Execute
- `security-scanner-hook.md` - Security vulnerability scanning
- `doc-updater-hook.md` - Documentation synchronization

### Conditional Based on File Type
- **Source Files**: Code quality validation, test execution
- **Test Files**: Test validation, coverage analysis
- **API Files**: API documentation updates, contract validation
- **Configuration Files**: Schema validation, environment checks

## Integration with Steering System

### Context-Aware Validation
```json
{
  "file_save_hooks": {
    "*.py": {
      "quality_checks": ["black", "flake8", "mypy", "bandit"],
      "test_execution": true,
      "documentation_update": true,
      "domain_specific": {
        "data_processing": ["data_quality_validation"],
        "api_integration": ["api_contract_validation"]
      }
    },
    "*.md": {
      "quality_checks": ["markdown_lint", "link_validation"],
      "spell_check": true,
      "table_of_contents_update": true
    }
  }
}
```

### Performance Thresholds
```json
{
  "performance_gates": {
    "max_file_size": 50000,
    "max_line_count": 1000,
    "max_function_length": 50,
    "max_complexity": 10
  }
}
```

## Error Handling and Recovery

### Validation Failures
```bash
# Handle linting failures
if ! flake8 "$file_path"; then
    echo "❌ Linting failed for $file_path"
    echo "   Run 'flake8 $file_path' to see details"
    echo "   Consider auto-fixing with 'autopep8 $file_path'"
fi

# Handle test failures
if ! pytest "$test_file"; then
    echo "❌ Tests failed for $file_path"
    echo "   Review test results and fix implementation"
    echo "   Run 'pytest $test_file -v' for detailed output"
fi
```

### Graceful Degradation
```bash
# Continue with warnings if non-critical checks fail
check_code_quality() {
    if command -v flake8 >/dev/null 2>&1; then
        flake8 "$file_path" || echo "⚠️  Code quality check completed with warnings"
    else
        echo "⚠️  flake8 not installed, skipping code quality check"
    fi
}
```

## Real-time Feedback

### Success Indicators
```bash
echo "✅ File saved successfully: $file_path"
echo "   - Code quality: PASSED"
echo "   - Security scan: PASSED" 
echo "   - Tests: PASSED (3/3)"
echo "   - Documentation: UPDATED"
```

### Warning Indicators
```bash
echo "⚠️  File saved with warnings: $file_path"
echo "   - Code quality: 2 style issues"
echo "   - Security scan: PASSED"
echo "   - Tests: PASSED (3/3)"
echo "   - Documentation: NEEDS UPDATE"
```

### Error Indicators
```bash
echo "❌ File saved with errors: $file_path"
echo "   - Code quality: FAILED (syntax error)"
echo "   - Security scan: BLOCKED (potential secret)"
echo "   - Tests: FAILED (1/3)"
echo "   - Action required before commit"
```

## AI Behavior Guidelines

### Validation Priority
1. **Security**: Highest priority - block dangerous patterns
2. **Syntax**: Critical - ensure code compiles/runs
3. **Style**: Important - maintain consistency
4. **Performance**: Monitor - suggest optimizations
5. **Documentation**: Maintain - keep synchronized

### Integration Behavior
- Respect project-specific quality standards
- Use established tooling and configurations
- Provide actionable feedback and suggestions
- Maintain development flow without blocking unnecessarily

### Continuous Learning
- Track common validation failures
- Suggest process improvements
- Update hook behavior based on project evolution
- Learn from team preferences and exceptions

---

**This hook provides immediate feedback and quality assurance on every file save, ensuring consistent code quality and security throughout the development process.**