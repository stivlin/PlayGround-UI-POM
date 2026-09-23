from pages.base_page import BasePage
from pages.buttons import ButtonsPage
from pages.input_fields_page import InputFieldsPage


class MainPage(BasePage):
    def select_input(self):
        input_link= self.page.get_by_role("link", name="Input Fields Beginner")
        input_link.wait_for(state="visible", timeout=5000)
        input_link.click()
        return InputFieldsPage(self.page)

    def select_buttons_page(self):
        button_link = self.page.get_by_test_id("new-practice-card-buttons")
        button_link.wait_for(state="visible", timeout=5000)
        button_link.click()
        return ButtonsPage(self.page)

