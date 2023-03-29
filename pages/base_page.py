from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    BASE_URL = "https://demoqa.com/"

    def __init__(self, browser):
        self.browser = browser

    def open(self, url=""):
        if url:
            complete_url = self.BASE_URL + url
            self.browser.get(complete_url)
        else:
            self.browser.get(self.BASE_URL)

    def click_on_element(self, how, what, wait=False, timeout=4):
        if wait:
            element = WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((how, what)))
            element.click()
        else:
            element = self.browser.find_element(how, what)
            element.click()

    def scroll_to_the_element(self, how, what):
        element = self.browser.find_element(how, what)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def get_multiple_elements(self, how, what):
        try:
            elements = self.browser.find_elements(how, what)
        except NoSuchElementException:
            return False
        return elements

    def get_page_title(self):
        return self.browser.title

    def get_page_current_url(self):
        return self.browser.current_url

    def get_elements_attribute_value(self, how, what, attr):
        element = self.browser.find_element(how, what)
        return element.get_attribute(attr)

    def get_text(self, how, what):
        element = self.browser.find_element(how, what)
        return element.text

