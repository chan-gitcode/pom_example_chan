from playwright.async_api import Page
from page.base_page import BasePage


class DepartmentPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.textbox_name = self.page.get_by_role("textbox", name="Name", exact=True)
        self.button_save = self.page.get_by_role("button", name="Save", exact=True)
        self.textbox_search = self.page.get_by_role("searchbox", name="Search", exact=True)
        self.department_name_table = self.page.locator('//table[@id="xin_table"]')

    def go_to_department_page(self):
        self.navigate_url("https://hrm.anhtester.com/erp/departments-list")
        self.verify_element_visible(self.textbox_name)

    def create_department(self, department_name: str):
        self.set_text(self.textbox_name, department_name)
        self.click(self.button_save)

    def verify_create_success(self, expected_value: str):
        self.set_text(self.textbox_search, expected_value)
        cell_department_name = self.page.locator('//table[@id="xin_table"]//td[1]')
        self.verify_element_text(cell_department_name, expected_value, is_extract=True)