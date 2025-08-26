from asyncio import timeout

from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "//input[@id='username']"
        self.password_input = "//input[@id='password']"
        self.login_button = "//button[@type='submit']"
        self.flash_message = "//div[@id='flash']"

    def enter_username(self, username):
        self.page.fill(self.username_input, username)

    def enter_password(self, password):
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.text_content(self.flash_message).strip()
