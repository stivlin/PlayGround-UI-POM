
def test_scenario_1(app):
    app.main.select_input()
    result = app.input_fields.add_movie("Matrix")
    assert result.inner_text() == "You entered: Matrix"


def test_scenario_2(app):
    app.main.select_input()
    result = app.input_fields.append_movie("Endgame")
    assert result.inner_text() == "Current value: Avengers, Endgame"

def test_scenario_3(app):
    app.main.select_input()
    result = app.input_fields.read_value()
    assert result.inner_text() == "Value: The Matrix"

def test_scenario_4(app):
    app.main.select_input()
    result = app.input_fields.clear_field()
    assert result == "Field cleared ✓", "field is not empty"

def test_scenario_5(app):
    app.main.select_input()
    assert app.input_fields.verify_input_disabled, f"Input is abled"

def test_scenario_6(app):
    app.main.select_input()
    result = app.input_fields.verify_read_only()
    assert "Readonly" in result