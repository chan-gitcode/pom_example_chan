from playwright.sync_api import Page, Locator, Error as PlaywrightError, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_url(self, url: str):
        try:
            self.page.goto(url)
        except PlaywrightError as e:
            raise PlaywrightError(f"Cannot navigate to URL: {url}") from e

    def click(self, element_locator: Locator):
        try:
            element_locator.click()
        except PlaywrightError as e:
            raise PlaywrightError(
                f"Fail to click on test object {element_locator}"
            ) from e

    def set_text(self, element_locator: Locator, input_value: str):
        try:
            element_locator.fill(input_value)
        except PlaywrightError as e:
            raise PlaywrightError(
                f"Fail to input {input_value} in object {element_locator}"
            ) from e

    def select_dropdown(self, element_locator: Locator, option: str, by_label: bool = False):
        try:
            if by_label:
                element_locator.select_option(label=option)
            else:
                element_locator.select_option(value=option)
        except PlaywrightError as e:
            select_by = "label" if by_label else "value"
            raise PlaywrightError(
                f"Fail to choose option '{option}' (by {select_by}) in dropdown {element_locator}"
            ) from e

    def upload_file(self, element_locator: Locator, file_path: str):
        try:
            element_locator.set_input_files(file_path)
        except FileNotFoundError as e:
            raise PlaywrightError(
                f"File not found for upload: '{file_path}'"
            ) from e
        except PlaywrightError as e:
            raise PlaywrightError(
                f"Fail to find upload file '{file_path}' in {element_locator}"
            ) from e

    def verify_element_visible(self, element_locator: Locator):
        try:
            expect(element_locator). to_be_visible()
        except PlaywrightError as e:
            raise PlaywrightError(
                f" Element don't visible in page: {element_locator}"
            ) from e
        
    def verify_element_text(self, element_locator: Locator, expected_text: str, is_extract: bool = True):
        try:
            if is_extract:
                expect(element_locator).to_have_text(expected_text)
        except PlaywrightError as e:
            mode = "have_text" if is_extract else "contains_text"
            raise PlaywrightError(
                f"Fail to verify text | Element: {element_locator}"
                f"| Expected: '{expected_text} | Mode: {mode}"
            ) from e

    def _click_open_new_tab(self, locator: Locator, timeout: int = 10000):
        with self.page.context.expect_page(timeout=timeout) as new_page:
            locator.click()

        new_page_info = new_page.value
        new_page_info.wait_for_load_state("load")
        return new_page_info

    def _bring_to_front(self):
        self.page.bring_to_front()

    def _page_close(self):
        self.page.close()

