from selenium.webdriver.common.by import By


class CatalogPageLocators:
    ASIDE_MENU = (By.CSS_SELECTOR, "#column-left")
    BANNER = (By.CSS_SELECTOR, "#banner0")
    LIST_VIEW_BTN = (By.CSS_SELECTOR, "#list-view")
    GRID_VIEW_BTN = (By.CSS_SELECTOR, "#grid-view")
    PRODUCTS = (By.CSS_SELECTOR, ".product-layout")
