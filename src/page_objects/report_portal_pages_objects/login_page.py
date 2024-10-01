from playwright.sync_api import Page

from src.page_objects.base_page import BasePage
from src.page_objects.report_portal_pages_objects.dash_board_page import ReportPortalDashBoardPage


class ReportPortalLoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        self._page = page
        self.login_button = self._page.locator("button[type='submit']")

    def click_login_button(self) -> ReportPortalDashBoardPage:
            self.login_button.click()
            return ReportPortalDashBoardPage(self._page)
