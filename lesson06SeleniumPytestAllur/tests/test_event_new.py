import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.config import Config
from component.event_card_component import EventCardComponent
import allure
@allure.epic("Реєстрація та Події") # Велика категорія
@allure.feature("Фільтрація подій") # Функціонал
@allure.title("Перевірка статусу 'Open' в списку подій") # Назва конкретного тесту

def test_filter_by_status(init_driver):
# Тепер це просто функції, які отримують init_driver як аргумент
 print(f"DEBUG: Email from config is {Config.USER_EMAIL}")
    
     
@allure.feature("Введення електронної пошти")
@allure.title("Введення валідної електронної пошти")
@allure.severity(allure.severity_level.CRITICAL)
def test_sign_in_modal(init_driver):
    page = BasePage(init_driver)
    page.click_sign_in()
        # Перевірка (Assertion) залишається
    modal_window = init_driver.find_element(By.XPATH, "//app-auth-modal")
    assert modal_window.is_displayed(), "Модальне вікно не з'явилося!"

    
@allure.feature("Введення електронної пошти")
@allure.title("Введення валідної електронної пошти")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_with_valid_email(init_driver):
    page = BasePage(init_driver)
    page.click_sign_in()
        
        # Використовуємо імейл з нашого Config
    page.enter_email(Config.USER_EMAIL)
        
        # Додамо перевірку, що імейл дійсно ввівся (це хороший тон)
    entered_email = init_driver.find_element(*page.email_field_locator).get_attribute("value")
    assert entered_email == Config.USER_EMAIL, f"Очікували {Config.USER_EMAIL}, але отримали {entered_email}"
    
@allure.feature("Введення пароля")
@allure.title("Введення валідного пароля")
@allure.severity(allure.severity_level.CRITICAL)
def test_fill_password_field(init_driver):
    page = BasePage(init_driver)
    page.click_sign_in()
        
        # Використовуємо пароль з Config
    page.enter_password(Config.USER_PASSWORD)
        
        # Перевірка через звичайний assert
    entered_value = init_driver.find_element(*page.password_field_locator).get_attribute("value")
    assert entered_value == Config.USER_PASSWORD, "Пароль у полі не збігається!"
    
@allure.feature("Увійти")
@allure.title("Увійти з валідними даними")
@allure.severity(allure.severity_level.CRITICAL)
def test_click_submit_button(init_driver):
    page = BasePage(init_driver)
    page.click_sign_in()
        
        # Послідовне заповнення
    page.enter_email(Config.USER_EMAIL)
    page.enter_password(Config.USER_PASSWORD)
        
    page.click_submit_button()
    print("Клік по кнопці 'Submit' виконано успішно!")

@allure.feature("Події")
@allure.title("Приєднання до відкритої події")
@allure.severity(allure.severity_level.CRITICAL)
def test_join_open_event(init_driver):
    page = BasePage(init_driver)

    page.click_events_link()
    
    page.select_status_filter()
    page.select_open_status()
    
    # Знаходимо картку та працюємо з компонентом
    first_card = init_driver.find_element(By.XPATH, "//app-events-list-item")
    event = EventCardComponent(first_card)
    event.click_join_event()
    print("Клік по кнопці 'Приєднатися' виконано!")