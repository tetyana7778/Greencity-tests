import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from pages.base_page import BasePage
from pages.events_page import EventsPage
from pages.eco_news_page import EcoNewsPage


class TestPO(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity"
    modal_xpath = "//app-auth-modal" #Знайди на сторінці елемент, який називається app-auth-modal". 
    #Це вікно авторизації (входу)
    
    
    def setUp(self):

        oprions = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=oprions)
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)

    def tearDown(self): #Це назва методу, яку Python розпізнає як: "Виконай мене, коли тест закінчиться"
        if self.driver: #Це перевірка на безпеку. Ми питаємо: "А чи існує взагалі наш браузер (driver)? 
            #Якщо він існує, то виконай команду закриття браузера
            self.driver.quit() #повністю завершує процес браузера і звільняє пам'ять твого комп'ютера.

    def test_switch_language(self):
        page = BasePage(self.driver) #Створення об'єкта сторінки, буду працювати з об'єктом BasePage, 
        #використовуючи браузер self.driver
        page.switch_language("ua") #Викликається  метод, який натискає на перемикач мов і обирає "Uk".
        event_link = page.get_events_link() #Ми знаходимо елемент посилання на події.
        self.assertTrue(event_link.is_displayed(), "Events link is not displayed") #Ми перевіряємо, 
        #чи видимий цей лінк на екрані. Якщо елемент захований — тест впаде.
        self.assertIn("Події", event_link.text, "Events link text is incorrect")#Ми перевіряємо, чи 
        #містить текст посилання слово "Події". Це доводить, що перемикач на "UA" спрацював.
        page.switch_language("en")
        event_link = page.get_events_link()
        self.assertTrue(event_link.is_displayed(), "Events link is not displayed")
        self.assertIn("Events", event_link.text, "Events link text is incorrect")

        page.navigate_to_events() #Ми кажемо базовій сторінці: «Натисни на посилання Події».
        sleep(2)
        event_page = EventsPage(self.driver) #Оскільки ми перейшли на нову сторінку, нам потрібен 
        # новий «інструмент» для роботи саме з нею. EventsPage — це ще один клас (схожий на BasePage), 
        # який знає, де на цій сторінці лежать картки подій.
        self.assertEqual(event_page.get_items_count(), 31, "Events count is incorrect")#питаєш у 
        #сторінки: «Скільки всього подій ти бачиш у заголовку чи лічильнику? якщо не 31-тест впаде
        cards = event_page.get_cards() #перевіряєш, скільки фізичних «прямокутників» (карток) 
        #відображається прямо зараз на сторінці. Очікується, що їх має бути 6.
        self.assertEqual(len(cards), 6, "Number of event cards is incorrect")
        cards_names = [card.get_name() for card in cards] #Пробіжися по кожній картці зі списку cards.
        # У кожної картки візьми її назву (get_name) і поклади цю назву в новий список cards_names
        expected_names = [
            'Eco Meetup 2026',
            'Community Cleanup Saturday',
            'Some Event',
            'Глобальний еко-вебінар 2026',
            'Еко Взаємодія',
            'Test 02'
        ] #Порівняння зі списком очікувань.Якщо хоча б одна літера в назві події відрізняється 
        #або події стоять у невірному порядку — тест не пройде.
        self.assertEqual(cards_names, expected_names, "Event card names are incorrect")
        cards[0].click_more()

        sleep(2)
        current_url = self.driver.current_url
        self.assertIn("/events/46", current_url, "Did not navigate to event details page")

        event_page.navigate_to_eco_news()
        sleep(2)

    


if __name__ == "__main__":
    unittest.main()