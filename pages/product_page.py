from .base_page import BasePage   # pylint: disable=relative-beyond-top-level
from .locators import ProductPageLocators   # pylint: disable=relative-beyond-top-level
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON)
        button.click()


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"


    def check_product_name(self):
        page_product_name = self.browser.find_element(
            *ProductPageLocators.PAGE_PRODUCT_NAME
        ).text
        alert_product_name =self.browser.find_element(
            *ProductPageLocators.ALERT_PRODUCT_NAME
        ).text
        assert page_product_name == alert_product_name, \
            "Incorrect product name"


    def check_product_price(self):
        page_product_price = self.browser.find_element(
            *ProductPageLocators.PAGE_PRODUCT_PRICE
        ).text
        alert_product_price =self.browser.find_element(
            *ProductPageLocators.ALERT_PRODUCT_PRICE
        ).text
        assert page_product_price == alert_product_price, \
            "Incorrect product price"
