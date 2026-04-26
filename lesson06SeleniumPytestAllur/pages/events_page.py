from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page_les05 import BasePage
from time import sleep
import allure

class EventsPage(BasePage):
    """Сторінка подій."""

    URL = "https://www.greencity.cx.ua/#/greenCity/events"

    # Локатори
    first_card_el_locator = (By.XPATH, "//app-events-list-item")
    status_filter_locator = (By.XPATH, "//mat-label[@class='filter']")
    open_status_locator = (By.XPATH, "//mat-option[contains(., 'Відкрита') or contains(., 'Open')]")
    @allure.step("Ініціалізація сторінки подій")    
    def __init__(self, driver):
        super().__init__(driver)
    @allure.step("Відкрити сторінку подій") 
    def open_events_page(self):
        self.driver.get(self.URL)
        sleep(2)
    @allure.step("Вибрати першу подію зі статусом 'Open'")
    def get_first_card(self):
        return self.driver.find_element(*self.first_card_el_locator)