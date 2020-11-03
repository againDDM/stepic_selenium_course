from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (
        By.CSS_SELECTOR,
        ".basket-mini .btn-group a"
    )


class BasketPageLocators():
    BASKET_URL = "http://selenium1py.pythonanywhere.com/basket/"
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")
    CONTENT = (By.CSS_SELECTOR, ".content #content_inner p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


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
