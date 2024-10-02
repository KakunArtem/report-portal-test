from playwright.sync_api import Page

from src.configuration import config
from src.page_objects.base_page import BasePage


class ReportPortalDashBoardPage(BasePage):
    def __init__(self, page: Page) -> None:
        page.wait_for_url(config.DASHBOARD_URL)
        self._page = page
        self.side_bar = self._page.locator("aside[class='sidebar__sidebar--mc65e']")
        self.all_launches_dropdown = self._page.locator(
            "div[class='allLatestDropdown__value--QwA8E allLatestDropdown__active--qisno']")

    def is_side_bar_displayed(self) -> bool:
        self.wait_for_element(self.side_bar)
        return self.side_bar.is_visible()

    def is_all_launches_dropdown_displayed(self) -> bool:
        self.wait_for_element(self.all_launches_dropdown)
        return self.all_launches_dropdown.is_visible()
