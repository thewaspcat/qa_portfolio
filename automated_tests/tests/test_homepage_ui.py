from playwright.sync_api import sync_playwright

def test_logo_visible():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.automationexercise.com/")
        logo = page.query_selector("div.logo.pull-left > a > img")
        assert logo.is_visible()
        browser.close()
