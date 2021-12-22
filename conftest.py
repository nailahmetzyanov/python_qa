import logging
import time
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.events import AbstractEventListener

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO, filename='tests.log')


class SeleniumListener(AbstractEventListener):
    def on_exception(self, exception, browser):
        allure.attach(browser.get_screenshot_as_png(), name=f"error_{browser.name}" + time.strftime("_%d_%b_%H:%M:%S") +
                                                            ".png", attachment_type=allure.attachment_type.PNG)


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run tests headless")
    parser.addoption("--executor", action="store", default="127.0.0.1:8081",
                     choices=["127.0.0.1:8081", "127.0.0.1:4444"])
    parser.addoption("--bversion", action="store", default="92.0", choices=["92.0", "91.0", "90.0"])
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--browser_driver", action="store", default="chrome",
                     choices=["chrome", "opera", "firefox"])
    parser.addoption("--url_base", action="store", default="https://demo.opencart.com")
    parser.addoption("--cat_url", action="store",
                     default="https://demo.opencart.com/index.php?route=product/category&path=18")
    parser.addoption("--prod_url", action="store",
                     default="https://demo.opencart.com/index.php?route=product/product&path=18&product_id=44")
    parser.addoption("--auth_url", action="store",
                     default="https://demo.opencart.com/admin/")
    parser.addoption("--local_base_url", action="store", default="http://127.0.0.1:8081/")
    parser.addoption("--local_admin_url", action="store", default="http://127.0.0.1:8081/admin/")
    parser.addoption("--local_register_url", action="store",
                     default="http://127.0.0.1:8081/index.php?route=account/register")


@pytest.fixture(scope='session')
def url_base(request):
    return request.config.getoption("--url_base")


@pytest.fixture(scope='session')
def cat_url(request):
    return request.config.getoption("--cat_url")


@pytest.fixture(scope='session')
def prod_url(request):
    return request.config.getoption("--prod_url")


@pytest.fixture(scope='session')
def auth_url(request):
    return request.config.getoption("--auth_url")


@pytest.fixture(scope='session')
def local_base_url(request):
    return request.config.getoption("--local_base_url")


@pytest.fixture(scope='session')
def local_admin_url(request):
    return request.config.getoption("--local_admin_url")


@pytest.fixture(scope='session')
def local_register_url(request):
    return request.config.getoption("--local_register_url")


@pytest.fixture(scope='session')
def browser(request):
    _browser = request.config.getoption("--browser_driver")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    mobile = request.config.getoption("--mobile")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    logger = logging.getLogger('BrowserLoger')
    test_name = request.node.name

    logger.info(" ----> Test {} started".format(test_name))

    driver = None
    executor_url = f"http://{executor}/wd/hub"

    if _browser == "chrome":
        if executor == "127.0.0.1:8081":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif executor == "127.0.0.1:4444":
            capabilities = {
                "browserName": _browser,
                "browserVersion": version,
                "screenResolution": "1280x1024",
                "name": "Chrome tests",
                "selenoid:options": {
                    "sessionTimeout": "60s",
                    "enableVNC": vnc,
                    "enableVideo": videos,
                    "enableLog": logs
                },
            }
            driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)
    elif _browser == "opera":
        if executor == "127.0.0.1:8081":
            driver = driver = webdriver.Opera(OperaDriverManager().install())
        elif executor == "127.0.0.1:4444":
            capabilities = {
                "browserName": _browser,
                "browserVersion": version,
                "screenResolution": "1280x1024",
                "name": "Opera tests",
                "selenoid:options": {
                    "sessionTimeout": "60s",
                    "enableVNC": vnc,
                    "enableVideo": videos,
                    "enableLog": logs
                },
            }
            driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)
    elif _browser == "firefox":
        if executor == "127.0.0.1:8081":
            driver = driver = webdriver.Firefox(GeckoDriverManager().install())
        elif executor == "127.0.0.1:4444":
            capabilities = {
                "browserName": _browser,
                "browserVersion": version,
                "screenResolution": "1280x1024",
                "name": "Firefox tests",
                "selenoid:options": {
                    "sessionTimeout": "60s",
                    "enableVNC": vnc,
                    "enableVideo": videos,
                    "enableLog": logs
                },
            }
            driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)
    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()
        logger.info(" ----> Test {} finished".format(test_name))
    request.addfinalizer(final)
    return driver
