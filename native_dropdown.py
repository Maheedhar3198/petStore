import time
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
iphone = playwright.devices["iPhone 12 Pro"]
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(**iphone)
page = context.new_page()

def test_native_dropdown():
    page.goto("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
    time.sleep(2)
    page.select_option("select", value="ALA")
    page.screenshot(path="Screenshots.png")
