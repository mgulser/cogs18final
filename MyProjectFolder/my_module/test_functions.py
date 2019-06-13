"""Test for my functions"""

from my_functions import *

def test_movie_info():

    assert movie_info(arrival, "rating") == 7.9

    assert isinstance(movie_info(arrival,"description"), str)

    assert isinstance(movie_info(arrival,"rating"), float)


test_movie_info()
