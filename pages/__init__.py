from pages.buttons_page import ButtonsPage

from pages.dropdown_page import DropdownPage
from pages.forms_page import FormsPage
from pages.links_page import LinksPage
from pages.main_page import MainPage
from pages.input_fields_page import InputFieldsPage

class Pages:
    def __init__(self, page):
        self.page = page
        self.main = MainPage(page)
        self.input_fields = InputFieldsPage(page)
        self.buttons_page = ButtonsPage(page)
        self.dropdown = DropdownPage(page)
        self.links_page = LinksPage(page)
        self.froms_page = FormsPage(page)