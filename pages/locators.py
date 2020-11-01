from selenium.webdriver.common.by import By


class MainPageLocators():
    MAINT_URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    ADD_PRODUCT_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div.alert-success div.alertinner strong")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages div.alert-info div.alertinner strong")
    PAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
