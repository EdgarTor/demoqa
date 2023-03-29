from .helpers.json_parser import JsonParser
from .pages.main_page import MainPage


class TestMainPage:
    MAIN_PAGE_DATA = JsonParser.read_from_json("test_data/main_page_data.json")

    def test_check_main_page_title(self, browser):
        page = MainPage(browser)
        page.open()

        current_page_title = page.get_page_title()
        expected_page_title = self.MAIN_PAGE_DATA["page_title"]

        assert current_page_title == expected_page_title, "The page titles is incorrect"

    def test_check_that_banner_image_and_logo_have_correct_attributes(self, browser):
        page = MainPage(browser)
        page.open()

        banner_image_src = page.get_banner_image_src()
        expected_banner_image_src = self.MAIN_PAGE_DATA["home_banner"]["img_src"]
        banner_image_alt = page.get_banner_image_alt()
        expected_banner_image_alt = self.MAIN_PAGE_DATA["home_banner"]["img_alt"]

        assert banner_image_src == expected_banner_image_src, "The banner images source is incorrect"
        assert banner_image_alt == expected_banner_image_alt, "The banner image alt is incorrect"

    def test_that_banner_page_is_opened_on_a_new_tab(self, browser):
        page = MainPage(browser)
        page.open()

        banner_link_href = page.get_banner_link_href()
        expected_banner_link_href = self.MAIN_PAGE_DATA["home_banner"]["link_href"]
        banner_link_target = page.get_banner_link_target()
        expected_banner_link_target = self.MAIN_PAGE_DATA["home_banner"]["link_target"]

        assert banner_link_href == expected_banner_link_href, "The banner link is incorrect"
        assert banner_link_target == expected_banner_link_target, "The banner link target should be '_blank'"

        page.click_on_banner()
        new_tab = browser.window_handles[1]
        browser.switch_to.window(new_tab)
        banner_new_tab_url = page.get_page_current_url()

        assert banner_new_tab_url == banner_link_href, "After clicking on banner, the wrong page is opened"

    def test_cards_texts(self, browser):
        page = MainPage(browser)
        page.open()

        cards_data = self.MAIN_PAGE_DATA["cards"]
        card_elements = page.get_card_elements()

        i = 0
        while i < len(cards_data):
            assert cards_data[i]["text"] == card_elements[i].text, "The order of elements has been changed," \
                                                                   " or some elements are missing"
            i += 1


