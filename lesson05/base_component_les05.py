from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from time import sleep


class BaseComponent:

    def __init__(self, root:WebElement):
        self.node = root
        self.driver = root.parent
    def find_element(self, by=By.XPATH, value=None):
        return self.node.find_element(by, value)