import time
from config import base_url, user_prompt
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(channel="msedge", headless=False)
page = browser.new_page()

def test_clicking_alert():
    page.goto(base_url, wait_until='load')
    assert page.is_visible('//img[@src="/images/Toolsqa.jpg"]'), "page not loaded"
    page.hover("//h5[text()='Widgets']")
    page.click("//h5[text()='Widgets']")
    assert page.get_by_text("Please select an item from left to start practice.").is_visible()
    page.click("//span[text()='Progress Bar']")
    assert page.locator("//div[text()='Progress Bar']").is_visible()
    page.click("//button[text()='Start']")
    while True:
        progress_text = page.locator("//div[@role='progressbar']").inner_text()
        value = int(progress_text.replace("%", "").strip())
        print(f"Current progress: {value}%")
        if value >= 70:
            # print("Automation stopped at 70%")
            page.click("//button[text()='Stop']")
            break
        time.sleep(2)



