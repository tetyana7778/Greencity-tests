from selenium.webdriver.common.by import By
from base_component_les05 import BaseComponent


class EventCardComponent(BaseComponent):
    more_button_locator = (By.XPATH, ".//button[1]")
    name_locator = (By.XPATH, ".//p[contains(@class, 'event-name')]")
    join_event_button_locator = (By.XPATH, ".//button[contains(@class, 'event-button')]")

    def click_more(self):
        more_button = self.find_element(*self.more_button_locator)
        more_button.click()

    def get_name(self):
        name_element = self.find_element(*self.name_locator)
        return name_element.text

    # def click_join_event(self):
    #     join_event_button = self.find_element(*self.join_event_button_locator)
    #     join_event_button.click()

    def click_join_event(self):
        join_button = self.find_element(*self.join_event_button_locator)
    #  JavaScript клік — ігнорує backdrop!
        self.node.parent.execute_script("arguments[0].click();", join_button)
        print("Клік по Join виконано!")