import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

scenarios('userSignin.feature')
@given('user is on the login page')
def test_loginpage():
    page.goto('https://petstore.octoperf.com/actions/Account.action?signonForm=', wait_until="load")
    assert page.get_by_text('Please enter your username and password.').is_visible(),f"Invalid page"
    print('user is in loginpage')

@given('user enters a valid username and password')
def test_entercredentials():
    page.fill("//input[@name='username']","3198")
    page.fill("//input[@name='password']", "Atmecs1223")
    print('user entered credentials')

@when('user clicks on the login button')
def test_loginbutton():
    page.click("//input[@name='signon']")
    print('user clicks login button')

@then('user should be redirected to the home page with welcome message')
def test_homepage():
    assert page.get_by_text("Welcome Maheedhar!").is_visible(),f"Invalid username or password"
    #print('user is in homepage')
    pass
