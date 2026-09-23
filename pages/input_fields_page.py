from .base_page import BasePage
from playwright.sync_api import expect



class InputFieldsPage(BasePage):

    MOVIE_NAME_INPUT = '[data-testid="input-movie-name"]'
    SUBMIT_MOVIE_BUTTON = '[data-testid="btn-submit-movie"]'
    RESULT = '[data-testid="result-s01"]'

    INP_APPEND = '[data-testid="input-append"]'
    RESULT_S02 = '[data-testid="result-s02"]'

    RESULT_S03 = '[data-testid="result-s03"]'
    READ_VALUE = '[data-testid="btn-read-value"]'
    INPUT_READ_VALUE = '[data-testid="input-read-value"]'

    INPUT_CLEAR = '[data-testid="input-clear"]'
    BTN_CLEAR = '[data-testid="btn-clear-field"]'
    RESULT_S04 = '[data-testid="result-s04"]'

    INPUT_DISABLED = '[data-testid="input-disabled"]'

    RESULT_S06 = '[data-testid="result-s06"]'


    def verify_loaded(self):
        self.page.get_by_role(
            "heading", name="Input Field Automation Practice"
        ).wait_for()
        print ("OK")

    def add_movie(self,movie: str):
        result = self.page.locator(self.RESULT)

        self.page.locator(self.MOVIE_NAME_INPUT).fill(movie)
        self.page.locator(self.SUBMIT_MOVIE_BUTTON).click()

        expect(result).to_contain_text(movie)
        return result

    def append_movie(self, movie: str):
        input_field = self.page.locator(self.INP_APPEND)
        result = self.page.locator(self.RESULT_S02)
        previous_movie = input_field.input_value()

        input_field.click()
        input_field.press("End")
        self.page.keyboard.type(f", {movie}")
        input_field.press("Tab")

        expected_value = f"Current value: {previous_movie}, {movie}"
        expect(result).to_have_text(expected_value)
        return result

    def read_value(self) -> str:
        result = self.page.locator(self.RESULT_S03)
        input_field = self.page.locator(self.INPUT_READ_VALUE)
        self.page.locator(self.READ_VALUE).click()

        read_value = input_field.input_value()
        expected_value = f"Value: {read_value}"

        expect(result).to_contain_text(expected_value)
        return result

    def verify_input_disabled(self):
        input_value = self.page.locator(self.INPUT_DISABLED)
        expect(input_value).to_be_disabled()
        return input_value 

    def clear_field(self):
        result = self.page.locator(self.RESULT_S04)
        input_field = self.page.locator(self.INPUT_CLEAR)
        input_field.fill("")
        self.page.locator(self.BTN_CLEAR).click()

        expect(input_field).to_be_empty()
        return result.inner_text()

    def verify_read_only(self):
        result = self.page.locator(self.RESULT_S06)
        
        expect(result).to_contain_text("Readonly")
        return result.inner_text()