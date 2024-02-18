import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    """
    Create a driver
    """    
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
