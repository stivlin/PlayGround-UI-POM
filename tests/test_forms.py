import allure
from faker import Faker
import pytest
from playwright.sync_api import expect

faker = Faker()



@allure.feature("forms")
@allure.title("Address form validation - missing city only")
def test_address_form_missing_city(app):
    app.main.select_forms_page()
    errors = app.froms_page.address_form_validation_error(country_id="us", city_name=None)
    error_text = " ".join(errors).lower()
    assert "city" in error_text, f"Expected city error, got: {errors}"

@allure.feature("forms")
@allure.title("Address form validation - missing country only")
def test_address_form_missing_country(app):
    app.main.select_forms_page()
    errors = app.froms_page.address_form_validation_error(country_id=None, city_name="New York")
    error_text = " ".join(errors).lower()
    assert "country" in error_text, f"Expected country error, got: {errors}"

@allure.feature("forms")
@allure.title("login form")
@pytest.mark.parametrize("email, password",[
    (faker.email(), faker.password())
])
def test_login_form(app, email, password):
    app.main.select_forms_page()
    login = app.froms_page.login_form(email, password)
    assert login == f"Login successful! Welcome, {email}."

@allure.feature("forms")
@allure.title("Personal Details")
@pytest.mark.parametrize("first_name, last_name, phone, date_birth",[
    (faker.name(), faker.last_name(), faker.phone_number(), faker.date_of_birth().strftime("%Y-%m-%d"))
])
def test_verify_personal_details(app, first_name, last_name, phone, date_birth):
    app.main.select_forms_page()
    details = app.froms_page.personal_detail_form(first_name, last_name, phone, date_birth)
    assert details == f"Phone must be exactly 10 digits."

@allure.feature("forms")
@allure.title("Address form validation")
def test_addres_form(app, city_id: str = "Mumbai", country: str = "IN"):
    app.main.select_forms_page()
    result = app.froms_page.address_form(country, city_id)
    assert result == f"Address saved: {city_id}, India"

# Negative test case
@allure.feature("forms")
@allure.title("Address form validation - missing country and city")
def test_address_form_missing_required_fields(app):
    app.main.select_forms_page()
    errors = app.froms_page.address_form_validation_error(country_id=None, city_name=None)
    assert len(errors) > 0, "Expected validation errors but got none"
    error_text = " ".join(errors).lower()
    assert "country" in error_text or "city" in error_text, f"Expected country/city errors but got: {errors}"

@allure.feature("forms")
@allure.title("Check interest form")
def test_interest_form(app):
    app.main.select_forms_page()
    result = app.froms_page.interest_form()
    assert result != "Please select at least one interest."

@allure.feature("forms")
@allure.title("Account setup validation - password mismatch and terms")
def test_account_setup_error(app):
    app.main.select_forms_page()
    errors = app.froms_page.account_setup_form_error("123456")

    # Verify errors exist
    assert len(errors) > 0, "Expected validation errors but got none"

    # Join errors for easier checking
    error_text = " ".join(errors).lower()

    # Verify password mismatch error
    assert "passwords do not match" in error_text or "password" in error_text, \
        f"Expected password mismatch error, got: {errors}"

    # Verify terms acceptance error
    assert "accept" in error_text or "terms" in error_text, \
        f"Expected terms acceptance error, got: {errors}"

@allure.feature("forms")
@allure.title("Account setup success, valid form submission")
def test_account_setup_success(app):
    app.main.select_forms_page()
    result = app.froms_page.account_setup_form_success()

    # Verify success message appears
    assert result == "Your account has been secured."