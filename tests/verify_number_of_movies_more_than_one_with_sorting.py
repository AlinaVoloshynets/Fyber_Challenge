import pytest
from utils.browser import Browser
from pageobjects.top_250_movies_page import Top_250_Movies


def test_verify_number_of_movies_more_than_one_with_sorting():
    top_movies = Top_250_Movies()
    top_movies.go_to_url('http://www.imdb.com/chart/top')
    top_movies.verify_page_title("Top 250")
    top_movies.verify_count_of_movies_more_than_one_with_sorting_options()

def teardown_function(function):
    Browser.quit()
