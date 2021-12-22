import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from page_objects.TestData import UserRegisterPageTestData
import random
import string


# Класс с локаторами элементов Хедера
class UserRegisterPage(BasePage):
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    PASS_INPUT = (By.CSS_SELECTOR, '#input-password')
    CONFIRM_PASS_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    AGREE_POLICY_BOX = (By.CSS_SELECTOR, "input[name=agree")
    CONTINUE_BTN = (By.CSS_SELECTOR, "input[value=Continue")
    SUCCESS_BLOCK = (By.CSS_SELECTOR, "#common-success")

    @allure.step("Entering data into chosen input")
    def fill_in_input(self, value: str):
        if value == 'First Name':
            self.logger.info("Filling in input: {} with data {}".format(value,
                                                                        UserRegisterPageTestData.FIRST_NAME_DATA))
            element = self.find_element(UserRegisterPage.FIRST_NAME_INPUT)
            element.send_keys(UserRegisterPageTestData.FIRST_NAME_DATA)
        elif value == "Last Name":
            self.logger.info("Filling in input: {} with data {}".format(value, UserRegisterPageTestData.LAST_NAME_DATA))
            element = self.find_element(UserRegisterPage.LAST_NAME_INPUT)
            element.send_keys(UserRegisterPageTestData.LAST_NAME_DATA)
        elif value == "E-Mail":
            self.logger.info("Filling in input: {} with data {}".format(value, UserRegisterPageTestData.EMAIL_DATA +
                                                                        str(random.randint(1, 1000)) + "_" +
                                                                        random.choice(string.ascii_letters) +
                                                                        "@gmail.com"))
            element = self.find_element(UserRegisterPage.EMAIL_INPUT)
            element.send_keys(UserRegisterPageTestData.EMAIL_DATA + str(random.randint(1, 1000)) + "_" + random.choice(
                string.ascii_letters) + "@gmail.com")
        elif value == "Telephone":
            self.logger.info("Filling in input: {} with data {}".format(value,
                                                                        UserRegisterPageTestData.TELEPHONE_DATA))
            element = self.find_element(UserRegisterPage.TELEPHONE_INPUT)
            element.send_keys(UserRegisterPageTestData.TELEPHONE_DATA)
        elif value == "Password":
            self.logger.info("Filling in input: {} with data {}".format(value, UserRegisterPageTestData.PASS_DATA))
            element = self.find_element(UserRegisterPage.PASS_INPUT)
            element.send_keys(UserRegisterPageTestData.PASS_DATA)
        elif value == "Password Confirm":
            self.logger.info("Filling in input: {} with data {}".format(value,
                                                                        UserRegisterPageTestData.PASS_CONFIRM_DATA))
            element = self.find_element(UserRegisterPage.CONFIRM_PASS_INPUT)
            element.send_keys(UserRegisterPageTestData.PASS_CONFIRM_DATA)

    @allure.step("Entering all data into inputs of the new user registration form")
    def fill_in_register_form(self):
        self.fill_in_input('First Name')
        self.fill_in_input('Last Name')
        self.fill_in_input('E-Mail')
        self.fill_in_input('Telephone')
        self.fill_in_input('Password')
        self.fill_in_input('Password Confirm')

    @allure.step("Agreeing with policy agreement")
    def agree_with_policy(self):
        self.simple_click(self.AGREE_POLICY_BOX)

    @allure.step("Pushing continue button")
    def push_continue_btn(self):
        self.simple_click(self.CONTINUE_BTN)
