import time

from seleniumbase import BaseCase


class GitHubTests(BaseCase):
    def slow_click(self, css_selector):
        time.sleep(1)
        self.click(css_selector)

    def test_github(self):
        self.open("https://github.com/")
        self.update_text("input.header-search-input", "SeleniumBase\n")
        self.slow_click('a[href="/seleniumbase/SeleniumBase"]')
        self.assert_element("div.repository-content")
        self.assert_text("SeleniumBase", "h1")
        self.slow_click('a[title="seleniumbase"]')
        self.slow_click('a[title="fixtures"]')
        self.slow_click('a[title="base_case.py"]')
        self.assert_text("Code", "nav a.selected")
