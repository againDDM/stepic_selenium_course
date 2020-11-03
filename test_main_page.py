from .pages.main_page import MainPage   # pylint: disable=relative-beyond-top-level
from .pages.locators import MainPageLocators   # pylint: disable=relative-beyond-top-level
from .pages.login_page import LoginPage   # pylint: disable=relative-beyond-top-level
from .pages.basket_page import BasketPage   # pylint: disable=relative-beyond-top-level


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


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MainPageLocators.MAINT_URL)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items()
    basket_page.should_be_empty_basket_message()
