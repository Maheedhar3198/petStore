import csv
import time
from pytest_bdd import scenarios, given, when
from conftest import base_url
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(channel='msedge',headless=False)
page = browser.new_page()

scenarios('features/multipleLogin.feature')

@given('user is on login page')  #if we are calling fixture function use
def login_page(base_url):
    """This function checks for the presence of a login form element and user registration form element,
    confirming that the login page is visible"""
    print("code is coming here")
    page.goto(f"{base_url}/actions/Account.action?signonForm=", wait_until="load")
    print("code is coming here")
    time.sleep(4)
    assert page.get_by_text('Please enter your username and password.').is_visible(), "Login page not loaded"
    if page.get_by_text("//*[text()='Register Now!']").is_visible():
        page.get_by_text("//*[text()='Register Now!']").click()
    else:
        time.sleep(5)
    assert page.get_by_text("//h3[text()='User Information']").is_visible(), "Registration page not loaded"

@when('user logged in 5 times by entering valid credentials and clicking login button')
def user_info():
    with open('D:\\petStore\\testdata\\registrationData.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) >= 1:
            print(rows[1])
        else:
            print("Error: CSV does not have a second row")
        second_row = rows[1]

    registration_form_xpaths = ["//input[@name='username']", "//input[@name='password']",
                                "//input[@name='repeatedPassword']","//input[@name='account.firstName']",
                                "//input[@name='account.lastName']","//input[@name='account.email']",
                                "//input[@name='account.phone']", "//input[@name='account.address1']",
                                "//input[@name='account.address2']", "//input[@name='account.city']",
                                "//input[@name='account.state']","//input[@name='account.zip']",
                                "//input[@name='account.country']"
              ]
    if len(rows[1]) == len(registration_form_xpaths):
        for xpath,value in zip(registration_form_xpaths,second_row):
            page.fill(xpath,value)

    if page.locator("//input[@name='newAccount']").is_visible():
        page.locator("//input[@name='newAccount']").click()
    else:
        time.sleep(4)





