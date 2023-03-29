from .helpers.json_parser import JsonParser
from .pages.main_page import MainPage
from .pages.elements_page import ElementsPage


class TestElementsPage:
    EXERCISE_PAGE_DATA = JsonParser.read_from_json("test_data/exercises_page_data.json")

    def test_check_that_user_can_open_elements_page(self, browser):
        page = MainPage(browser)
        page.open()

        page.click_on_elements_card()
        elements_page = ElementsPage(browser)
        page_url = elements_page.get_page_current_url()

        current_page_title = elements_page.get_page_title()
        expected_page_title = self.EXERCISE_PAGE_DATA["page_title"]
        elements_header_title = elements_page.get_text(*elements_page.ELEMENTS_TITLE)
        expected_elements_header_title = self.EXERCISE_PAGE_DATA["elements_section"]["title"]
        elements_default_message = elements_page.get_text(*elements_page.DEFAULT_STATE_MESSAGE)
        expected_elements_default_message = self.EXERCISE_PAGE_DATA["elements_section"]["default_state_msg"]

        assert page_url == (elements_page.BASE_URL + elements_page.URL), "Elements page has incorrect url"
        assert current_page_title == expected_page_title, "The page titles is incorrect"
        assert elements_header_title == expected_elements_header_title, "Elements menu has incorrect header text"
        assert elements_default_message == expected_elements_default_message, "Elements menu has incorrect default text"

    def test_check_that_main_page_is_opened_after_clicking_on_logo(self, browser):
        page = ElementsPage(browser)
        page.open(page.URL)

        logo_link_href = page.get_logo_link_href()
        expected_logo_link_href = self.EXERCISE_PAGE_DATA["logo"]["link_href"]
        logo_image_src = page.get_logo_image_src()
        expected_logo_image_src = self.EXERCISE_PAGE_DATA["logo"]["image_src"]

        assert logo_link_href == expected_logo_link_href, "The banner link is incorrect"
        assert logo_image_src == expected_logo_image_src, "The banner image is incorrect"

        page.click_on_the_logo()
        main_page = MainPage(browser)

        assert main_page.get_page_current_url() == page.BASE_URL

    def test_accordion_menu_elements(self, browser):
        page = ElementsPage(browser)
        page.open(page.URL)

        accordion_menu_data = self.EXERCISE_PAGE_DATA["accordion_menu_items"]
        accordion_menu_items = page.get_accordion_menu_items_texts()
        accordion_menu_collapsable_items = page.get_accordion_menu_collapsable_items()

        i = 0
        while i < len(accordion_menu_data):
            if i == 0:
                assert page.check_if_element_has_show_class(accordion_menu_collapsable_items[i]), "The Elements menu " \
                                                                                                  "isn't opened"
            else:
                assert not page.check_if_element_has_show_class(accordion_menu_collapsable_items[i]), "On Elements " \
                                                                                                      "page other " \
                                                                                                      "menus are also " \
                                                                                                      "opened"
            assert accordion_menu_items[i].text == accordion_menu_data[i]["menu_title"], "The order of accordion menus has" \
                                                                                 "been changed or some elements are " \
                                                                                         "missing"
            i += 1




