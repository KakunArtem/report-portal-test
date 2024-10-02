import pytest
from playwright.sync_api import Page

from src.modetls.contact_us_model import ContactUsModel
from src.page_objects.contact_us_page import ContactUsPage
from src.page_objects.main_page import MainPage


class TestMainPage:

    @pytest.mark.description("Verify that the user can enter the ‘Demo page’ and see the dashboard")
    def test_login_to_demo_page(self, page: Page):
        report_portal_dashboard_page = (MainPage(page)
                                        .open_main_page()
                                        .click_try_demo()
                                        .click_login_button())

        assert report_portal_dashboard_page.is_side_bar_displayed() is True
        assert report_portal_dashboard_page.is_all_launches_dropdown_displayed() is True

    @pytest.mark.description("Verify that a user can fill out the Contact Us form and submitting a request")
    def test_fill_contact_us_request(self, page: Page):
        contact_object = ContactUsModel(
            first_name="John",
            last_name="Doe",
            email="john.doe@test.com",
            company_name="Test company.")

        main_page = MainPage(page)
        (main_page
         .open_main_page()
         .click_get_a_quote()
         .fill_contact_form(contact_object))

        assert ContactUsPage(page).is_thank_you_modal_displayed() is True
