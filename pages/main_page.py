from pages.base_page import BasePage
from pages.buttons_page import ButtonsPage
from pages.dropdown_page import DropdownPage
from pages.input_fields_page import InputFieldsPage
from pages.links_page import LinksPage


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

    def select_dropdown_page(self):
        button_link = self.page.get_by_test_id("new-practice-card-dropdowns")
        button_link.wait_for(state="visible", timeout=5000)
        button_link.click()
        return DropdownPage(self.page)

    def select_links_page(self):
        button_link = self.page.get_by_test_id("new-practice-card-links")
        button_link.wait_for(state="visible", timeout=5000)
        button_link.click()
        return LinksPage(self.page)
