import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language', action='store',
        default='en', help="Choose language"
    )


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_experimental_option(
        'prefs', {
            'intl.accept_languages': request.config.getoption("language"),
        }
    )
    options.add_argument("--window-position=-1920,0")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
