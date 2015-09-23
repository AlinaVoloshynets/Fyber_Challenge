from pageobjects.pageobject import pageobject
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class Top_250_Movies(pageobject):
    def __init__(self):
    ######  page elements defined  ######
        self.xpath_movie_list = '//*/table/tbody[@class="lister-list"]/tr'
        self.xpath_sort_by = '//*/select[@class="lister-sort-by"]'

    ###### behaviour ######
    def verify_count_of_movies_more_than_one(self):
        assert self.count_elements(self.xpath_movie_list) >= 1

    def verify_count_of_movies_more_than_one_with_sorting_options(self):
        sortBySelect = Select(self.find_element(self.xpath_sort_by))
        for option in sortBySelect.options:
            sortBySelect.select_by_visible_text(option.text)
            self.verify_count_of_movies_more_than_one()