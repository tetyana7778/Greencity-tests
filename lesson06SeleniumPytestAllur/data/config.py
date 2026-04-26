# import os
# from pathlib import Path
# from dotenv import load_dotenv

# # 1. Шлях до самого файлу config.py
# # 2. .parent — це папка 'data'
# # 3. .parent — це папка 'lesson06SeleniumPytestAllur'
# # 4. .parent — це корінь проєкту 'CrashCourseQA_Automation'
# BASE_DIR = Path(__file__).resolve().parent.parent.parent 
# dotenv_path = BASE_DIR / ".env"
# load_dotenv(dotenv_path=dotenv_path)
# class Config:
#     # Тепер os.getenv бере значення ЗА НАЗВОЮ КЛЮЧА з твого .env
#     USER_EMAIL = os.getenv("USER_EMAIL")
#     USER_PASSWORD = os.getenv("USER_PASSWORD")
#     USER_NAME = os.getenv("USER_NAME")
    
#     # Налаштування браузера
#     BROWSER_LANG = os.getenv("BROWSER_LANG", "en")
#     BASE_UI_URL = "https://www.greencity.cx.ua/#/greenCity"
#     IMPLICIT_WAIT_TIMEOUT = 10
    
#     # Перетворюємо рядок "False" з .env у справжній булевий тип (True/False)
#     HEADLESS_MODE = os.getenv("HEADLESS_MODE", "False").lower() in ("true", "1", "t")
import os
from pathlib import Path
from dotenv import load_dotenv

# Отримуємо шлях до папки, де лежить цей файл (тобто до папки data)
CURRENT_DIR = Path(__file__).resolve().parent
dotenv_path = CURRENT_DIR / ".env"

# Додаємо перевірку для впевненості
print(f"\n--- ПЕРЕВІРКА ЛОКАЦІЇ .ENV ---")
print(f"Шукаю файл тут: {dotenv_path}")
print(f"Файл знайдено? {'ТАК' if dotenv_path.exists() else 'НІ'}")

load_dotenv(dotenv_path=dotenv_path)

class Config:
    USER_EMAIL = os.getenv("USER_EMAIL")
    USER_PASSWORD = os.getenv("USER_PASSWORD")
    USER_NAME = os.getenv("USER_NAME")
    
    # Інші налаштування
    BASE_UI_URL = "https://www.greencity.cx.ua/#/greenCity"
    IMPLICIT_WAIT_TIMEOUT = 10
    BROWSER_LANG = os.getenv("BROWSER_LANG", "uk-UA")
    HEADLESS_MODE = os.getenv("HEADLESS_MODE", "False").lower() in ("true", "1", "t")

# Перевірка, чи зчиталися дані
print(f"DEBUG: Email зчитано як -> {Config.USER_EMAIL}")
print(f"------------------------------\n")