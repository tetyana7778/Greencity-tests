from selenium.webdriver.remote.webelement import WebElement


class BaseComponent:
    """
    Базовий клас для компонентів сторінки.
    Компонент — це частина сторінки, наприклад картка події.
    Відрізняється від BasePage тим, що працює НЕ з цілою сторінкою,
    а з конкретним елементом (node) всередині сторінки.
    """

    def __init__(self, node: WebElement):
        # node — це конкретний WebElement, всередині якого шукаємо дочірні елементи
        # Наприклад: картка події app-events-list-item
        self.node = node

    def find_element(self, by, value):
        """
        Шукає елемент ВСЕРЕДИНІ компонента (node),
        а не на всій сторінці як у BasePage!
        """
        return self.node.find_element(by, value)

    def find_elements(self, by, value):
        """
        Шукає список елементів всередині компонента.
        """
        return self.node.find_elements(by, value)

    def get_text(self, by, value):
        """
        Повертає текст елемента всередині компонента.
        """
        return self.find_element(by, value).text

    def is_displayed(self, by, value):
        """
        Перевіряє чи видимий елемент всередині компонента.
        Повертає True або False.
        """
        try:
            return self.find_element(by, value).is_displayed()
        except:
            return False