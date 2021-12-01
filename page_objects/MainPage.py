from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_SLIDER = (By.CSS_SELECTOR, "#slideshow0")
    CART = (By.CSS_SELECTOR, "#cart")
    SEARCH = (By.CSS_SELECTOR, "#search")
    LOGO_CAROUSEL = (By.CSS_SELECTOR, "#carousel0")
    PRODUCTS = (By.CSS_SELECTOR, ".product-layout")
