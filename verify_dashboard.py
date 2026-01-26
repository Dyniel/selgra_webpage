
import pytest
from playwright.sync_api import sync_playwright, Page, expect
import os
import time

BASE_URL = f"file://{os.getcwd()}/index.html"

def run_verification(page: Page):
    """Reusable verification steps for the new single-page layout."""
    page.goto(BASE_URL)

    # 1. Verify the header is visible
    header = page.locator("#main-header")
    expect(header).to_be_visible()

    # 2. Verify main sections are present and user panel is hidden
    expect(page.locator("section#about")).to_be_visible()
    expect(page.locator("section#user-panel")).to_be_hidden()

    # 3. Test password-protected panel
    panel_link = page.locator("nav a[href='#user-panel']")

    # Use a dialog handler to interact with the prompt
    # Test wrong password first
    page.once("dialog", lambda dialog: dialog.dismiss())
    panel_link.click()
    expect(page.locator("section#user-panel")).to_be_hidden() # It should still be hidden

    # Test correct password
    page.once("dialog", lambda dialog: dialog.accept("123"))
    panel_link.click()

    # Wait for the panel to become visible after entering the correct password
    expect(page.locator("section#user-panel")).to_be_visible()

    # Give it a moment for the scroll to finish
    time.sleep(1)

    # 4. Take a screenshot of the new layout with the user panel visible
    os.makedirs("verification_screenshots", exist_ok=True)
    page.screenshot(path="verification_screenshots/redesigned_page_with_panel.png", full_page=True)


def test_dashboard_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        run_verification(page)
        browser.close()

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        run_verification(page)
        print("Verification complete. Check 'verification_screenshots' for 'redesigned_page_with_panel.png'.")
        browser.close()
