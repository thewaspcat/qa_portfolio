# Automated Test Suite

## Tests
- `test_homepage_functionality.py` - checks navigation links and product sections
- `test_homepage_ui.py` - checks logo and layout visibility
- `test_homepage_performance.py` - measures homepage load time and checks console errors

## Run Tests
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest automated_tests/tests/

