from playwright.sync_api import sync_playwright
from page.login_page import LoginPage
import pytest

@pytest.fixture(scope="session")
def browser_instance():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    yield browser
    browser.close()
    p.stop()

@pytest.fixture(scope = "function")
def page(browser_instance):
    context = browser_instance.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    page.close()
    context.close()