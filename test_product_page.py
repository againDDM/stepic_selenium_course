import time
import pytest
from .pages.product_page import ProductPage   # pylint: disable=relative-beyond-top-level
from .pages.locators import ProductPageLocators   # pylint: disable=relative-beyond-top-level
from .pages.locators import LoginPageLocators   # pylint: disable=relative-beyond-top-level
from .pages.login_page import LoginPage   # pylint: disable=relative-beyond-top-level
from .pages.basket_page import BasketPage   # pylint: disable=relative-beyond-top-level


@pytest.mark.need_review
@pytest.mark.parametrize(
    'link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ]
)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product_name()
    page.check_product_price()


@pytest.mark.xfail(reason="I was forced to write this falling test.")
@pytest.mark.parametrize(
    'link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
        "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/",
    ]
)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize(
    'link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
        "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/",
    ]
)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="I was forced to write this falling test.")
@pytest.mark.parametrize(
    'link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
        "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/",
    ]
)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items()
    basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LoginPageLocators.LOGIN_URL)
        login_page.open()
        login_page.register_new_user(
            email = f"{id(self)}{str(time.time())}@fakemail.org",
            password = f"{id(self)}{str(time.time())}",
        )
        login_page.should_be_authorized_user()


    @pytest.mark.xfail(reason="I was forced to write this falling test.")
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.success_message_should_be_disappeared()


    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.check_product_name()
        page.check_product_price()
