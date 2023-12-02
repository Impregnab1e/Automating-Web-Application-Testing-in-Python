import pytest


@pytest.fixture()
def good_word():
    return "кашалот"


@pytest.fixture()
def bad_word():
    return "кошолот"
