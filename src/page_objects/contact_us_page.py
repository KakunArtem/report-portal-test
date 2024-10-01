from playwright.sync_api import Page

from src.modetls.contact_us_model import ContactUsModel
from src.page_objects.base_page import BasePage


class ContactUsPage(BasePage):
    def __init__(self, page: Page) -> None:
        self._page = page
        self.first_name_field = self._page.locator('input.input[name="first_name"]')
        self.last_name_field = self._page.locator('input.input[name="last_name"]')
        self.email_field = self._page.locator('input.input[name="email"]')
        self.company_field = self._page.locator('input.input[name="company"]')
        self.agree_with_terms_checkbox = self._page.locator(
            "(//label[@class='custom-checkbox']//div[@class='custom-checkbox__checkmark'])[2]")
        self.send_request = self._page.locator("//button[@class='btn btn--primary btn--large']")
        self.thank_you_modal = self._page.locator(
            "//div[@class='contact-us-form__subtitle how-did-you-hear__subtitle']")

    def fill_contact_form(self, contact_us_object: ContactUsModel):
        self.first_name_field.fill(contact_us_object.first_name)
        self.last_name_field.fill(contact_us_object.last_name)
        self.email_field.fill(contact_us_object.email)
        self.company_field.fill(contact_us_object.company_name)
        self.agree_with_terms_checkbox.click()
        self.send_request.click()
        return self

    def is_thank_you_modal_displayed(self) -> bool:
        self.wait_for_element(self.thank_you_modal)
        return self.thank_you_modal.is_visible()
