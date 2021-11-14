import allure
from page_objects.BasePage import BasePage
from page_objects.TestData import ProductPageTestData
from page_objects.ProductPage import ProductPageLocators


@allure.title("Тест на проверку видимости элемента 'Все изображения товара в одном блоке' на странице товара")
def test_thumbnails_block_visibility(browser, prod_url):
    product_page = BasePage(browser, prod_url)
    product_page.go_to_site()
    prod_thumbnails = product_page.find_element(ProductPageLocators.THUMBS_ELEM, 2)
    assert ProductPageTestData.THUMBS_ELEM_CLASS == product_page.get_property(prod_thumbnails, 'className'),\
        "Needs main thumbnails className to be equal to 'thumbnails'!"


@allure.title("Тест на проверку видимости 4х элементов 'изображения товара' на странице товара")
def test_thumbnails_visibility(browser, prod_url):
    product_page = BasePage(browser, prod_url)
    product_page.go_to_site()
    assert ProductPageTestData.THUMBS_QTY == product_page.get_quantity(ProductPageLocators.THUMBS_QTY),\
        "Quantity of elements should be equal to 4!"


@allure.title("Тест на проверку видимости элемента 'название товара' на странице товара")
def test_product_title_visibility(browser, prod_url):
    product_page = BasePage(browser, prod_url)
    product_page.go_to_site()
    title_elem = product_page.find_element(ProductPageLocators.PROD_TITLE, 2)
    assert ProductPageTestData.PROD_TITLE_VALUE == product_page.get_property(title_elem, 'textContent'),\
        "Needs h1 header should be equal to 'MacBook Air'!"


@allure.title("Тест на проверку видимости элемента 'поле для ввода количества товаров' на странице товара")
def test_input_of_quantity_visibility(browser, prod_url):
    product_page = BasePage(browser, prod_url)
    product_page.go_to_site()
    input_elem = product_page.find_element(ProductPageLocators.QTY_INPUT, 2)
    assert ProductPageTestData.QTY_INPUT_NAME == product_page.get_property(input_elem, 'name'),\
        "Needs name value should be equal to 'quantity'!"


@allure.title("Тест на проверку видимости элемента кнопки 'положить в корзину' на странице товара")
def test_cart_btn_visibility(browser, prod_url):
    product_page = BasePage(browser, prod_url)
    product_page.go_to_site()
    btn_elem = product_page.find_element(ProductPageLocators.CART_BTN, 2)
    assert ProductPageTestData.CART_BTN_ID == product_page.get_property(btn_elem, 'id'),\
        "Needs button id should be equal to 'button-cart'!"
