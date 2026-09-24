

from playwright.sync_api import expect

from pages.base_page import BasePage


class ButtonsPage(BasePage):

    def verify_home_button(self):
        btn = self.page.get_by_test_id("btn-navigate-home")
        btn.click()
        result = self.page.get_by_test_id("result-s01")
        expect(result).to_contain_text("Home")
        return result.inner_text()

    def get_label(self):
        label = self.page.get_by_text("Go To Home")
        return label.inner_text()

    def get_location(self):
        btn_location = self.page.get_by_test_id("btn-get-coordinates")
        btn_location.click()

        box = self.page.get_by_test_id("result-s02").bounding_box()
        if box:
            x = box["x"]
            y = box["y"]
        return box

    def get_background_color(self) -> str:
        bg_color = self.page.get_by_test_id("btn-navigate-home").evaluate(
            "el => getComputedStyle(el).backgroundColor"
        )
        self.page.get_by_test_id("btn-get-color").click()
        result_field = self.page.get_by_test_id("result-s03")

        expect(result_field).to_contain_text(f"Background: {bg_color}")
        return result_field.inner_text() 

    def verify_double_click(self):
        initial_value = self.page.get_by_test_id("result-s07")
        dc_btn = self.page.get_by_test_id("btn-double-click")
        dc_btn.dblclick()
        new_value = self.page.get_by_test_id("result-s07")
        return new_value.inner_text()

    def press_context_click(self) -> list:
        result_field = self.page.get_by_test_id("result-s08")
        initial_value = result_field.inner_text()

        btn_right = self.page.get_by_test_id("btn-right-click")
        btn_right.click(button= "right")

        expect(result_field).to_have_text("Context menu triggered!")
        new_value = result_field.inner_text()

        return [initial_value, new_value]

    def keep_click_pressed(self):
        result_field = self.page.get_by_test_id("result-s06")
        
        btn_hold = self.page.get_by_test_id("btn-click-hold")
        btn_hold.click(delay=1500)
        
        expect(result_field).to_contain_text("Held")
        output = result_field.inner_text()
        return output

    def check_disable_button(self) -> bool:
        return self.page.get_by_test_id("btn-disabled").is_disabled()

    
