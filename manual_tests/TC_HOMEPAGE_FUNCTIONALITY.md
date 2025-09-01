# Test Case: Homepage Functional Elements
## Test Case ID: TC_HOMEPAGE_FUNC_001
## Test Type: Manual
## Priority: High
## Preconditions:
- User is logged out
- Homepage accessible: https://www.automationexercise.com

| Step | Action | Selector / Locator | Expected Result |
|------|--------|-----------------|----------------|
| 1 | Open homepage | URL | Homepage loads fully |
| 2 | Verify navigation links | ul.nav.navbar-nav > li > a | Links visible |
| 3 | Verify Features Items | div.features_items | Section visible with product cards |
| 4 | Verify Recommended Items | div.recommended_items | Section visible with product cards |
