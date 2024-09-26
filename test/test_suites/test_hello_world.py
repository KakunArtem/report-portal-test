from playwright.sync_api import Page

from src.configuration import config


class TestHelloWorld:


    def test_hello_world(self, page: Page):
        page.goto(config.BASE_URL)
        pass
