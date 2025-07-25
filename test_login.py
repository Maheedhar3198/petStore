import pytest
from pytest_bdd import scenarios, given, when, then

scenarios('userSignin.feature')
@given('user is on the login page')
def test_loginpage():
    print('user is in loginpage')



@when('user clicks on the login button')
def test_loginbutton():
    print('user clicks login button')



@then('user should be redirected to the home page with welcome message')
def test_homepage():
    print('user is in homepage')
