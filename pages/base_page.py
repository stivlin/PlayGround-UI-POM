class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def wait_for_page(self):
        self.page.wait_for_load_state("domcontentloaded")

    def is_visible(self, selector: str ) -> bool:
        self.page.locator(selector).is_visible()