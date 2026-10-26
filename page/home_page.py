from playwright.sync_api import Page
from page.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header_component = self.page.locator('//header')
        self.left_menu = self.page.locator('//nav')
        self.label_profile_name = self.page.locator('//a[@href="https://hrm.anhtester.com/erp/my-profile"]//p')

    def choose_left_menu(self, main_menu: str, sub_menu: str):
        locator_main_menu = self.page.get_by_role("link", name=f"{main_menu}", exact=True)
        self.click(locator_main_menu)
        if sub_menu is not None:
            locator_sub_menu = self.page.get_by_role("link", name=f"{sub_menu}", exact=True)
            self.click(locator_sub_menu)