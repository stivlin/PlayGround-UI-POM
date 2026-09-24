import allure

@allure.feature("dropdown")
@allure.title("Select fruit from the list")
def test_select_element(app):
    app.main.select_dropdown_page()
    fruit = app.dropdown.select_one_element()
    assert "Apple" in fruit

@allure.feature("dropdown")
@allure.title("Select by value from the list")
def test_select_by_value(app):
    app.main.select_dropdown_page()
    value = app.dropdown.select_by_value()
    assert value == "Selected country: India (india)"

@allure.feature("dropdown")
@allure.title("Select the last from the list")
def test_select_the_last(app):
    app.main.select_dropdown_page()
    last = app.dropdown.select_last()
    assert last == "Selected language: TypeScript"

@allure.feature("dropdown")
@allure.title("Select city from combobox")
def test_select_from_combobox(app):
    app.main.select_dropdown_page()
    result = app.dropdown.select_from_combobox("Mumbai")
    assert "Mumbai" in result

@allure.feature("dropdown")
@allure.title("Select High Priority")
def test_select_high_priority(app):
    app.main.select_dropdown_page()
    priority = app.dropdown.select_from_list_box()
    assert priority == "Priority selected: High Priority"