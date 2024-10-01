from playwright.sync_api import Page

from src.configuration import config
from src.configuration.time_out_constants import TimeOutConstants
from src.page_objects.base_page import BasePage
from src.page_objects.contact_us_page import ContactUsPage
from src.page_objects.report_portal_pages_objects.login_page import ReportPortalLoginPage


class MainPage(BasePage):
    def __init__(self, page: Page) -> None:
        self._page = page
        self._try_demo_button = self._page.locator(
            "//div[@class='showcase__btn-group']//a[@data-gtm='start_free_trial']")
        self._get_a_quote_button = self._page.locator("//div[@class='showcase__btn-group']//a[@data-gtm='get_a_quote']")

    def open_main_page(self):
        self._page.goto(config.BASE_URL)
        self._page.wait_for_url(config.BASE_URL, timeout=TimeOutConstants.TIME_OUT_10_SECONDS)
        return self

    def click_try_demo(self) -> ReportPortalLoginPage:
        with self._page.context.expect_page() as report_portal_login_page:
            self._try_demo_button.click()
            return ReportPortalLoginPage(report_portal_login_page.value)

    def click_get_a_quote(self) -> ContactUsPage:
        self._get_a_quote_button.click()
        return ContactUsPage(self._page)
