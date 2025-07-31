import csv
import random
import time
from pytest_bdd import scenarios, given, when, then

from conftest import base_url
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(channel='msedge',headless=False)
page = browser.new_page()

scenarios('features/user-registration.feature')

@given('user is on the registration page')  #if we are calling fixture function use
def login_page(base_url):
    """This function checks for the presence of a login form element and user registration form element,
    confirming that the login page is visible"""
    page.goto(f"{base_url}/actions/Account.action?signonForm=", wait_until="load")
    time.sleep(4)
    assert page.get_by_text('Please enter your username and password.').is_visible(), "Login page not loaded"
    if page.get_by_text("Register Now").is_visible():
        page.get_by_text("Register Now").click()
    else:
        time.sleep(5)
    assert page.get_by_text("User Info").is_visible(), "Registration page not loaded"

@given('user enters all required information')
def user_info():
    """This method reads userdata from csv file and fills it in form fields
       and gives the details of registered user's first name and last name"""
    with open('testdata\\registrationData.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) >= 1:
            print(rows[1])
        else:
            print("Error: CSV does not have a second row")
        second_row = rows[1]

    if len(second_row) >= 3:
        print(f"{second_row[3]}")
        print(f"{second_row[4]}")
    else:
        print("There is no firstname and last name in data")

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

    print("formdata has filled")

    page.select_option("//select[@name='account.languagePreference']", value='english')
    options = ["FISH", "DOGS", "REPTILES", "CATS", "BIRDS"]
    random_option = random.choice(options)
    page.select_option('select[name="account.favouriteCategoryId"]', value=random_option)

    print("categories have selected")

    page.locator("//input[@name='account.listOption']").click()
    page.locator("//input[@name='account.bannerOption']").click()

@when('user clicks the "Save Account Information" button')
def save_info():
    """This method clicks the Save Account Information button to
       save the user info which is filled"""
    if page.locator("//input[@name='newAccount']").is_visible():
        page.locator("//input[@name='newAccount']").click()
    else:
        time.sleep(4)

@then('user should be successfully registered')
def verify_page():
    assert page.get_by_text("Sign In").is_visible(), f"Invalid page"


