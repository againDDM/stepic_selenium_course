from .pages.main_page import MainPage   # pylint: disable=relative-beyond-top-level
from .pages.locators import MainPageLocators   # pylint: disable=relative-beyond-top-level
from .pages.login_page import LoginPage   # pylint: disable=relative-beyond-top-level


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MainPageLocators.MAINT_URL)
    page.open()
    page.should_be_login_link()
