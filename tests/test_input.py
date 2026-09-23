import allure
@allure.feature("Input field test")
@allure.title("enter movie name")
def test_scenario_1(app):
    app.main.select_input()
    result = app.input_fields.add_movie("Matrix")
    assert result.inner_text() == "You entered: Matrix"

@allure.feature("Input field test")
@allure.title("append movie")
def test_scenario_2(app):
    app.main.select_input()
    result = app.input_fields.append_movie("Endgame")
    assert result.inner_text() == "Current value: Avengers, Endgame"

@allure.feature("Input field test")
@allure.title("Read values")
def test_scenario_3(app):
    app.main.select_input()
    result = app.input_fields.read_value()
    assert result.inner_text() == "Value: The Matrix"

@allure.feature("Input field test")
@allure.title("clear button")
def test_scenario_4(app):
    app.main.select_input()
    result = app.input_fields.clear_field()
    assert result == "Field cleared ✓", "field is not empty"

@allure.feature("Input field test")
@allure.title("button disabled")
def test_scenario_5(app):
    app.main.select_input()
    assert app.input_fields.verify_input_disabled(), f"Input is abled"

@allure.feature("Input field test")
@allure.title("Read Only")
def test_scenario_6(app):
    app.main.select_input()
    result = app.input_fields.verify_read_only()
    assert "Readonly" in result