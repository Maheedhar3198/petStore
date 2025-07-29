"""
Author      : Maheedhar Doddi
Date        : 29-07-2025
Module      : test_multiplelogin.py
Description : Automates login test using pytest-bdd and Playwright.
              Logs in 5 times using same credentials and verifies welcome page.
"""
import time
from conftest import base_url,credentials
from playwright.sync_api import sync_playwright

from pytest_bdd import scenarios, given, when, then

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

scenarios('features/multipleLogin.feature')


@given('user is on login page')
def login_page(base_url):
    """This function checks for the presence of a login form element,
    confirming that the login page is visible"""
    page.goto(f"{base_url}/actions/Account.action?signonForm=", wait_until="load")
    assert page.get_by_text('Please enter your username and password.').is_visible(), "Login page not loaded"


@when('user logged in 5 times by entering valid credentials and clicking login button')
def fill_credentials(base_url, credentials):
    """This function performs login operation multiple times(5)
    using the same credentials"""
    for attempts in range(5):
        page.goto(f"{base_url}/actions/Account.action?signonForm=")
        page.fill("//input[@name='username']", credentials['username'])
        page.fill("//input[@name='password']", credentials['password'])
        time.sleep(2)
        if page.locator("//input[@value='Login']").is_visible():
            page.click("//input[@value='Login']")
        else:
            time.sleep(5)


@then('user has to enter welcome page')
def verify_user():
    """This function checks for the presence of a welcome message element,
    confirming that the login was successful"""
    assert page.locator("//div[@id='WelcomeContent']").is_visible(), "Login failed: Welcome message not visible"
    page.click("text=Sign Out")
    time.sleep(2)
