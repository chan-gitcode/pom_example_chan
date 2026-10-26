import pytest
from utils.text_data import TextData
import time


NAME_DEPARTMENT = TextData.create_text_data("New Department")
NAME_DESIGNATION = TextData.create_text_data("New Designation")
NAME_POLICIES = TextData.create_text_data("New Policies")

def test_create_department(logged_in_department):
    logged_in_department.go_to_department_page()
    logged_in_department.create_department(NAME_DEPARTMENT)
    logged_in_department.verify_create_success(NAME_DEPARTMENT)

# def test_create_designation(logged_in_designation):
#     logged_in_designation.go_to_designation_page()
#     logged_in_designation.create_designation(NAME_DESIGNATION)
#     logged_in_designation.verify_create_success(NAME_DESIGNATION)

# def test_create_policies(logged_in_policy):
#     logged_in_policy.go_to_policies_page()
#     logged_in_policy.create_policies(NAME_POLICIES)
#     logged_in_policy.verify_create_success(NAME_POLICIES)

def test_click_menu(logged_in_designation):
    locator_corehr = logged_in_designation.page.get_by_role("link", name="Core HR")
    locator_designation = logged_in_designation.page.get_by_role("link", name="Designation")
    time.sleep(5000)
    logged_in_designation.click(locator_corehr)
    logged_in_designation.click(locator_designation)

    