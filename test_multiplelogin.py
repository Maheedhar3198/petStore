import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

scenarios('multipleLogin.feature')

@given('user has to login multipletimes')
def repeated_login():
    for i in range(3):
        print(f"\nLogin Attempt {i + 1}")

        page.goto('https://petstore.octoperf.com/actions/Account.action?signonForm=', wait_until="load")
        assert page.get_by_text('Please enter your username and password.').is_visible(), "Login page not loaded"

        page.fill("//input[@name='username']", "3198")
        page.fill("//input[@name='password']", "Atmecs1223")

        page.click("//input[@name='signon']")

        assert page.get_by_text("Welcome Maheedhar!").is_visible(), "Login failed"
        print("Login successful")

        page.click("text=Sign Out")


#context rekated variable namings
#16- no hardcoding of url's
#env based url
#username and pw