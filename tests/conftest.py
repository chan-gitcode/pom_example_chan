import pytest
from utils.path_helper import PathFile
from page import HomePage, LoginPage, DepartmentPage, DesignationPage, PoliciesPage

@pytest.fixture(scope ="session")
def get_credential():
    credential = PathFile.read_json_data("input_data/config.json")
    yield credential

@pytest.fixture(scope="function")
def login(page):
    return LoginPage(page)

@pytest.fixture
def logged_in_home(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    homePage = HomePage(page)
    yield homePage


@pytest.fixture
def logged_in_department(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    departmentPage = DepartmentPage(page)

    yield departmentPage


@pytest.fixture
def logged_in_designation(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    designation = DesignationPage(page)
    yield designation


@pytest.fixture
def logged_in_policy(page, login, get_credential):
    login.login(
        get_credential["URL"],
        get_credential["USERNAME"],
        get_credential["PASSWORD"]
    )
    policy = PoliciesPage(page)
    yield policy




