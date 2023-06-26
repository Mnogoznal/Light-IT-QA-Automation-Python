"""

Auto Test Python №1:

Авторизація на сайті + Тестування

"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import pytest_check as check


def test_case():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(executable_path='C:\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    # Завантаження сторінки:
    driver.get("http://testsite.light-it.io/#/auth/sign-in")

    time.sleep(5)

    # Пошук елементів на сторінці сайту та присвоєння змінним (Логін, Емейл, Пароль, Кнопка):
    input_username = driver.find_element("id", "mat-input-0")
    input_email = driver.find_element("id", "mat-input-1")
    input_password = driver.find_element("id", "mat-input-2")
    login_button = driver.find_element("xpath", "/html/body/qa-root/qa-sign-in/div/div/div[2]/div/form/button/span")

    # Дії з формами, заповнення значень:
    input_username.send_keys("Oleksanders")
    input_email.send_keys("testznu@gmail.com")
    input_password.send_keys("123456qwerty123!")

    time.sleep(5)

    # Натискання на кнопку авторизації:
    ActionChains(driver).move_to_element(login_button).click(login_button).perform()

    time.sleep(5)

    # Пошук елементу на сторінці завдяки xpath:
    text_all_check = driver.find_element("xpath", "/html/body/qa-root/qa-dashboard/div/div/div/div/div[1]/div[1]/h2")

    print(text_all_check.text)

    # Отримаемо значення елементу
    proofcheck = text_all_check.text

    # Тестування
    check.equal(proofcheck, "All Orders List")

    if text_all_check is None:
        print("Елемент не знайдено!")
        time.sleep(5)
    else:
        print("Елемент знайдено!")
        time.sleep(5)

    # Закриття ВебДрайвера
    driver.close()

# Головна функція:
if __name__ == '__main__':
    test_case()