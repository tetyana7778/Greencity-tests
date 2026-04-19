import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from base_page_les05 import BasePage
from events_page_les05 import EventsPage


class TestPO(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity"
    modal_xpath = "//app-auth-modal"
    sign_in_container_locator = (By.XPATH, "//app-auth-modal")

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)
        sleep(2)
        self.driver.delete_all_cookies()
        self.driver.execute_script("localStorage.clear();")
        self.driver.execute_script("localStorage.setItem('language', 'en');")
        self.driver.refresh()
        sleep(2)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_sign_in_modal(self):
        page = BasePage(self.driver)
        page.click_sign_in()
        sleep(3)
        modal_window = self.driver.find_element(*self.sign_in_container_locator)
        self.assertTrue(modal_window.is_displayed(), "Модальне вікно не з'явилося!")

    def test_login_with_valid_email(self):
        page = BasePage(self.driver)
        page.click_sign_in()
        sleep(3)
        page.enter_email("testtetiana@test.com")

    def test_fill_password_field(self):
        page = BasePage(self.driver)
        page.click_sign_in()
        sleep(1)
        valid_password = "Tetiana_123"
        page.enter_password(valid_password)
        entered_value = self.driver.find_element(*page.password_field_locator).get_attribute("value")
        self.assertEqual(entered_value, valid_password, "Пароль у полі не збігається!")

    def test_click_submit_button(self):
        page = BasePage(self.driver)
        page.click_sign_in()
        sleep(3)
        page.enter_email("testtetiana@test.com")
        sleep(3)
        page.enter_password("Tetiana_123")
        sleep(3)
        page.click_submit_button()
        sleep(2)
        print("Клік по кнопці 'Submit' виконано!")

    def test_join_open_event(self):
        page = BasePage(self.driver)
        page.click_events_link()
        print("Перехід на сторінку Подій виконано!")
        page.select_status_filter()
        sleep(2)
        print("Клік по кнопці 'Статус' виконано!")
        page.select_open_status()
        sleep(2)
        print("Клік по кнопці 'Відкрита' виконано!")
        wait = WebDriverWait(self.driver, 10)
        first_card = self.driver.find_element(By.XPATH, "//app-events-list-item")
        from events_card_component_les05 import EventCardComponent
        event = EventCardComponent(first_card)
        event.click_join_event()
        print("Клік по кнопці 'Приєднатися до події' виконано!")
        sleep(3)


if __name__ == "__main__":
    unittest.main()