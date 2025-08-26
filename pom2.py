from playwright.sync_api import sync_playwright
from pom import LoginPage

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")

        login_page = LoginPage(page)

        login_page.enter_username("wrongUser")
        login_page.enter_password("wrongPass")
        login_page.click_login()

        error_message = login_page.get_error_message()
        assert "Your username is invalid!" in error_message

        browser.close()
