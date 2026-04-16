from selenium.webdriver.common.by import By
from time import sleep

class BasePage:
    #Це "адреси" елементів на сторінці.
    sign_in_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")
    language_switcher = (By.XPATH, "//ul[@aria-label='language switcher']")
    language_en_option = (By.XPATH, ".//span[contains(text(), 'En')]")
    language_ua_option = (By.XPATH, ".//span[contains(text(), 'Uk')]")

    events_link_locator = (By.XPATH, "//header//a[contains(@class, 'url-name') and contains(., 'Події') or contains(., 'Events')]")
    
    # Вставила локатор на модальне вікно входу, щоб потім в тесті перевірити його появу після кліку на кнопку Sign in

    sign_in_container_locator = (By.XPATH, '//div[contains(@class, "right-side")]')
    email_field_locator = (By.XPATH, "//input[@id='email']")
    #Локатор для кнопки підтвердження входу після введення даних.
    #він знаходиться всередині модального вікна 
    submit_button_locator = (By.XPATH, "//button[@class='greenStyle']")
    # Локатор для вводу пароля.
    password_field_locator = (By.XPATH, "//input[@id='password']")
    #Конструктор класу, який приймає об'єкт драйвера і зберігає його для подальшого використання
    def __init__(self, driver):
        self.driver = driver

    #Метод для отримання кнопки на вхід на сторінці
    def get_sign_in_button(self):
        return self.driver.find_element(*self.sign_in_button_locator) #
    
    #Метод для кліку на кнопку входу
    def click_sign_in(self):
        sign_in_button = self.get_sign_in_button()
        sign_in_button.click()
    
    #Метод для отримання елемента перемикача мови
    def get_language_switcher(self):
        return self.driver.find_element(*self.language_switcher)
    
    #Метод для перемикання мови на сторінці
    def switch_language(self, language):
        language_switcher = self.get_language_switcher()
        language_switcher.click()
        if language.lower() == "en":
            language_option = self.driver.find_element(*self.language_en_option)
        elif language.lower() == "ua":
            language_option = self.driver.find_element(*self.language_ua_option)
        else:
            raise ValueError("Unsupported language: {}".format(language))
        language_option.click()
        sleep(1)
    #Метод заповнення поля електроннної пошти в модальному вікнівходу 

    def enter_email(self, email_address):
        # 1. Знаходимо поле
        email_field = self.driver.find_element(*self.email_field_locator)
        # 2. Клікаємо на нього (щоб активувати курсор)
        email_field.click()
        # 3. Очищаємо поле (про всяк випадок)
        email_field.clear()
        # 4. Вводимо сам імейл
        email_field.send_keys(email_address)
#Метод заповнення пароля в модальному вікні входу
    def enter_password(self, password):
        # 1. Знаходимо поле пароля
        password_field = self.driver.find_element(*self.password_field_locator)
        
        # 2. Активуємо поле кліком
        password_field.click()
        
        # 3. Очищаємо, якщо там щось було
        password_field.clear()
        
        # 4. Вводимо пароль
        password_field.send_keys(password)   
    
    #Метод для кліку на кнопку Увійти 
    def click_submit_button(self):
        submit_button = self.driver.find_element(*self.submit_button_locator)
        submit_button.click()
    #Метод для отримання посилання на сторінку з новинами
    def get_events_link(self):
        return self.driver.find_element(*self.events_link_locator)
    
    #Метод для переходу до сторінки з подіями
    def navigate_to_events(self):
        events_link = self.get_events_link()
        events_link.click()
