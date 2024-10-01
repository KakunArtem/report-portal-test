from playwright.sync_api import Page

from src.configuration.time_out_constants import TimeOutConstants


class BasePage:
    @staticmethod
    def wait_for_element(locator) -> None:
        locator.wait_for(state='visible', timeout=TimeOutConstants.TIME_OUT_10_SECONDS)

    @staticmethod
    def get_relevant_context(page: Page) -> Page:
        page.reload(wait_until='networkidle', timeout=TimeOutConstants.TIME_OUT_10_SECONDS)
        return page
