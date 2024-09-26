import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

@pytest.fixture(scope="session")
def browser() -> Browser:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope="session")
def browser_context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="session")
def page(browser_context: BrowserContext) -> Page:
    page = browser_context.new_page()
    yield page
    page.close()
