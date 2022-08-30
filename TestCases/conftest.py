import pytest
from selenium import webdriver
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
    else:
        driver= webdriver.Firefox()
    return driver

def pytest_addoption(parser):  # this will get the value from cLI or hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")

#pytest html report
# It is hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'customers'
    config._metadata['tester'] = 'priya'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)