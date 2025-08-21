import time
from config import base_url, user_prompt
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(channel="msedge", headless=False)
page = browser.new_page()

def test_formfilling():
    page.goto(base_url, wait_until='load')
    assert page.is_visible('//img[@src="/images/Toolsqa.jpg"]'), "page not loaded"
    page.hover("//h5[text()='Forms']")
    page.click("//h5[text()='Forms']")
    assert page.get_by_text("Please select an item from left to start practice.").is_visible()
    page.click("//span[text()='Practice Form']")
    time.sleep(3)
    page.click("//label[text()='Female']")
    page.click("//div[@aria-hidden='true']")
    page.click("//div[text()='Haryana']")

