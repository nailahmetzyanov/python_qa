from selenium.webdriver.common.by import By


class ProductPageLocators:
    THUMBS_ELEM = (By.CSS_SELECTOR, ".thumbnails")
    THUMBS_QTY = (By.CSS_SELECTOR, ".thumbnail")
    PROD_TITLE = (By.CSS_SELECTOR, "div.btn-group + h1")
    QTY_INPUT = (By.CSS_SELECTOR, "input[name=quantity]")
    CART_BTN = (By.CSS_SELECTOR, "#button-cart")
