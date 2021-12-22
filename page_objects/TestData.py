

# Класс с данными элементов Главной страницы для проверки
class MainPageTestData:
    MAIN_SLIDER_ID = "slideshow0"
    CART_ID = "cart"
    SEARCH_ID = "search"
    LOGO_CAROUSEL_ID = "carousel0"
    PRODUCT_CLASS_QTY = 4


# Класс с данными элементов Хедера
class HeaderTestData:
    EURO_SIGN_CHECK = '€'
    GBP_SIGN_CHECK = '£'
    USD_SIGN_CHECK = '$'


# Класс с данными элементов Продуктовой страницы
class ProductPageTestData:
    THUMBS_ELEM_CLASS = 'thumbnails'
    THUMBS_QTY = 4
    PROD_TITLE_VALUE = 'MacBook Air'
    QTY_INPUT_NAME = 'quantity'
    CART_BTN_ID = "button-cart"


# Класс с данными элементов страницы Каталога
class CatalogPageTestData:
    ASIDE_MENU_ID = 'column-left'
    BANNER_ID = 'banner0'
    LIST_VIEW_BTN_ID = 'list-view'
    GRID_VIEW_BTN_ID = 'grid-view'
    ALL_PRODUCTS_QTY = 5


# Класс с данными элементов страницы Регистрации пользователя
class UserRegisterPageTestData:
    FIRST_NAME_DATA = 'Nail'
    LAST_NAME_DATA = 'Ahmetzyanov'
    EMAIL_DATA = 'automation'
    TELEPHONE_DATA = '89170000000'
    PASS_DATA = 'qwerty987'
    PASS_CONFIRM_DATA = 'qwerty987'
    SUCCESS_REGISTER_PAGE_TITLE = 'Your Account Has Been Created!'


# Класс с данными элементов страницы Аутентификации
class AuthPageTestData:
    USER_LOGIN = 'user'
    USER_PASS = 'bitnami'
    AUTH_FORM_TITLE_CHECK = ' Please enter your login details.'
    LOGIN_INPUT_ID = 'input-username'
    PASS_INPUT_ID = 'input-password'
    FORGOT_PASS_TEXT = 'Forgotten Password'
    LOGIN_BTN_TYPE = 'submit'


# Класс с данными элементов страницы Админки (каталог/продукты)
class AdminCatalogProductsPageTestData:
    NO_RESULTS_TEXT = 'No results!'
    PROD_NAME_DATA = 'New product'
    META_TAG_TITLE_DATA = 'New product'
    MODEL_DATA = 'New model'
