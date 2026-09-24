

import requests

from pages.base_page import BasePage


class LinksPage(BasePage):
    def verify_broken_link(self):
        broken_link = self.page.get_by_test_id("link-broken-same")
        href = broken_link.get_attribute("href")
        response = requests.get(href)
        assert response.status_code == 500, f"Expected code 500, instead was received {response.status_code}"
        return response.status_code