import time
from config import base_url, user_prompt
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(channel="msedge", headless=False)
page = browser.new_page()

def test_dragdrop():
    page.goto(base_url, wait_until='load')
    assert page.is_visible('//img[@src="/images/Toolsqa.jpg"]'), "page not loaded"
    page.hover("//h5[text()='Interactions']")
    page.click("//h5[text()='Interactions']")
    assert page.get_by_text("Please select an item from left to start practice.").is_visible()
    page.click("//span[text()='Droppable']")
    page.drag_and_drop("//div[text()='Drag me']", "//div[@id='droppable']")
