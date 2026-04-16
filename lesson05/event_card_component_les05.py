from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from base_component_les05 import BaseComponent


class EventCardComponent(BaseComponent):
    more_button_locator = (By.XPATH, "./app-events-list-item/div/div[3]/div[2]/button[1]")
    name_locator = (By.XPATH, ".//p[contains(@class, 'event-name')]")

    def click_more(self):
        more_button = self.find_element(*self.more_button_locator)
        more_button.click()
    def get_name(self):
        name_element = self.find_element(*self.name_locator)
        return name_element.text