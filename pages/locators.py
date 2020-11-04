from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (
        By.CSS_SELECTOR,
        ".basket-mini .btn-group a"
    )
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_URL = "http://selenium1py.pythonanywhere.com/basket/"
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")
    CONTENT = (By.CSS_SELECTOR, ".content #content_inner p")


class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGESTRATION_EMAIL = (
        By.CSS_SELECTOR, 'input.form-control[name="registration-email"]'
    )
    REGESTRATION_PASSWORD_MAIN = (
        By.CSS_SELECTOR, 'input.form-control[name="registration-password1"]'
    )
    REGESTRATION_PASSWORD_REPEAT = (
        By.CSS_SELECTOR, 'input.form-control[name="registration-password2"]'
    )
    REGESTRATION_BUTTON = (
        By.CSS_SELECTOR, 'button[name="registration_submit"]'
    )


class MainPageLocators():
    MAINT_URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET_BUTTON = (
        By.CSS_SELECTOR,
        ".btn-add-to-basket"
    )
    ALERT_PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "#messages div.alert-success div.alertinner strong"
    )
    ALERT_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "#messages div.alert-info div.alertinner strong"
    )
    PAGE_PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "div.product_main h1"
    )
    PAGE_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "div.product_main p.price_color"
    )
    SUCCESS_MESSAGE = ALERT_PRODUCT_NAME
