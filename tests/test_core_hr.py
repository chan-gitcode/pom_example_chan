import pytest
from playwright.async_api import Page
from page import LoginPage, DepartmentPage, DesignationPage, PoliciesPage
from utils.path_helper import PathFile
from utils.text_data import TextData


config_data = PathFile.read_json_data('input_data/config.json')
URL = config_data['URL']
USERNAME = config_data['USERNAME']
PASSWORD = config_data['PASSWORD']
NAME_DEPARTMENT = TextData.create_text_data("New Department")

@pytest.mark.dependency(name="create_department")
def test_create_department(page: Page):
    """Kiểm thử quy trình tạo Designation mới gắn liền với phòng ban: đăng nhập, điều hướng tới
    trang Designation, tạo Designation mới và xác minh việc tạo thành công trong danh sách.

    Args:
        page (Page): Đối tượng Page của Playwright.
    """
    name_designation = TextData.create_text_data("New Designation")

    login_page = LoginPage(page)
    login_page.navigate_url(URL)
    login_page.login(USERNAME, PASSWORD)
    login_page.verify_login_success(USERNAME)

    designation_page = DesignationPage(page)
    designation_page.go_to_designation_page()
    designation_page.create_designation(NAME_DEPARTMENT, name_designation)
    designation_page.verify_create_success(NAME_DEPARTMENT, name_designation)

@pytest.mark.dependency(depends=["create_department"])
def test_create_designation(page: Page):
    """Kiểm thử quy trình tạo Designation mới gắn liền với phòng ban: đăng nhập, điều hướng tới
    trang Designation, tạo Designation mới và xác minh việc tạo thành công trong danh sách.

    Args:
        page (Page): Đối tượng Page của Playwright.
    """
    name_designation = TextData.create_text_data("New Designation")

    login_page = LoginPage(page)
    login_page.navigate(URL)
    login_page.login(USERNAME, PASSWORD)
    login_page.verify_login_success(USERNAME)

    designation_page = DesignationPage(page)
    designation_page.go_to_designation_page()
    designation_page.create_designation(NAME_DEPARTMENT, name_designation)
    designation_page.verify_create_success(NAME_DEPARTMENT, name_designation)

def test_create_policies(page: Page):
    name_policy = TextData.create_text_data("New Policies")
    policy_description = TextData.create_text_data("New Policy Description")
    file_path = PathFile.get_string_file("upload_files/test_policies.png")

    login_page = LoginPage(page)
    login_page.navigate(URL)
    login_page.login(USERNAME, PASSWORD)
    login_page.verify_login_success(USERNAME)

    policies_page = PoliciesPage(page)
    policies_page.go_to_policies_page()
    policies_page.create_policies(name_policy, policy_description, file_path)
    policies_page.verify_create_success(name_policy)

