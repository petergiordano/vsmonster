# Production Readiness Command

## Purpose
Comprehensively evaluate and ensure applications are ready for production deployment with enterprise-grade reliability, security, and performance standards.

## Usage
```
@production-readiness [check-type] [options]
```

## Assessment Categories

### 1. Complete Production Assessment
```
@production-readiness full [--environment staging] [--output report.json]
```
Comprehensive production readiness evaluation across all categories.

### 2. Infrastructure Readiness
```
@production-readiness infrastructure [--cloud-provider aws]
```
Infrastructure and deployment configuration assessment:
- Container configuration
- Cloud service setup
- Networking configuration
- Resource allocation
- Scaling policies

### 3. Security Readiness
```
@production-readiness security [--compliance-level enterprise]
```
Security posture evaluation:
- Authentication mechanisms
- Authorization patterns
- Data encryption
- API security
- Compliance requirements

### 4. Performance Readiness
```
@production-readiness performance [--load-profile high]
```
Performance and scalability assessment:
- Load testing results
- Performance benchmarks
- Resource optimization
- Caching strategies
- CDN configuration

### 5. Monitoring & Observability
```
@production-readiness observability [--include-alerting]
```
Monitoring and observability setup:
- Logging configuration
- Metrics collection
- Alerting rules
- Health checks
- Error tracking

### 6. Data & Backup Readiness
```
@production-readiness data [--backup-strategy validated]
```
Data management and backup systems:
- Database configuration
- Backup procedures
- Data migration readiness
- Disaster recovery plans
- Data compliance

## Production Readiness Report

### Executive Summary
```
Production Readiness Assessment
═══════════════════════════════════════════════════════════════════════

🎯 OVERALL READINESS: 87% - READY WITH MINOR IMPROVEMENTS

📊 Category Scores:
├─ Infrastructure: 92% (🟢 Excellent)
├─ Security: 89% (🟢 Very Good)  
├─ Performance: 85% (🟢 Good)
├─ Monitoring: 83% (🟡 Acceptable)
├─ Data & Backup: 91% (🟢 Excellent)
└─ Documentation: 79% (🟡 Acceptable)

✅ Ready for Production:
├─ Core functionality tested and validated
├─ Security measures properly implemented
├─ Infrastructure scaled and configured
├─ Monitoring and alerting operational
└─ Backup and recovery procedures tested

⚠️ Improvements Recommended (Not Blocking):
├─ Enhanced error handling in payment flow
├─ Additional performance monitoring for API
├─ Expanded documentation for ops team
└─ Secondary backup location setup

🚀 Deployment Recommendation: PROCEED
├─ Risk Level: LOW
├─ Estimated Deployment Time: 2 hours
├─ Rollback Time: <30 minutes
└─ Recommended Deploy Window: Maintenance hours
```

### Detailed Infrastructure Assessment
```
Infrastructure Readiness: 92/100
═══════════════════════════════════════════════════════════════════════

🏗️ Container & Orchestration:
├─ Docker Configuration: ✅ Optimized multi-stage build
├─ Kubernetes Manifests: ✅ Production-ready with resource limits
├─ Helm Charts: ✅ Templated and validated
├─ Image Security: ✅ Scanned, minimal base images
└─ Registry: ✅ Private registry with vulnerability scanning

☁️ Cloud Infrastructure:
├─ Load Balancer: ✅ Application Load Balancer configured
├─ Auto Scaling: ✅ HPA and VPA policies defined
├─ Networking: ✅ VPC with proper subnet configuration
├─ Security Groups: ✅ Principle of least privilege applied
└─ SSL/TLS: ✅ Valid certificates with auto-renewal

💾 Database & Storage:
├─ RDS Configuration: ✅ Multi-AZ with read replicas
├─ Connection Pooling: ✅ PgBouncer configured
├─ Storage: ✅ Encrypted EBS volumes
├─ Backup: ✅ Automated daily backups
└─ Migration: ✅ Zero-downtime migration strategy

📊 Resource Planning:
├─ CPU Allocation: ✅ Appropriate limits and requests
├─ Memory Allocation: ✅ Based on profiling data
├─ Storage Planning: ✅ Growth projected for 12 months
├─ Network Bandwidth: ✅ Sufficient for expected load
└─ Cost Optimization: ✅ Right-sized instances

⚠️ Areas for Improvement:
├─ Add chaos engineering tests
├─ Implement blue-green deployment
├─ Set up disaster recovery region
└─ Enhance monitoring for Kubernetes events
```

### Security Readiness Deep Dive
```
Security Readiness: 89/100
═══════════════════════════════════════════════════════════════════════

🔐 Authentication & Authorization:
├─ User Authentication: ✅ OAuth 2.0 + JWT tokens
├─ API Authentication: ✅ Bearer tokens with expiration
├─ Service-to-Service: ✅ mTLS between services
├─ Role-Based Access: ✅ Granular permissions implemented
└─ Multi-Factor Auth: ✅ Required for admin accounts

🛡️ Data Protection:
├─ Encryption at Rest: ✅ AES-256 for all data stores
├─ Encryption in Transit: ✅ TLS 1.3 for all connections
├─ Key Management: ✅ AWS KMS with rotation
├─ PII Handling: ✅ Encrypted and access-controlled
└─ Data Anonymization: ✅ For analytics and testing

🌐 Network Security:
├─ Firewall Rules: ✅ WAF configured with OWASP rules
├─ DDoS Protection: ✅ CloudFlare protection enabled
├─ Network Segmentation: ✅ Private subnets for data
├─ VPN Access: ✅ Required for admin operations
└─ Security Headers: ✅ HSTS, CSP, and others configured

🔍 Security Monitoring:
├─ Intrusion Detection: ✅ AWS GuardDuty enabled
├─ Vulnerability Scanning: ✅ Automated container scanning
├─ Security Logging: ✅ All security events logged
├─ Incident Response: ✅ Playbooks documented
└─ Compliance: ✅ SOC 2 Type II preparation

⚠️ Security Improvements:
├─ Implement secret rotation automation
├─ Add runtime security monitoring
├─ Enhance audit logging coverage
└─ Set up security metrics dashboard
```

### Performance Readiness Analysis
```
Performance Readiness: 85/100
═══════════════════════════════════════════════════════════════════════

⚡ Load Testing Results:
├─ Concurrent Users: ✅ Tested up to 10,000 users
├─ Response Times: ✅ 95th percentile < 500ms
├─ Throughput: ✅ 5,000 requests/second sustained
├─ Error Rate: ✅ <0.1% under normal load
└─ Resource Usage: ✅ CPU <70%, Memory <80%

🚀 Performance Optimizations:
├─ Database Queries: ✅ Optimized with proper indexing
├─ API Responses: ✅ Gzip compression enabled
├─ Static Assets: ✅ CDN with global edge locations
├─ Caching Strategy: ✅ Redis for session and data
└─ Code Optimization: ✅ Bundle size optimized

📊 Scalability Measures:
├─ Horizontal Scaling: ✅ Stateless application design
├─ Database Scaling: ✅ Read replicas configured
├─ Cache Scaling: ✅ Redis cluster setup
├─ File Storage: ✅ S3 with CloudFront
└─ Search: ✅ Elasticsearch cluster

📱 Client Performance:
├─ First Contentful Paint: ✅ <1.5s on 3G
├─ Time to Interactive: ✅ <3s average
├─ Bundle Size: ✅ <500KB initial load
├─ Image Optimization: ✅ WebP with fallbacks
└─ Mobile Performance: ✅ Lighthouse score >85

⚠️ Performance Opportunities:
├─ Implement database query caching
├─ Add performance regression testing
├─ Optimize cold start times
└─ Implement adaptive loading strategies
```

### Monitoring & Observability Setup
```
Observability Readiness: 83/100
═══════════════════════════════════════════════════════════════════════

📊 Metrics & Monitoring:
├─ Application Metrics: ✅ Prometheus + Grafana
├─ Infrastructure Metrics: ✅ CloudWatch integration
├─ Custom Business Metrics: ✅ Revenue, conversions
├─ SLA/SLO Tracking: ✅ 99.9% uptime target
└─ Performance Metrics: ✅ Response times, throughput

📝 Logging Infrastructure:
├─ Centralized Logging: ✅ ELK stack deployed
├─ Log Aggregation: ✅ Structured JSON logging
├─ Log Retention: ✅ 90 days with archival
├─ Log Security: ✅ Encrypted and access-controlled
└─ Error Tracking: ✅ Sentry integration

🚨 Alerting & Notifications:
├─ Critical Alerts: ✅ PagerDuty integration
├─ Warning Alerts: ✅ Slack notifications
├─ Alert Escalation: ✅ Defined escalation paths
├─ Alert Fatigue: ✅ Tuned thresholds
└─ Runbook Integration: ✅ Linked to procedures

🔍 Observability Tools:
├─ Distributed Tracing: ✅ Jaeger implementation
├─ APM: ✅ New Relic for application monitoring
├─ Synthetic Monitoring: ✅ Uptime checks configured
├─ User Analytics: ✅ Google Analytics + custom events
└─ Error Analysis: ✅ Error rate and pattern tracking

⚠️ Monitoring Gaps:
├─ Add business process monitoring
├─ Implement user experience monitoring
├─ Enhance database performance tracking
└─ Add capacity planning dashboards
```

## Production Checklist Generator

### Deployment Checklist
```
@production-readiness checklist --type deployment
```

```
Production Deployment Checklist
═══════════════════════════════════════════════════════════════════════

📋 Pre-Deployment (T-24 hours):
□ Code freeze implemented
□ Final regression testing completed
□ Load testing passed
□ Security scan cleared
□ Database migration scripts tested
□ Rollback procedures verified
□ Monitoring alerts configured
□ Team availability confirmed
□ Communication plan activated
□ Maintenance window scheduled

📋 Deployment Day (T-0):
□ Backup current production data
□ Verify all systems operational
□ Execute deployment pipeline
□ Run database migrations
□ Verify application startup
□ Execute smoke tests
□ Monitor system metrics
□ Validate core functionality
□ Check error rates and logs
□ Confirm user access

📋 Post-Deployment (T+2 hours):
□ Monitor system stability
□ Review error logs and metrics
□ Validate business KPIs
□ Confirm integrations working
□ Check performance metrics
□ Verify monitoring and alerts
□ Document any issues
□ Notify stakeholders of success
□ Schedule post-mortem if needed
□ Update deployment documentation
```

### Go-Live Readiness Assessment
```
@production-readiness go-live --comprehensive
```

```
Go-Live Readiness Assessment
═══════════════════════════════════════════════════════════════════════

🎯 READY FOR GO-LIVE: YES (Confidence: 94%)

✅ Critical Systems Ready:
├─ Application: All core features tested and operational
├─ Database: Production-ready with backup/recovery
├─ Infrastructure: Scaled and monitored
├─ Security: Hardened and compliant
├─ Integrations: All third-party services tested
└─ Team: Trained and ready for support

📊 Business Readiness:
├─ User Acceptance Testing: ✅ Passed
├─ Performance Under Load: ✅ Validated
├─ Data Migration: ✅ Completed successfully
├─ Training Materials: ✅ Created and distributed
├─ Support Procedures: ✅ Documented and tested
└─ Marketing Coordination: ✅ Launch plan ready

🛡️ Risk Assessment:
├─ Technical Risk: LOW (mitigation plans in place)
├─ Business Risk: LOW (gradual rollout planned)
├─ Security Risk: LOW (security measures validated)
├─ Operational Risk: MEDIUM (new monitoring setup)
└─ Financial Risk: LOW (cost projections validated)

🚀 Launch Strategy:
├─ Phased Rollout: 5% → 25% → 50% → 100%
├─ Feature Flags: Ready for instant rollback
├─ Monitoring: Enhanced monitoring during rollout
├─ Support: 24/7 team coverage for first week
└─ Communication: Stakeholder updates every 4 hours

📞 Escalation Contacts:
├─ Technical Lead: [Contact info]
├─ Product Manager: [Contact info]
├─ Infrastructure: [Contact info]
├─ Security: [Contact info]
└─ Executive Sponsor: [Contact info]
```

## Automated Validation Scripts

### Environment Validation
Create `scripts/validate-production-ready.py`:

```python
#!/usr/bin/env python3
"""
Production Readiness Validation Script
Automated validation of production deployment requirements
"""

import sys
import json
import subprocess
import requests
from typing import Dict, List, Tuple

class ProductionValidator:
    def __init__(self, config_path: str):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self.results = []
    
    def validate_infrastructure(self) -> Tuple[bool, str]:
        """Validate infrastructure components"""
        checks = [
            self._check_load_balancer(),
            self._check_database_connectivity(),
            self._check_ssl_certificates(),
            self._check_auto_scaling(),
            self._check_backup_systems()
        ]
        passed = all(check[0] for check in checks)
        details = "\n".join(check[1] for check in checks)
        return passed, details
    
    def validate_security(self) -> Tuple[bool, str]:
        """Validate security configuration"""
        checks = [
            self._check_security_headers(),
            self._check_authentication(),
            self._check_encryption(),
            self._check_vulnerability_scan(),
            self._check_access_controls()
        ]
        passed = all(check[0] for check in checks)
        details = "\n".join(check[1] for check in checks)
        return passed, details
    
    def validate_performance(self) -> Tuple[bool, str]:
        """Validate performance requirements"""
        checks = [
            self._check_response_times(),
            self._check_load_capacity(),
            self._check_resource_usage(),
            self._check_caching(),
            self._check_cdn_setup()
        ]
        passed = all(check[0] for check in checks)
        details = "\n".join(check[1] for check in checks)
        return passed, details
    
    def validate_monitoring(self) -> Tuple[bool, str]:
        """Validate monitoring and alerting"""
        checks = [
            self._check_logging_setup(),
            self._check_metrics_collection(),
            self._check_alerting_rules(),
            self._check_health_endpoints(),
            self._check_error_tracking()
        ]
        passed = all(check[0] for check in checks)
        details = "\n".join(check[1] for check in checks)
        return passed, details
    
    def generate_report(self) -> Dict:
        """Generate comprehensive readiness report"""
        infrastructure_ok, infrastructure_details = self.validate_infrastructure()
        security_ok, security_details = self.validate_security()
        performance_ok, performance_details = self.validate_performance()
        monitoring_ok, monitoring_details = self.validate_monitoring()
        
        overall_ready = all([
            infrastructure_ok,
            security_ok,
            performance_ok,
            monitoring_ok
        ])
        
        return {
            "overall_ready": overall_ready,
            "readiness_score": self._calculate_score(),
            "categories": {
                "infrastructure": {
                    "passed": infrastructure_ok,
                    "details": infrastructure_details
                },
                "security": {
                    "passed": security_ok,
                    "details": security_details
                },
                "performance": {
                    "passed": performance_ok,
                    "details": performance_details
                },
                "monitoring": {
                    "passed": monitoring_ok,
                    "details": monitoring_details
                }
            },
            "recommendations": self._generate_recommendations()
        }

if __name__ == "__main__":
    validator = ProductionValidator(".claude/production-config.json")
    report = validator.generate_report()
    
    print(json.dumps(report, indent=2))
    
    if not report["overall_ready"]:
        sys.exit(1)
```

## Configuration Files

### Production Configuration
Create `.claude/production-config.json`:

```json
{
  "production_standards": {
    "infrastructure": {
      "high_availability": true,
      "auto_scaling": true,
      "load_balancer": "required",
      "backup_strategy": "automated",
      "disaster_recovery": "cross_region"
    },
    "security": {
      "ssl_required": true,
      "authentication": "required",
      "authorization": "rbac",
      "encryption_at_rest": true,
      "vulnerability_scanning": "continuous"
    },
    "performance": {
      "response_time_p95": 500,
      "availability_target": 99.9,
      "load_capacity": "10000_concurrent_users",
      "cache_hit_ratio": 0.8
    },
    "monitoring": {
      "logging_level": "info",
      "metrics_retention": "90_days",
      "alerting": "24x7",
      "health_checks": "required"
    }
  },
  "deployment_requirements": {
    "code_quality": {
      "test_coverage_min": 80,
      "security_scan": "passed",
      "performance_tests": "passed",
      "documentation": "complete"
    },
    "approval_process": {
      "technical_review": "required",
      "security_review": "required",
      "business_approval": "required",
      "change_management": "documented"
    }
  }
}
```

## Integration with Deployment Pipeline

### GitHub Actions Integration
```yaml
name: Production Readiness Check

on:
  pull_request:
    branches: [main]
  workflow_dispatch:

jobs:
  production-readiness:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Run Production Readiness Assessment
        run: |
          @production-readiness full \
            --environment production \
            --output production-readiness-report.json \
            --fail-on-critical
      
      - name: Upload Assessment Report
        uses: actions/upload-artifact@v2
        with:
          name: production-readiness-report
          path: production-readiness-report.json
      
      - name: Comment PR with Results
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = JSON.parse(fs.readFileSync('production-readiness-report.json', 'utf8'));
            const comment = `## Production Readiness Assessment
            
            **Overall Score:** ${report.readiness_score}/100
            **Ready for Production:** ${report.overall_ready ? '✅ YES' : '❌ NO'}
            
            ### Category Scores:
            - Infrastructure: ${report.categories.infrastructure.score}/100
            - Security: ${report.categories.security.score}/100
            - Performance: ${report.categories.performance.score}/100
            - Monitoring: ${report.categories.monitoring.score}/100
            
            [View Full Report](${context.payload.pull_request.html_url}/checks)`;
            
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

## Best Practices

### Production Readiness Culture
1. **Shift Left**: Consider production requirements early in development
2. **Automate Validation**: Use automated tools to validate readiness
3. **Regular Assessment**: Continuously assess and improve production readiness
4. **Documentation**: Maintain comprehensive operational documentation
5. **Team Training**: Ensure team understands production requirements

### Continuous Improvement
1. **Post-Incident Reviews**: Learn from production issues
2. **Metrics-Driven**: Use data to drive production improvements
3. **Regular Audits**: Periodically audit production systems
4. **Feedback Loops**: Incorporate operational feedback into development
5. **Industry Standards**: Stay current with industry best practices