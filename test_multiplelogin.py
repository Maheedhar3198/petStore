import time

import pytest
import os
import env
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright

from conftest import base_url

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

# base_url = env.BASE_URL
# username = env.USERNAME
# password = env.PASSWORD
scenarios('multipleLogin.feature')

@given('user is on login page')
def test_login_page(base_url):
    page.goto(f"{base_url}/actions/Account.action?signonForm=", wait_until="load")
    assert page.get_by_text('Please enter your username and password.').is_visible(), "Login page not loaded"
    # return page

@when('user logged in 5 times by entering valid credentials and clicking login button')
def test_fillcredentials(credentials):
    page.fill("//input[@name='username']",credentials['username'])
    page.fill("//input[@name='password']",credentials['password'])
    # return test_login_page

@then('user has to enter welcome page')
def test_loginbutton(base_url,credentials):
    for attempts in range(5):
        page.goto(f"{base_url}/actions/Account.action?signonForm=")
        page.fill("//input[@name='username']", credentials['username'])
        page.fill("//input[@name='password']", credentials['password'])
        # print(f"login attempt {attempts + 1}")
        if page.locator("//input[@value='Login']").is_visible():
            page.click("//input[@value='Login']")
        else:
            time.sleep(5)

        assert page.locator("//div[@id='WelcomeContent']").is_visible(), "Login failed"
        # print("Login successful")
        page.click("text=Sign Out")
        time.sleep(2)



