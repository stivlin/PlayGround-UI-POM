from core.browser import BrowserDriver
from core.config import BASE_URL
from pages import Pages
import pytest


@pytest.fixture(scope="session")
def browser_driver():
    driver = BrowserDriver()
    driver.start()
    yield driver
    driver.stop()

@pytest.fixture()
def app(browser_driver):
    context = browser_driver.new_context()
    playwright_page = context.new_page()
    playwright_page.goto(BASE_URL)
    app = Pages(playwright_page)
    yield app
    context.close()