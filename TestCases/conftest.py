from selenium import webdriver
from Utilities.readProperties import ReadConfig
import pytest


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()

    driver.maximize_window()

    # Navigate to URL from config.ini
    url = ReadConfig.getApplicationURL()
    driver.get(url)

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

