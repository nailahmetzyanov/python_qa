import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from random import randint


class AdminCatalogProductsPage(BasePage):
    CATALOG_BTN = (By.CSS_SELECTOR, 'a[href*="#collapse1"]')
    PRODUCTS_BTN = (By.CSS_SELECTOR, 'a[href*="product&user"]')
    PRODUCT_ROW = (By.CSS_SELECTOR, 'tr')
    MARK_BOX = (By.CSS_SELECTOR, 'thead > tr > td:nth-child(1) > input[type=checkbox]')
    NO_RESULTS_ELEM = (By.CSS_SELECTOR, 'tbody > tr > td')
    DELETE_BTN = (By.CSS_SELECTOR, '.btn-danger')
    ADD_NEW_BTN = (By.CSS_SELECTOR, 'a[href*="add&user"]')
    PROD_NAME_INP = (By.CSS_SELECTOR, '#input-name1')
    META_TAG_TITLE_INP = (By.CSS_SELECTOR, '#input-meta-title1')
    DATA_TAB = (By.CSS_SELECTOR, 'a[href*="#tab-data"]')
    MODEL_INP = (By.CSS_SELECTOR, '#input-model')
    SAVE_BTN = (By.CSS_SELECTOR, 'button[type=submit]')

    @allure.step("Pushing catalog button in navigation menu")
    def push_catalog_link(self):
        self.move_and_click(self.CATALOG_BTN)

    @allure.step("Pushing products button in navigation menu")
    def push_products_link(self):
        self.move_and_click(self.PRODUCTS_BTN)

    @allure.step("Pushing catalog button + products button in navigation menu")
    def enter_catalog_products(self):
        self.move_and_click(self.CATALOG_BTN)
        self.move_and_click(self.PRODUCTS_BTN)

    @allure.step("Find and mark random product in products list")
    def mark_random_product(self):
        random_product = randint(0, self.get_quantity(self.PRODUCT_ROW))
        self.move_and_click(
            (By.CSS_SELECTOR, f'tbody > tr:nth-child({random_product}) > td:nth-child(1) > input[type=checkbox]'))

    @allure.step("Find and mark all the products in products list one by one")
    def mark_all_products_by_one(self):
        quantity = self.get_quantity(self.PRODUCT_ROW)
        for i in range(1, quantity):
            self.move_and_click(
                (By.CSS_SELECTOR, f'tbody > tr:nth-child({i}) > td:nth-child(1) > input[type=checkbox]'))

    @allure.step("Mark all the products with one action")
    def mark_all_products_together(self):
        self.move_and_click(self.MARK_BOX)

    @allure.step("Pushing delete product button")
    def push_delete_btn(self):
        self.move_and_click(self.DELETE_BTN)

    @allure.step("Pushing add new product button")
    def push_add_new_btn(self):
        self.move_and_click(self.ADD_NEW_BTN)
