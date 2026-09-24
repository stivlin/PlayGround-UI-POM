import re
from playwright.sync_api import expect
from pages.base_page import BasePage


class DropdownPage(BasePage):

    def select_one_element(self) -> str:
        dropdown = self.page.get_by_test_id("fruit-select")
        result = self.page.get_by_test_id("result-s01")
        dropdown.select_option(label="Apple")

        expect(result).to_contain_text(re.compile(r"Apple|Banana|Orange"))
        return result.inner_text()


    def select_by_value(self):
        country = self.page.get_by_test_id("country-select")
        country.select_option(value="india")
 
        result = self.page.get_by_test_id("result-s02")
        expect(result).to_contain_text("india")
        return result.inner_text()

    def select_last(self):
        dropdown = self.page.get_by_test_id("language-select")
        all_options = dropdown.locator("option")
        count = all_options.count()
        dropdown.select_option(index=count-1)
        result = self.page.get_by_test_id("result-s03")
        expect(result).to_contain_text("TypeScript")
        return result.inner_text()

    def select_from_list_box(self):
        dropdown = self.page.get_by_test_id("priority-dropdown-trigger")
        dropdown.click()
        self.page.get_by_role("listbox").get_by_text("High Priority").click()

        result = self.page.get_by_test_id("result-s05")
        expect(result).to_contain_text("High Priority")
        return result.inner_text()

    def select_from_combobox(self, city_name: str) -> str:
        self.page.pause()
        comobox = self.page.locator('//label[normalize-space()="City"]/following-sibling::div//input')
        comobox.fill(city_name)
        option = self.page.get_by_role("option", name=city_name)
        option.click()
        result = self.page.get_by_test_id("result-s06")
        expect(result).to_contain_text(city_name)
        return result.inner_text()
