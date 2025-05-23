# Cloud Cost Optimization Report

## Initial Setup (Before)
- EC2 instance: t3.medium
- RDS instance: db.t3.medium
- Running 24/7, no scaling or stop/start

## Optimization Plan
- Switch EC2 to spot instance (t3a.small)
- Downsize RDS to db.t3.small or Aurora Serverless
- Add scheduler to stop EC2 off-hours

## Estimated Monthly Savings

| Resource | Before | After | Savings |
|----------|--------|-------|---------|
| EC2      | $30/mo | $8/mo | $22     |
| RDS      | $50/mo | $20/mo| $30     |
| **Total**|        |       | **$52** |
