# Test Case: Homepage Performance
## Test Case ID: TC_HOMEPAGE_PERF_001
## Test Type: Performance
## Priority: High
## Preconditions:
- User is logged out
- Homepage accessible

| Step | Action | Expected Result |
|------|--------|----------------|
| 1 | Open DevTools → Performance → Reload homepage | Page loads in under 5 seconds |
| 2 | Open DevTools → Console | No major JavaScript errors appear during page load |
