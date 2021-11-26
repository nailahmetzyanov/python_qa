import allure
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import common


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step("Looking for the unique element {locator} on the page")
    def find_element(self, locator: tuple, time=10):
        self.logger.info("Finding element: {}".format(locator))
        try:
            return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator),
                                                           message=f"Can't find element by locator {locator}")
        except TimeoutException:
            allure.attach(self.browser.get_screenshot_as_png(),
                          name=f"error_{self.browser.name}" + ".png",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Can't find element by locator {locator}")
        except common.exceptions.NoSuchElementException:
            allure.attach(self.browser.get_screenshot_as_png(),
                          name=f"error_{self.browser.name}" + ".png",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Element {locator} not found on the page!")

    @allure.step("Looking for same elements on the page")
    def find_elements(self, locator: tuple, time=10):
        self.logger.info("Finding elements: {}".format(locator))
        return WebDriverWait(self.browser, time).until(EC.visibility_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    @allure.step("Verifying if the element {locator} is on the page")
    def verify_element_presence(self, locator: tuple, time=10):
        self.logger.info("Verifying element {} presence".format(locator))
        try:
            return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(self.browser.get_screenshot_as_png(),
                          name=f"error_{self.browser.name}" + ".png",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Can't find element by locator {locator}")

    @allure.step("Going to page")
    def go_to_site(self):
        self.logger.info("Moving to url: {}".format(self))
        return self.browser.get(self.url)

    @allure.step("Getting property of the element")
    def get_property(self, element: object, prop: str):
        self.logger.info("Getting property: {} of element: {}".format(prop, element))
        return element.get_property(prop)

    @allure.step("Getting quantity of elements")
    def get_quantity(self, locator: tuple):
        self.logger.info("Getting quantity of elements: {}".format(locator))
        return len(self.find_elements(locator, 2))

    @allure.step("Clicking the element (without moving)")
    def simple_click(self, locator: tuple):
        self.logger.info("Clicking element: {}".format(locator))
        self.find_element(locator).click()

    @allure.step("Moving the mouse to the element and clicking it")
    def move_and_click(self, locator: tuple):
        self.logger.info("Moving and clicking element: {}".format(locator))
        ActionChains(self.browser).pause(0.3).move_to_element(self.find_element(locator)).pause(0.3).click().perform()

    @allure.step("Getting the page title")
    def get_page_title(self):
        self.logger.info("Getting page {} title".format(self.url))
        return self.browser.title

    @allure.step("Approving the allert message")
    def alert_accept(self):
        self.logger.info("Accepting alert: {}".format(self.browser.switch_to.alert))
        self.browser.switch_to.alert.accept()

    @allure.step("Denying the allert message")
    def alert_dismiss(self):
        self.logger.info("Denying alert: {}".format(self.browser.switch_to.alert))
        self.browser.switch_to.alert.dismiss()

    @allure.step("Entering data to the input")
    def enter_data(self, locator: tuple, value: str):
        self.logger.info("Entering data: {} to element {}".format(value, locator))
        self.find_element(locator, 2).send_keys(value)
