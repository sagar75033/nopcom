from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


################### For pytest reports #########################
# hook for adding environment info in html report

def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project , nopcommerce'
    config.stash[metadata_key]['Modul Name'] = 'Admin Login Test'
    config.stash[metadata_key]['Tester Name'] = 'Sagar'


# hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
