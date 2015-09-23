import pytest
from utils.browser import Browser
from pageobjects.western_movies_page import Western_Movies

def test_verify_number_of_movies_more_than_one():
    western_movie = Western_Movies()
    western_movie.go_to_url('http://www.imdb.com/chart/top')
    western_movie.verify_page_title("Top 250")
    western_movie.verify_count_of_western_movies_more_than_one()
    western_movie.verify_page_title("Western")

def teardown_function(function):
    Browser.quit()
