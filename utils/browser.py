from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from configs import configs

class Browser(object):
    driver = webdriver.Firefox()

    @classmethod
    def get_driver(cls):
        return cls.driver

    @classmethod
    def wait(cls):
        return WebDriverWait(cls.driver, timeout=configs.wait)

    @classmethod
    def maximize_window(cls):
        cls.driver.maximize_window()

    @classmethod
    def open(cls):
        driver = cls.driver.Firefox()
        cls.driver.maximize_window()

    @classmethod
    def quit(cls):
        cls.driver.quit()

    @classmethod
    def title(cls):
        return cls.driver.title

    @classmethod
    def go_to(cls, url):
        cls.driver.get(url)
        cls.driver.maximize_window()
