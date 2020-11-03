from .base_page import BasePage   # pylint: disable=relative-beyond-top-level
from .locators import MainPageLocators   # pylint: disable=relative-beyond-top-level
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
