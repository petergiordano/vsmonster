# Workflow Orchestrator Command

## Purpose
Automate complex multi-step development workflows by orchestrating sequences of tasks with intelligent decision-making and error handling.

## Usage
```
@workflow-orchestrator [workflow-name] [options]
```

## Available Workflows

### 1. Feature Implementation Workflow
```
@workflow-orchestrator feature-implementation --spec "Add user authentication"
```

**Steps**:
1. Generate requirements from specification
2. Create technical design document
3. Generate task breakdown with dependencies
4. Create file structure and boilerplate
5. Implement core functionality
6. Generate tests automatically
7. Update documentation
8. Run validation suite

### 2. Bug Fix Workflow
```
@workflow-orchestrator bug-fix --issue "Login fails on mobile devices"
```

**Steps**:
1. Analyze bug description and impact
2. Identify affected components
3. Create reproduction test case
4. Implement fix with minimal changes
5. Verify fix doesn't break existing tests
6. Update regression test suite
7. Document fix in changelog

### 3. Refactoring Workflow
```
@workflow-orchestrator refactor --target "src/api/" --pattern "repository-pattern"
```

**Steps**:
1. Analyze current code structure
2. Identify refactoring opportunities
3. Create safety test harness
4. Perform incremental refactoring
5. Verify behavior preservation
6. Update documentation
7. Optimize performance if needed

### 4. API Integration Workflow
```
@workflow-orchestrator api-integration --service "stripe" --operations "payment,subscription"
```

**Steps**:
1. Generate API client from specification
2. Create type definitions
3. Implement service wrapper
4. Add error handling and retry logic
5. Create integration tests
6. Add monitoring and logging
7. Update API documentation

### 5. Performance Optimization Workflow
```
@workflow-orchestrator performance --target "dashboard" --metric "load-time"
```

**Steps**:
1. Profile current performance
2. Identify bottlenecks
3. Generate optimization plan
4. Implement improvements
5. Measure performance gains
6. Add performance tests
7. Document optimizations

## Workflow Configuration

### Custom Workflow Definition
Create `.claude/workflows/custom-workflow.json`:

```json
{
  "name": "custom-workflow",
  "description": "Custom development workflow",
  "steps": [
    {
      "id": "analyze",
      "name": "Analyze Requirements",
      "command": "@context-analyzer",
      "inputs": ["specification"],
      "outputs": ["analysis_report"],
      "on_failure": "abort"
    },
    {
      "id": "design",
      "name": "Generate Design",
      "command": "@generate-design",
      "inputs": ["analysis_report"],
      "outputs": ["design_doc"],
      "on_failure": "retry",
      "retry_count": 2
    },
    {
      "id": "implement",
      "name": "Implement Solution",
      "command": "@implement-feature",
      "inputs": ["design_doc"],
      "outputs": ["implementation"],
      "parallel": true,
      "on_failure": "rollback"
    },
    {
      "id": "test",
      "name": "Generate and Run Tests",
      "command": "@generate-tests",
      "inputs": ["implementation"],
      "outputs": ["test_results"],
      "on_failure": "fix_and_retry"
    },
    {
      "id": "validate",
      "name": "Validate Quality",
      "command": "@quality-assessor",
      "inputs": ["implementation", "test_results"],
      "outputs": ["quality_report"],
      "on_failure": "escalate"
    }
  ],
  "error_handlers": {
    "rollback": {
      "action": "git checkout -- .",
      "notify": true
    },
    "fix_and_retry": {
      "action": "@auto-fix-tests",
      "max_attempts": 3
    },
    "escalate": {
      "action": "request_user_input",
      "message": "Quality validation failed. Manual intervention required."
    }
  },
  "success_actions": [
    "commit_changes",
    "update_documentation",
    "notify_completion"
  ]
}
```

## Options

### Global Options
- `--dry-run`: Preview workflow steps without execution
- `--verbose`: Show detailed progress information
- `--checkpoint`: Save progress after each step
- `--resume`: Resume from last checkpoint
- `--parallel`: Run independent steps in parallel
- `--timeout <minutes>`: Set maximum workflow duration

### Execution Modes
- `--mode autopilot`: Run fully autonomous (default for low-risk workflows)
- `--mode supervised`: Require approval for each step
- `--mode hybrid`: Auto-run safe steps, supervise risky ones

### Quality Gates
- `--strict`: Fail on any quality issues
- `--lenient`: Continue with warnings
- `--custom-gates <file>`: Use custom quality gate configuration

## Advanced Features

### Conditional Execution
```yaml
conditions:
  - if: "test_coverage < 80%"
    then: "add_more_tests"
  - if: "complexity > 10"
    then: "suggest_refactoring"
  - if: "security_issues > 0"
    then: "abort_workflow"
```

### Parallel Execution
```yaml
parallel_groups:
  - group: "independent_features"
    steps: ["auth_implementation", "ui_implementation", "api_implementation"]
    max_parallel: 3
  - group: "test_suite"
    steps: ["unit_tests", "integration_tests", "e2e_tests"]
    max_parallel: 2
```

### Rollback Strategy
```yaml
rollback:
  strategy: "checkpoint"
  checkpoints:
    - after: "design"
    - after: "core_implementation"
    - before: "deployment"
  cleanup_actions:
    - "remove_temp_files"
    - "reset_test_data"
    - "notify_team"
```

## Integration with Other Commands

### Pre-workflow Commands
- `@context-analyzer`: Understand project state
- `@dependency-mapper`: Identify component relationships
- `@quality-assessor`: Baseline quality metrics

### During Workflow
- `@generate-tasks`: Create granular task breakdowns
- `@validate-steering`: Ensure AI has correct context
- `@hook-executor`: Trigger automated actions

### Post-workflow Commands
- `@production-readiness`: Verify deployment readiness
- `@update-documentation`: Sync all documentation
- `@notify-stakeholders`: Send completion reports

## Error Handling

### Common Errors and Solutions

1. **Dependency Conflict**
   - Auto-resolution attempt
   - Suggest manual resolution
   - Rollback if critical

2. **Test Failure**
   - Analyze failure pattern
   - Attempt auto-fix
   - Generate fix suggestion

3. **Performance Regression**
   - Compare with baseline
   - Suggest optimizations
   - Option to proceed with warning

4. **Security Issue**
   - Immediate workflow halt
   - Generate security report
   - Require manual approval

## Monitoring and Reporting

### Progress Tracking
```
Workflow: Feature Implementation
Status: In Progress (Step 4/8)
Duration: 12 minutes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50%

✓ Requirements Generated
✓ Design Document Created
✓ Tasks Breakdown Complete
→ Implementing Core Features...
  - UserService: 80% complete
  - AuthController: 60% complete
  - Database Schema: 100% complete
□ Generate Tests
□ Update Documentation
□ Run Validation Suite
□ Prepare for Review

Estimated Time Remaining: 8 minutes
```

### Final Report
```
Workflow Completed Successfully!
═══════════════════════════════════════════════════

Summary:
- Total Duration: 22 minutes
- Files Created: 12
- Files Modified: 8
- Tests Added: 24
- Coverage: 87%
- Quality Score: A

Key Achievements:
✓ User authentication implemented
✓ 100% API endpoint coverage
✓ Security best practices applied
✓ Documentation updated
✓ All tests passing

Recommendations:
- Consider adding rate limiting
- Implement session management
- Add monitoring for auth failures

Next Steps:
1. Review generated PR: #142
2. Deploy to staging environment
3. Run integration tests
```

## Best Practices

### Workflow Design
1. **Keep Steps Atomic**: Each step should do one thing well
2. **Handle Errors Gracefully**: Always have fallback strategies
3. **Save Progress**: Enable checkpoint recovery
4. **Validate Early**: Catch issues before they compound
5. **Document Decisions**: Record why choices were made

### Performance Optimization
1. **Parallelize When Possible**: Run independent steps concurrently
2. **Cache Intermediate Results**: Avoid redundant work
3. **Set Reasonable Timeouts**: Prevent infinite loops
4. **Monitor Resource Usage**: Stay within system limits
5. **Optimize Critical Paths**: Focus on bottlenecks

## Examples

### Example 1: Full Feature Implementation
```bash
@workflow-orchestrator feature-implementation \
  --spec "Add real-time notifications" \
  --mode hybrid \
  --checkpoint \
  --parallel \
  --strict
```

### Example 2: Emergency Bug Fix
```bash
@workflow-orchestrator bug-fix \
  --issue "Critical: Payment processing fails" \
  --mode supervised \
  --priority high \
  --notify-team
```

### Example 3: API Migration
```bash
@workflow-orchestrator api-integration \
  --service "aws-s3" \
  --migrate-from "local-storage" \
  --dry-run
```

## Troubleshooting

### Workflow Stuck
1. Check `claude/logs/workflow.log` for details
2. Use `--resume` to continue from checkpoint
3. Try `--verbose` mode for more information
4. Manually complete step and continue

### Quality Gate Failures
1. Review quality report for specific issues
2. Use `--lenient` mode if appropriate
3. Fix issues and re-run workflow
4. Consider adjusting quality thresholds

### Performance Issues
1. Reduce parallel execution count
2. Enable caching for expensive operations
3. Break large workflows into smaller ones
4. Optimize individual step performance