from .base_page import BasePage   # pylint: disable=relative-beyond-top-level
from .locators import MainPageLocators   # pylint: disable=relative-beyond-top-level
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
