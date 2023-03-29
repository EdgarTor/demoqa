from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    LOGO_LINK = (By.CSS_SELECTOR, "header  a")
    LOGO_IMAGE = (By.CSS_SELECTOR, "header  a > img")
    BANNER_LINK = (By.CSS_SELECTOR, "div.home-content div.home-banner > a")
    BANNER_IMAGE = (By.CSS_SELECTOR, "div.home-content div.home-banner > a > img.banner-image")
    CARDS = (By.CSS_SELECTOR, "div.card.mt-4.top-card h5")
    ELEMENTS_CARD = (By.XPATH, "//div[contains(@class, 'card')]/h5[text()='Elements']")

    def click_on_logo(self):
        self.click_on_element(*self.LOGO_LINK)

    def click_on_banner(self):
        self.click_on_element(*self.BANNER_LINK)

    def get_banner_link_href(self):
        return self.get_elements_attribute_value(*self.BANNER_LINK, "href")

    def get_banner_link_target(self):
        return self.get_elements_attribute_value(*self.BANNER_LINK, "target")

    def get_banner_image_src(self):
        return self.get_elements_attribute_value(*self.BANNER_IMAGE, "src")

    def get_banner_image_alt(self):
        return self.get_elements_attribute_value(*self.BANNER_IMAGE, "alt")

    def get_card_elements(self):
        return self.get_multiple_elements(*self.CARDS)

    def click_on_elements_card(self):
        self.scroll_to_the_element(*self.ELEMENTS_CARD)
        self.click_on_element(*self.ELEMENTS_CARD)



