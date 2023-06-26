"""

Auto Test Python №2:

Створення профілю нового користувача + Авторизація на сайті

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
    driver.get("http://testsite.light-it.io/#/auth/sign-up")

    time.sleep(5)

    # Пошук елементів на сторінці сайту та присвоєння змінним (Логін, Емейл, Пароль, Кнопка):
    input_username = driver.find_element("id", "mat-input-0")
    input_email = driver.find_element("id", "mat-input-1")
    input_password = driver.find_element("id", "mat-input-2")
    input_repeat_password = driver.find_element("id", "mat-input-3")
    login_button = driver.find_element("xpath", "/html/body/qa-root/qa-sign-up/div/div/div[2]/div/div[1]/form/button/span")

    # Дії з формами, заповнення значень:
    form_username = "Oleksanders23"
    form_email = "testznu23@gmail.com"
    form_password = "!123456qwerty123!"

    input_username.send_keys(form_username)
    input_email.send_keys(form_email)
    input_password.send_keys(form_password)
    input_repeat_password.send_keys(form_password)

    time.sleep(5)

    # Натискання на кнопку авторизації:
    ActionChains(driver).move_to_element(login_button).click(login_button).perform()

    time.sleep(15)

    # Завантаження сторінки авторизації:
    driver.get("http://testsite.light-it.io/#/auth/sign-in")

    time.sleep(5)

    # Пошук елементів на сторінці сайту та присвоєння змінним (Логін, Емейл, Пароль, Кнопка):
    input_username1 = driver.find_element("id", "mat-input-0")
    input_email1 = driver.find_element("id", "mat-input-1")
    input_password1 = driver.find_element("id", "mat-input-2")
    login_button1 = driver.find_element("xpath", "/html/body/qa-root/qa-sign-in/div/div/div[2]/div/form/button/span")

    # Дії з формами, заповнення значень:
    input_username1.send_keys(form_username)
    input_email1.send_keys(form_email)
    input_password1.send_keys(form_password)

    time.sleep(5)
    # Натискання на кнопку авторизації:
    ActionChains(driver).move_to_element(login_button1).click(login_button1).perform()

    time.sleep(5)

    text_all_check = driver.find_element("xpath", "/html/body/qa-root/qa-dashboard/div/div/div/div/div[1]/div[1]/h2")

    # Отримаемо значення елементу:
    proofcheck = text_all_check.text

    # Тестування:
    check.equal(proofcheck, "All Orders List")

    if text_all_check is None:
        print("Елемент не знайдено!")
        time.sleep(5)
    else:
        print("Елемент знайдено!")
        time.sleep(5)

    time.sleep(3)


if __name__ == '__main__':
    test_case()