from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BasePage:
    # Локатори
    sign_in_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")
    sign_in_container_locator = (By.XPATH, '//div[contains(@class, "right-side")]')
    email_field_locator = (By.XPATH, "//input[@id='email']")
    password_field_locator = (By.XPATH, "//input[@id='password']")
    submit_button_locator = (By.XPATH, "//button[@class='greenStyle']")
    events_link_locator = (By.XPATH, "//header//a[contains(@class, 'url-name') and (contains(., 'Події') or contains(., 'Events'))]")
    first_card_el_locator = (By.XPATH, "//app-events-list-item")
    status_filter_locator = status_filter_locator = (By.XPATH, "//mat-label[contains(., 'Статус') or contains(., 'Status')]")
    open_status_locator = (By.XPATH, "//mat-option[contains(., 'Відкрита') or contains(., 'Open')]")
    join_event_button_locator = (By.XPATH, ".//button[contains(., 'Приєднатися') or contains(., 'Join')]")
    def __init__(self, driver):
        self.driver = driver

    def get_sign_in_button(self):
        return self.driver.find_element(*self.sign_in_button_locator)

    def click_sign_in(self):
        self.get_sign_in_button().click()

    def enter_email(self, email_address):
        email_field = self.driver.find_element(*self.email_field_locator)
        email_field.click()
        email_field.clear()
        email_field.send_keys(email_address)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password_field_locator)
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button_locator).click()

    def click_events_link(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located(self.sign_in_container_locator))
        events_link = wait.until(EC.element_to_be_clickable(self.events_link_locator))
        events_link.click()
        sleep(2)

    def select_status_filter(self):
        wait = WebDriverWait(self.driver, 10)
        status_filter = wait.until(
            EC.element_to_be_clickable(self.status_filter_locator)
        )
        status_filter.click()
        sleep(2)  # чекаємо поки список відкриється
        print("Клік по фільтру Status виконано!")

    def select_open_status(self):
        wait = WebDriverWait(self.driver, 10)
        open_status = wait.until(
            EC.element_to_be_clickable(self.open_status_locator)
        )
        open_status.click()
        print("Статус Open вибрано успішно!")
        sleep(3) 
        # Чекаємо поки backdrop повністю зникне
        wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'cdk-overlay-backdrop')]")
            )
        )

    def click_events_link(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located(self.sign_in_container_locator))
        events_link = wait.until(EC.element_to_be_clickable(self.events_link_locator))
        events_link.click()
        sleep(2)

    def get_events_link(self):
        return self.driver.find_element(*self.events_link_locator)

    def navigate_to_events(self):
        self.get_events_link().click()