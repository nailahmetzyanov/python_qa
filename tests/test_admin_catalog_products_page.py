import allure
from page_objects.AuthPage import AuthPage
from page_objects.AdminCatalogProductsPage import AdminCatalogProductsPage
from page_objects.TestData import AdminCatalogProductsPageTestData


@allure.title("Тест на проверку удаления случайного товара из каталога")
def test_delete_random_product(browser, local_admin_url):
    admin_page = AdminCatalogProductsPage(browser, local_admin_url)
    auth_page = AuthPage(browser, local_admin_url)
    auth_page.go_to_site()
    auth_page.enter_admin_page()
    admin_page.enter_catalog_products()
    total_products_qty = admin_page.get_quantity(AdminCatalogProductsPage.PRODUCT_ROW)
    admin_page.mark_random_product()
    admin_page.push_delete_btn()
    admin_page.alert_accept()
    assert admin_page.get_quantity(
        AdminCatalogProductsPage.PRODUCT_ROW) == total_products_qty, "Needs products quantity to be equal to 18"


@allure.title("Тест на проверку удаления всех товаров из каталога")
def test_delete_all_products(browser, local_admin_url):
    admin_page = AdminCatalogProductsPage(browser, local_admin_url)
    auth_page = AuthPage(browser, local_admin_url)
    auth_page.go_to_site()
    auth_page.enter_admin_page()
    admin_page.enter_catalog_products()
    admin_page.mark_all_products_together()
    admin_page.push_delete_btn()
    admin_page.alert_accept()
    assert AdminCatalogProductsPageTestData.NO_RESULTS_TEXT == admin_page.get_property(
        admin_page.find_element(AdminCatalogProductsPage.NO_RESULTS_ELEM, 2),
        'outerText'), "Needs quantity of products to be equal to 'No results!"


@allure.title("Тест на проверку добавления в каталог нового товара")
def test_add_product(browser, local_admin_url):
    admin_page = AdminCatalogProductsPage(browser, local_admin_url)
    auth_page = AuthPage(browser, local_admin_url)
    auth_page.go_to_site()
    auth_page.enter_admin_page()
    admin_page.enter_catalog_products()
    total_products_qty = admin_page.get_quantity(AdminCatalogProductsPage.PRODUCT_ROW)
    admin_page.push_add_new_btn()
    admin_page.enter_data(AdminCatalogProductsPage.PROD_NAME_INP, AdminCatalogProductsPageTestData.PROD_NAME_DATA)
    admin_page.enter_data(AdminCatalogProductsPage.META_TAG_TITLE_INP,
                          AdminCatalogProductsPageTestData.META_TAG_TITLE_DATA)
    admin_page.move_and_click(AdminCatalogProductsPage.DATA_TAB)
    admin_page.enter_data(AdminCatalogProductsPage.MODEL_INP, AdminCatalogProductsPageTestData.MODEL_DATA)
    admin_page.move_and_click(AdminCatalogProductsPage.SAVE_BTN)
    assert admin_page.get_quantity(AdminCatalogProductsPage.PRODUCT_ROW) == total_products_qty + 1,\
        "Needs total products quantity to be equal to: total + 1!"
