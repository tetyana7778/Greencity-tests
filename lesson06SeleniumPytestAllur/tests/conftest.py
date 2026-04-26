import pytest

from selenium import webdriver

from data.config import Config

@pytest.fixture(scope="function")
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument(f"--lang={Config.BROWSER_LANG}")
    if Config.HEADLESS_MODE:
        options.add_argument("--headless=new")
        print("Running in headless mode")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(Config.IMPLICIT_WAIT_TIMEOUT)
    driver.maximize_window()
    driver.get(Config.BASE_UI_URL)

    # after yield code will be executed as teardown
    yield driver # тут тест виконується
    # before yield code will be executed as setup

    driver.quit() #А тут браузер закривається після тесту