from playwright.sync_api import Page

from src.configuration import config


class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open_home_page(self):
        self.page.goto(config.BASE_URL)
        return self
