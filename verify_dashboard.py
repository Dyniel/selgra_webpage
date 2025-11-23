
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

    # 2. Verify that the main sections are present
    expect(page.locator("section#about")).to_be_visible()
    expect(page.locator("section#history")).to_be_visible()
    expect(page.locator("section#join")).to_be_visible()
    expect(page.locator("section#feed")).to_be_visible()
    expect(page.locator("section#calendar")).to_be_visible()

    # 3. Test smooth scrolling
    # Click on the 'Join Us' link in the navigation
    page.locator("nav a[href='#join']").click()

    # Wait a moment for the scroll to finish
    time.sleep(1)

    # 4. Take a screenshot of the new layout
    os.makedirs("verification_screenshots", exist_ok=True)
    page.screenshot(path="verification_screenshots/redesigned_page.png", full_page=True)


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
        print("Verification complete. Check the 'verification_screenshots' folder for 'redesigned_page.png'.")
        browser.close()
