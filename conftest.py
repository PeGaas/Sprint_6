import pytest
from selenium import webdriver
from data_static import MAIN_URL


@pytest.fixture()
def firefox_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()
