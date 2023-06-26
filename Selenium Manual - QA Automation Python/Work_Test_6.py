"""

Auto Test Python №6:

Авторизація на сайті + Видалення Товару та Перевірка

"""

import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

class Test():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        service = Service(executable_path='C:\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def test_case(self):
        # Завантаження сторінки:
        self.driver.get("http://testsite.light-it.io/#/auth/sign-in")

        time.sleep(5)

        # Пошук елементів на сторінці сайту та присвоєння змінним (Логін, Емейл, Пароль, Кнопка):
        input_username = self.driver.find_element("id", "mat-input-0")
        input_email = self.driver.find_element("id", "mat-input-1")
        input_password = self.driver.find_element("id", "mat-input-2")
        login_button = self.driver.find_element("xpath", "/html/body/qa-root/qa-sign-in/div/div/div[2]/div/form/button/span")

        # Дії з формами, заповнення значень:
        input_username.send_keys("Oleksanders")
        input_email.send_keys("testznu@gmail.com")
        input_password.send_keys("123456qwerty123!")

        time.sleep(5)
        # Натискання на кнопку авторизації:
        ActionChains(self.driver).move_to_element(login_button).click(login_button).perform()

        time.sleep(5)
        # Пошук елементу на сторінці сайту
        text_all_check = self.driver.find_element("xpath", "/html/body/qa-root/qa-dashboard/div/div/div/div/div[1]/div[1]/h2")

        if text_all_check is None:
            print("Елемент не знайдено!")
            time.sleep(5)
        else:
            print("Елемент знайдено!")
            time.sleep(5)


        # Вибір зі списку меню!
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/qa-root/qa-dashboard/div/div/div/div/div[1]/div[2]/qa-orders-bay/div/mat-card[4]/mat-card-actions/div/button[1]/span"))).click()

        time.sleep(5)


if __name__ == '__main__':
    a = Test()
    a.test_case()