from playwright.sync_api import sync_playwright

def test_navigation_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.automationexercise.com/")
        links = page.query_selector_all("ul.nav.navbar-nav > li > a")
        assert len(links) >= 7  # Home, Products, Cart, Signup/Login, etc.
        browser.close()
