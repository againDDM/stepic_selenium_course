from .base_page import BasePage   # pylint: disable=relative-beyond-top-level
from .locators import LoginPageLocators   # pylint: disable=relative-beyond-top-level


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "It is not login page"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Register form is not presented"


    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGESTRATION_EMAIL)\
            .send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.REGESTRATION_PASSWORD_MAIN
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGESTRATION_PASSWORD_REPEAT
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGESTRATION_BUTTON
        ).click()
