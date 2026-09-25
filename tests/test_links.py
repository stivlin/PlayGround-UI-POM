import allure

@allure.feature("Links")
@allure.title("Verify broken link returns 500 status")
def test_broken_link(app):
    app.main.select_links_page()
    link = app.links_page.verify_broken_link()
    assert link == 500, f"a different code was expected, you got {link}"


