

from playwright.sync_api import expect

from pages.base_page import BasePage


class FormsPage(BasePage):
    def login_form(self, email: str, password: str):
        email_field = self.page.get_by_test_id("input-login-email")
        email_field.fill(email)
        password_field = self.page.locator("#login-password")
        password_field.fill(password)
        self.page.get_by_test_id("btn-login-submit").click()
        login_result = self.page.get_by_test_id("result-login")
        expect(login_result).to_contain_text(email)
        return login_result.inner_text()


    def personal_detail_form(self,first_name:str , last_name:str, phone: int, date_birth:str):
        first = self.page.get_by_test_id("input-first-name")
        last = self.page.get_by_test_id("input-last-name")
        first.fill(first_name)
        last.fill(last_name)
        number = self.page.get_by_test_id("input-phone")
        number.fill(phone)
        date = self.page.get_by_test_id("input-dob")
        date.fill(date_birth)
        self.page.get_by_test_id("radio-gender-male").click()
        self.page.locator("#personalSubmitBtn").click()

        if self.page.locator("#phoneError"):
            errorphone = self.page.locator("#phoneError").inner_text()
            return errorphone

        result = self.page.get_by_test_id("result-personal")
        expect(result).to_contain_text(first_name, last_name)
        return result.inner_text()


    def address_form(self, country_id:str = None, city_name: str = None ):
        self.page.pause()
        country_locator = self.page.get_by_test_id("select-country")
        country_locator.select_option(value=country_id)
        city_locator = self.page.get_by_test_id("input-city")
        city_locator.fill(city_name)
        about = self.page.locator("#bio")
        about.fill("lin baba is the best")
        self.page.get_by_test_id("btn-address-submit").click()

        self.page.get_by_test_id("result-address")
        result = self.page.get_by_test_id("result-address")
        expect(result).to_contain_text("Address saved")
        return result.inner_text()

    def address_form_validation_error(self, country_id: str = None, city_name: str = None):
        about = self.page.locator("#bio")
        about.fill("Some bio text")

        self.page.get_by_test_id("btn-address-submit").click()

        errors = []

        if country_id is None:
            country_error = self.page.locator("[data-testid='error-country']")
            if country_error.is_visible():
                errors.append(country_error.inner_text())

        if city_name is None:
            city_error = self.page.locator("[data-testid='error-city']")
            if city_error.is_visible():
                errors.append(city_error.inner_text())

        expect(country_error or city_error).to_be_visible()
        return errors

    def interest_form(self):
        interests = ["Playwright", "Selenium", "Cypress", "Appium", "Jest"]
        self.page.pause()
        for interest in interests:
            self.page.get_by_label(interest).click()
        self.page.get_by_test_id("btn-interests-submit").click()

        alert = self.page.get_by_text("select at least")
        if alert.is_visible():
            return alert.inner_text()
        result = self.page.get_by_test_id("result-interests")
        expect(result).to_contain_text(f"Interests saved")
        return result.inner_text()

    def account_setup_form_error(self, password: str):
        input_pass = self.page.get_by_test_id("input-password")
        self.page.pause()
        input_conf_pass = self.page.get_by_test_id("input-confirm-password")
        input_pass.fill(password)
        input_conf_pass.fill("")
        self.page.get_by_test_id("submit-form-btn").click()

        errors = []

        if self.page.get_by_test_id("error-confirm-password").is_visible():
            confirm_password = self.page.get_by_test_id("error-confirm-password")
            errors.append(confirm_password.inner_text())

        if self.page.locator("#termsError").is_visible():
            terms = self.page.locator("#termsError")
            errors.append(terms.inner_text())

        expect(confirm_password or terms).to_be_visible()
        return errors

    def account_setup_form_success(self, password: str = "SecurePass123"):
        input_pass = self.page.get_by_test_id("input-password")
        input_conf_pass = self.page.get_by_test_id("input-confirm-password")
        input_pass.fill(password)
        input_conf_pass.fill(password)

        self.page.locator("#terms").click()

        self.page.get_by_test_id("submit-form-btn").click()

        success_msg = self.page.get_by_test_id("form-success-msg")
        submitted_name = self.page.get_by_test_id("submitted-name")

        expect(success_msg).to_be_visible()
        expect(submitted_name).to_be_visible()

        return submitted_name.inner_text()

