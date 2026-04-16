from __future__ import annotations # щоб не було помилок із типами
#Ця команда імпортує весь модуль під назвою re-це скорочення від Regular Expressions
import re
from turtle import title
#Імпортуємо клас BasePage  з модуля .base_page
from base_page_les05 import BasePage
from selenium.webdriver.common.by import By
from event_card_component_les05 import EventCardComponent

class EventsPage(BasePage):
#Це адреси елементів на сторінці
    main_header_locator = (By.XPATH, "//p[contains(@class, 'main-header')]")
    items_fount_locator = (By.XPATH, "//div[@class='active-filter-container']/p")
    cards_locator = (By.XPATH, "//mat-card")
    more_in_card_locator = (By.XPATH, ".//button[normalize-space()='More' or normalize-space()='Більше']")
    #додаю адресу кнопки ідля реєтрації в картці події.Вона знаходиться всередині картки, тому починаю з крапки, 
    #щоб шукати її відносно картки події, а не відносно всієї сторінки
    join_event_in_card_locator = (By.XPATH, ".//button[normalize-space()='Join event' or normalize-space()='Приєднатися до події']")
    def __init__(self, driver):
        super().__init__(driver)
# Meтод для отримання головного заголовку на сторінці 
    def get_main_header(self):
        return self.driver.find_element(*self.main_header_locator)
    #Метод для отримання елемента, який показує кількість знайдених подій
    def get_items_found(self):
        return self.driver.find_element(*self.items_fount_locator)
    #Метод для отримання кількості знайдених подій, який використовує регулярні вирази для витягання числа 
    #з тексту
    def get_items_count(self):
        items_found = self.get_items_found()
        text = items_found.text
    # Викорстовуємо регулярний вираз для пошуку першого числа в текті
        match = re.search(r'\d+', text)
        if match:
            result = int(match.group())
            return result
    # Метод для отримання всіх карток подій на сторінці, який повертає список об'єктів типу EventCardComponent
    def get_cards(self)->list[EventCardComponent]:
        cards_web_elements = self.driver.find_elements(*self.cards_locator)
        cards = []
        for card_element in cards_web_elements:
            card = EventCardComponent(card_element)
            cards.append(card)

        return cards