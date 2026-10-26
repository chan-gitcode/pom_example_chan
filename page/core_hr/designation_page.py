from playwright.async_api import Page, expect
import re
from page.base_page import BasePage
from page.home_page import HomePage

class DesignationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page_name = "Designation"
        self.home_page = HomePage(page)
        self.dropdown_department = self.page.get_by_role("combobox", name="Department", exact=True)
        self.textbox_designation_name = self.page.get_by_role("textbox", name="Designation Name", exact=True)
        self.textbox_description = self.page.get_by_role("textbox", name="Description", exact=True)
        self.button_save = self.page.get_by_role("button", name="Save", exact=True)
        self.textbox_search = self.page.get_by_role("searchbox",name="Search", exact=True)

    def go_to_designation_page(self):
        designation_header = self.page.locator(
            '//div[@class="page-header"]//li[normalize-space()="{self.page_name}"]')
        tab_designation = self.page.locator(
            f'//li[contains(.,"{self.page_name}")][contains(@class,"nav-item")]')

        
        # self.home_page.choose_left_menu("Core HR", self.page_name)
        locator_main_menu = self.page.get_by_role("link", name="Core HR", exact=True)
        self.click(locator_main_menu)
        locator_sub_menu = self.page.get_by_role("link", name="Designation", exact=True)
        self.click(locator_sub_menu)


        self.verify_element_visible(designation_header)
        # expect(tab_designation).to_contain_class("active")
        expect(tab_designation).to_have_class(re.compile(r"\bactive\b"))

    def create_designation(self, department_name: str, designation_name: str):
        self.select_dropdown(self.dropdown_department, department_name, by_label=True)
        self.set_text(self.textbox_designation_name, department_name)
        self.click(self.button_save)

    def verify_create_success(self, designation_name: str):
        self.set_text(self.textbox_search, designation_name)
        self.verify_element_text(self.page.locator('//table[@id="xin_table"]//tr[1]//td[1]'), is_extract=True)
        self.verify_element_text(self.page.locator('//table[@id="xin_table"]//tr[1]//td[2]'), is_extract=True)