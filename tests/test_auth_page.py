import allure
from page_objects.AuthPage import AuthPage
from page_objects.TestData import AuthPageTestData


@allure.title("Тест на проверку видимости элемента 'заголовок формы аутентификации' на странице входа в админку")
def test_form_title_visibility(browser, auth_url):
    auth_page = AuthPage(browser, auth_url)
    auth_page.go_to_site()
    user_form_title = auth_page.find_element(auth_page.AUTH_FORM_TITLE, 2)
    assert AuthPageTestData.AUTH_FORM_TITLE_CHECK == auth_page.get_property(user_form_title, 'innerText'), \
        "Needs title text should be equal to ' Please enter your login details.'!"


@allure.title("Тест на проверку видимости элемента 'поле ввода логина' на странице входа в админку")
def test_login_input_visibility(browser, auth_url):
    auth_page = AuthPage(browser, auth_url)
    auth_page.go_to_site()
    login_inp = auth_page.find_element(auth_page.USERNAME_INPUT, 2)
    assert AuthPageTestData.LOGIN_INPUT_ID == auth_page.get_property(login_inp, 'id'), \
        "Needs login input id should be equal to 'input-username'!"


@allure.title("Тест на проверку видимости элемента 'поле ввода пароля' на странице входа в админку")
def test_password_input_visibility(browser, auth_url):
    auth_page = AuthPage(browser, auth_url)
    auth_page.go_to_site()
    pass_inp = auth_page.find_element(auth_page.PASS_INPUT, 2)
    assert AuthPageTestData.PASS_INPUT_ID == auth_page.get_property(pass_inp, 'id'), \
        "Needs password input id should be equal to 'input-password'!"


@allure.title("Тест на проверку видимости элемента 'ссылка Забыли пароль' на странице входа в админку")
def test_forgot_password_visibility(browser, auth_url):
    auth_page = AuthPage(browser, auth_url)
    auth_page.go_to_site()
    forgot_btn = auth_page.find_element(auth_page.FORGOT_PASS_BTN, 2)
    assert AuthPageTestData.FORGOT_PASS_TEXT == auth_page.get_property(forgot_btn, 'innerText'), \
        "Needs forgot password text should be equal to 'Forgotten Password'!"


@allure.title("Тест на проверку видимости элемента 'кнопка Войти' на странице входа в админку")
def test_login_btn_visibility(browser, auth_url):
    auth_page = AuthPage(browser, auth_url)
    auth_page.go_to_site()
    login_btn = auth_page.find_element(auth_page.LOGIN_BTN, 2)
    assert AuthPageTestData.LOGIN_BTN_TYPE == auth_page.get_property(login_btn, 'type'), \
        "Needs login button type should be equal to 'submit'!"
