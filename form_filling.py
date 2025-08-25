import random
import time
from config import base_url, user_prompt
from faker import Faker
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(channel="msedge", headless=False)
page = browser.new_page()
faker = Faker()

def test_formfilling():
    page.goto(base_url, wait_until='load')
    assert page.is_visible('//img[@src="/images/Toolsqa.jpg"]'), "page not loaded"
    page.hover("//h5[text()='Forms']")
    page.click("//h5[text()='Forms']")
    assert page.get_by_text("Please select an item from left to start practice.").is_visible()
    page.click("//span[text()='Practice Form']")
    time.sleep(3)
    page.locator("//input[@placeholder='First Name']").fill(faker.first_name())
    time.sleep(2)
    page.locator("//input[@placeholder='Last Name']").fill(faker.last_name())
    page.locator("//input[@placeholder='name@example.com']").fill(faker.email())
    radio_buttons = ["//label[@for='gender-radio-1']","//label[@for='gender-radio-2']","//label[@for='gender-radio-3']"]
    gender = random.choices(radio_buttons)
    print(gender)
    page.locator(gender).click()
    # page.click("//label[text()='Female']")
    page.click("//div[@aria-hidden='true']")
    # page.click("//div[text()='Haryana']")


