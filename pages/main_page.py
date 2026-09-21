from pages.base_page import BasePage
from pages.buttons import ButtonsPage
from pages.input_fields_page import InputFieldsPage


class MainPage(BasePage):
    def select_input(self):
        self.page.get_by_role("link", name="Input Fields Beginner").click()
        return InputFieldsPage(self.page)

    def select_buttons_page(self):
        self.page.get_by_selector("new-practice-card-buttons").click()
        return ButtonsPage(self.page)

