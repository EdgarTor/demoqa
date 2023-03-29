from selenium.webdriver.common.by import By

from .base_page import BasePage


class ElementsPage(BasePage):
    URL = "elements"
    LOGO_LINK = (By.CSS_SELECTOR, "header a")
    LOGO_IMAGE = (By.CSS_SELECTOR, "header a > img")
    ELEMENTS_TITLE = (By.CSS_SELECTOR, "div.playgound-header  div.main-header")
    DEFAULT_STATE_MESSAGE = (By.CSS_SELECTOR, "div.row > div:nth-child(2)")
    ACCORDION_ITEMS_TITLES_LIST = (By.CSS_SELECTOR, "div.accordion div.element-group div.header-text")
    ACCORDION_MENU_COLLAPSABLE_ITEMS = (By.CSS_SELECTOR, "div.accordion div.element-group div.element-list.collapse")

    def get_logo_link_href(self):
        return self.get_elements_attribute_value(*self.LOGO_LINK, "href")

    def get_logo_image_src(self):
        return self.get_elements_attribute_value(*self.LOGO_IMAGE, "src")

    def click_on_the_logo(self):
        self.click_on_element(*self.LOGO_LINK)

    def get_accordion_menu_items_texts(self):
        return self.get_multiple_elements(*self.ACCORDION_ITEMS_TITLES_LIST)

    def get_accordion_menu_collapsable_items(self):
        return self.get_multiple_elements(*self.ACCORDION_MENU_COLLAPSABLE_ITEMS)

    def check_if_element_has_show_class(self, element):
        classes = element.get_attribute("class")
        if "show" in classes:
            return True
        return False
