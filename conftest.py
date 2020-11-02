import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language', action='store',
        default='en', help="Choose language"
    )


@pytest.fixture(scope="module")
def browser(request):
    options = Options()
    options.add_experimental_option(
        'prefs', {
            'intl.accept_languages': request.config.getoption("language"),
        }
    )
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope="function", autouse=True)
def clear_cookie(browser):
    browser.delete_all_cookies()
