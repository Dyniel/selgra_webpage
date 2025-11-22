
import pytest
from playwright.sync_api import sync_playwright, Page, expect
import os

BASE_URL = f"file://{os.getcwd()}/index.html"

def run_verification(page: Page):
    """Reusable verification steps."""
    page.goto(BASE_URL)

    # 1. Login
    page.locator("#username").fill("member")
    page.locator("#password").fill("member")
    page.locator("button[type='submit']").click()

    # Wait for dashboard to be visible
    expect(page.locator("#dashboard-view")).to_be_visible()

    # 2. Verify Tab View is active and content is visible
    expect(page.locator("#tab-view-btn")).to_have_class("active")

    # Check that the first tab's content is visible
    # The default first tab is "Social Feed"
    expect(page.locator("#social-feed-container")).to_be_visible()

    # Check that another tab's content is hidden
    expect(page.locator("#calendar-container")).to_be_hidden()

    os.makedirs("verification_screenshots", exist_ok=True)
    page.screenshot(path="verification_screenshots/01_tab_view_initial.png")

    # 3. Switch to another tab
    page.locator("button[data-tab-target='calendar']").click()

    # Verify the new tab's content is visible
    expect(page.locator("#social-feed-container")).to_be_hidden()
    expect(page.locator("#calendar-container")).to_be_visible()
    page.screenshot(path="verification_screenshots/02_tab_view_switched.png")

    # 4. Switch to Module View
    page.locator("#module-view-btn").click()
    expect(page.locator("#module-view-btn")).to_have_class("active")

    # Verify all widgets are now visible
    for item in page.locator(".grid-stack-item").all():
        if item.get_attribute("id") != "admin-panel":
             expect(item).not_to_have_class("hidden")

    expect(page.locator("#admin-panel")).to_be_hidden()

    page.screenshot(path="verification_screenshots/03_module_view.png")

def test_dashboard_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        run_verification(page)
        browser.close()

if __name__ == "__main__":
    # This allows running the script directly for debugging
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        run_verification(page)
        print("Verification complete. Check the 'verification_screenshots' folder.")
        browser.close()
