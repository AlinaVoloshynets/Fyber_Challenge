from utils.browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class pageobject(object):
    def __init__(self):
        self.driver = Browser.getDriver()

    def go_to_url(self,url):
        Browser.go_to(url)

    def verify_page_title(self, title):
        assert title in Browser.title()

    def wait_until_visibile(self, locator):
        Browser.wait().until(EC.visibility_of_element_located(locator))

    def find_element(self, xpath):
        return Browser.get_driver().find_element_by_xpath(xpath)

    def find_elements(self, xpath):
        return Browser.get_driver().find_elements_by_xpath(xpath)

    def count_elements(self, xpath):
        return len(self.find_elements(xpath))