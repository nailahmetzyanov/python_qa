import allure
from page_objects.BasePage import BasePage
from page_objects.TestData import CatalogPageTestData
from page_objects.CatalogPage import CatalogPageLocators


@allure.title("Тест на проверку видимости элемента 'боковое меню' на странице каталога")
def test_aside_menu_visibility(browser, cat_url):
    catalog_page = BasePage(browser, cat_url)
    catalog_page.go_to_site()
    aside_menu_elem = catalog_page.find_element(CatalogPageLocators.ASIDE_MENU, 2)
    assert CatalogPageTestData.ASIDE_MENU_ID == catalog_page.get_property(aside_menu_elem, 'id'),\
        "Needs aside menu id should be equal to 'column-left'!"


@allure.title("Тест на проверку видимости элемента 'баннер' на странице каталога")
def test_banner_visibility(browser, cat_url):
    catalog_page = BasePage(browser, cat_url)
    catalog_page.go_to_site()
    banner_elem = catalog_page.find_element(CatalogPageLocators.BANNER, 2)
    assert CatalogPageTestData.BANNER_ID == catalog_page.get_property(banner_elem, 'id'),\
        "Needs banner id should be equal to 'banner0'!"


@allure.title("Тест на проверку видимости элемента 'кнопка вывода - list' на странице каталога")
def test_list_btn_visibility(browser, cat_url):
    catalog_page = BasePage(browser, cat_url)
    catalog_page.go_to_site()
    list_btn = catalog_page.find_element(CatalogPageLocators.LIST_VIEW_BTN, 2)
    assert CatalogPageTestData.LIST_VIEW_BTN_ID == catalog_page.get_property(list_btn, 'id'),\
        "Needs list view button id should be equal to 'list-view'!"


@allure.title("Тест на проверку видимости элемента 'кнопка вывода - grid' на странице каталога")
def test_grid_btn_visibility(browser, cat_url):
    catalog_page = BasePage(browser, cat_url)
    catalog_page.go_to_site()
    grid_btn = catalog_page.find_element(CatalogPageLocators.GRID_VIEW_BTN, 2)
    assert CatalogPageTestData.GRID_VIEW_BTN_ID == catalog_page.get_property(grid_btn, 'id'),\
        "Needs list view button id should be equal to 'grid-view'!"


@allure.title("Тест на проверку видимости 5 продуктовых карточек на странице каталога с товарами")
def test_products_visibility(browser, cat_url):
    catalog_page = BasePage(browser, cat_url)
    catalog_page.go_to_site()
    assert CatalogPageTestData.ALL_PRODUCTS_QTY == catalog_page.get_quantity(
        CatalogPageLocators.PRODUCTS), "Quantity of elements should be equal to 5!"
