from playwright.sync_api import sync_playwright
import time

def test_homepage_load_time():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        start = time.time()
        page.goto("https://www.automationexercise.com/")
        end = time.time()
        load_time = end - start
        assert load_time < 5, f"Page load took {load_time:.2f} seconds"
        browser.close()
