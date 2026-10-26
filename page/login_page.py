from playwright.sync_api import Page
from page.base_page import BasePage
from page.home_page import HomePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.textbox_username = self.page.get_by_role(
            "textbox", name="Your Username", exact=True
        )
        self.textbox_password = self.page.get_by_role(
            "textbox", name="Enter Password", exact=True
        )
        self.button_login = self.page.get_by_role("button", name="Login", exact=False)

    def login(self, url: str, username: str, password: str):
        self.navigate_url(url)
        self.set_text(self.textbox_username, username)
        self.set_text(self.textbox_password, password)
        self.click(self.button_login)

    def verify_login_success(self, expect_value: str):
        self.verify_element_visible(self.left_menu)
        self.verify_element_visible(self.header_component)
        self.verify_element_text(
            self.label_profile_name, expect_value, is_extract=False
        )
