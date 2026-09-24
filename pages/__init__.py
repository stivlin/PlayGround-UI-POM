from pages.buttons import ButtonsPage

from pages.dropdown import DropdownPage
from pages.main_page import MainPage
from pages.input_fields_page import InputFieldsPage

class Pages:
    def __init__(self, page):
        self.page = page
        self.main = MainPage(page)
        self.input_fields = InputFieldsPage(page)
        self.buttons_page = ButtonsPage(page)
        self.dropdown = DropdownPage(page)