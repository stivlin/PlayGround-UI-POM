from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page


class BrowserDriver:
    def __init__(self, browser_name: str = "chromium", headless: bool = False):
        self.browser_name = browser_name
        self._playwright = None
        self.headless = headless
        self._browser: Browser | None = None

    def start(self):
        self._playwright = sync_playwright().start()
        browser_type = getattr(self._playwright, self.browser_name)
        self._browser = browser_type.launch(headless=self.headless)
        return self._browser

    def new_context(self, **kwargs) -> BrowserContext:
        return self._browser.new_context(**kwargs)

    def new_page(self, context: BrowserContext | None = None) -> Page:
        context = context or self.new_context()
        return context.new_page()


    def stop(self) -> None:
        if self._browser is not None:
            self._browser.close()
        if self._playwright is not None:
            self._playwright.stop()