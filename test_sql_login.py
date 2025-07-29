"""
Author      : Maheedhar Sai
Date        : 29-07-2025
Module      : test_sql_login.py
Description : Automates login test using pytest-bdd and Playwright.
              Retreiving user details data from sql server.
"""
import pymysql
import time
from conftest import base_url
from playwright.sync_api import sync_playwright
from pytest_bdd import scenarios, given, when, then

database = pymysql.connect(host='localhost', user='root', password='Atmecs!1234', database='userdata')
cursor = database.cursor()
cursor.execute('SELECT Username,Password FROM Users')
users = cursor.fetchall()

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
def fill_credentials(base_url):
    """This function performs login operation multiple times(5)
    using the same credentials"""
    for Username, Password in users:
        for attempts in range(5):
            page.goto(f"{base_url}/actions/Account.action?signonForm=")
            time.sleep(5)
            page.fill("//input[@name='username']", f"{Username}")
            page.fill("//input[@name='password']", f"{Password}")
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
