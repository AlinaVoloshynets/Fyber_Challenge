from pageobjects.pageobject import pageobject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Western_Movies(pageobject):
    def __init__(self):
        ######  page elements defined  ######
        self.xpath_western_movies_link = '//*[@id="sidebar"]/div[6]/span/ul/li[23]/a'
        self.xpath_movies_items = '//*[@id="main"]/div/table[@class="results"]/tbody/tr'
        self.movies_list = (By.XPATH, '//*[@id="main"]/div/table[@class="results"]')

    ###### behaviour ######
    def verify_count_of_western_movies_more_than_one(self):
        self.find_element(self.xpath_western_movies_link).click()
        self.wait_until_visibile(self.movies_list)
        assert self.count_elements(self.xpath_movies_items) >= 1