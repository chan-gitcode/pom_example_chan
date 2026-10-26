from playwright.async_api import Page, expect
import re
from page.base_page import BasePage
from page.home_page import HomePage

class PoliciesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page_name = "Policies"
        self.home_page = HomePage(page)
        self.textbox_title = self.page.get_by_role("textbox",name="Title")
        self.textbox_description = self.page.get_by_role("textbox", name="Description")
        self.input_file_attachment = self.page.locator('/form[@name="add_policy"]//input[@type="file"]')
        self.button_save = self.page.get_by_role("button",name="Save")
        self.textbox_search = self.page.get_by_role("textbox", name="Search")

    def go_to_policies_page(self):
        policies_header = self.page.locator(
            f'//div[@class="page-header"]//li[normalize-space()="{self.page_name}"]')
        tab_policies = self.page.locator(
            f'//li[contains(.,"{self.page_name}")][contains(@class,"nav-item")]')
        self.home_page.choose_left_menu("Core HR", self.page_name)
        self.verify_element_visible(policies_header)
        expect(tab_policies).to_have_class(re.compile(r"\bactive\b"))

    def create_policies(self, policy_name: str, policy_description: str, file_path: str):
        self.set_text(self.textbox_title, policy_name)
        self.set_text(self.textbox_description, policy_description)
        self.upload_file(self.input_file_attachment, file_path)
        self.click(self.button_save)

    def verify_create_success(self, expected_text: str):
        self.set_text(self.textbox_search, expected_text)
        cell_policy_name = self.page.locator('//table[@id="xin_table"]//tr[1]/td[1]//h6')
        self.verify_element_text(cell_policy_name, expected_text)

