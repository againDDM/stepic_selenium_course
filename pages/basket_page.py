from .base_page import BasePage   # pylint: disable=relative-beyond-top-level
from .locators import BasketPageLocators   # pylint: disable=relative-beyond-top-level
from selenium.webdriver.common.by import By


class BasketPage(BasePage):

    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "There are items in basket, but should not be"


    def should_be_empty_basket_message(self):
        assert bool("empty" in
            self.browser.find_element(*BasketPageLocators.CONTENT).text
        ), "There are not empty text"
