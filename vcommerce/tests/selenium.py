import pytest

from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture(scope="module")
def edge_browser_instance(request):
    """
    Provide Selenium Web driver instance.
    """
    options = Options()
    browser = webdriver.Edge(options)
    yield browser
    browser.close()
