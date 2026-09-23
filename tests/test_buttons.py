import allure

@allure.feature("buttons")
@allure.title("check first scenario")
def test_btn_scenario_1(app):
    app.main.select_buttons_page()
    response = app.buttons_page.verify_home_button()
    assert "Home" in response

@allure.feature("buttons")
@allure.title("Button Label")
def test_btn_correct_label(app):
    app.main.select_buttons_page()
    label = app.buttons_page.get_label()
    assert label == "Go To Home"

@allure.feature("buttons")
@allure.title("Location")
def test_btn_scenario_2(app):
    app.main.select_buttons_page()
    location = app.buttons_page.get_location()
    assert location is not None
    assert location["x"] > 0
    assert location["y"] > 0

@allure.feature("buttons")
@allure.title("Get Color")
def test_get_background(app):
    app.main.select_buttons_page()
    bg_color = app.buttons_page.get_background_color()
    assert bg_color == "Background: rgb(237, 233, 254)"

@allure.feature("buttons")
@allure.title("Double click")
def test_double_click(app):
    app.main.select_buttons_page()
    output = app.buttons_page.verify_double_click()
    assert output == "Double clicked!"

@allure.feature("buttons")
@allure.title("context click")
def test_press_context_click(app):
    app.main.select_buttons_page()
    values = app.buttons_page.press_context_click()
    assert values[0] != values[1]
    assert values[1] == "Context menu triggered!"

@allure.feature("buttons")
@allure.title("keep click")
def test_keep_mouse_click(app):
    app.main.select_buttons_page()
    btn_held = app.buttons_page.keep_click_pressed()
    assert btn_held == "Held for 1.5s"

@allure.feature("buttons")
@allure.title("disable button")
def test_disable_button(app):
    app.main.select_buttons_page()
    btn_disabled = app.buttons_page.check_disable_button()
    assert btn_disabled is True