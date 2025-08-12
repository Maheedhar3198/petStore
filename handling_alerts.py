import time

from config import base_url, user_prompt
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(channel="msedge",headless=False)
page = browser.new_page()

def test_clicking_alert():
    page.goto(base_url , wait_until='load')
    assert page.is_visible('//img[@src="/images/Toolsqa.jpg"]'), "page not loaded"
    page.hover('//div[@class="card-body"]//h5[text()="Alerts, Frame & Windows"]')
    page.click('//div[@class="card-body"]//h5[text()="Alerts, Frame & Windows"]')
    assert page.get_by_text("Please select an item from left to start practice.").is_visible()
    page.click('//span[text()="Alerts"]')
    assert page.is_visible("//h1[text()='Alerts']"), "Wrong option selected"

    page.on("dialog", lambda dialog: time.sleep(2) or dialog.accept())
    page.click("//div[@class='col']//button[@id='alertButton']")
    page.wait_for_timeout(5000)
    page.click("//button[@id='timerAlertButton']")
    page.wait_for_timeout(5000)

    page.on("dialog", lambda dialog: time.sleep(2) and dialog.accept("maheedhar"))
    page.click("//button[@id='promtButton']")
    page.wait_for_timeout(4000)
    if page.locator("//span[contains(text(), 'You entered')]").count() > 0:
        print("Element is present")
    else:
        print("Element is absent")
    page.wait_for_selector("//span[contains(text(), 'You entered')]", timeout=20000)
    assert page.is_visible("//span[contains(text(), 'You entered')]"), "Error"



