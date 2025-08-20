import time
from config import base_url, user_prompt
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(channel="msedge", headless=False)
page = browser.new_page()

def test_clicking_alert():
    page.goto(base_url, wait_until='load')
    assert page.is_visible('//img[@src="/images/Toolsqa.jpg"]'), "page not loaded"
    page.hover('//div[@class="card-body"]//h5[text()="Alerts, Frame & Windows"]')
    page.click('//div[@class="card-body"]//h5[text()="Alerts, Frame & Windows"]')
    assert page.get_by_text("Please select an item from left to start practice.").is_visible()
    page.click('//span[text()="Alerts"]')
    assert page.is_visible("//h1[text()='Alerts']"), "Wrong option selected"

    page.once("dialog", lambda dialog: time.sleep(2) or  dialog.accept())
    page.click("//div[@class='col']//button[@id='alertButton']")
    page.wait_for_timeout(2000)

    page.once("dialog", lambda dialog: time.sleep(2) or dialog.accept())
    page.click("//button[@id='timerAlertButton']")
    page.wait_for_timeout(5000)

def test_handle_dialog():
    page.click("//button[@id='promtButton']")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Enter")

    # page.wait_for_timeout(5000)
    #
    # page.locator("//span[@class='text-success']").wait_for(state='visible')
    # assert page.is_visible("//span[@class='text-success']"), "Error"
