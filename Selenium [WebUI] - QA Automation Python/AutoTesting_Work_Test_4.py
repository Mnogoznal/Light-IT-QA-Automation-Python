"""

Auto Test Python №4:

Авторизація на сайті + Зміна Мови Інтерфейсу та Перевірка

"""

import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import pytest_check as check


def test_case_lang():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(executable_path='C:\chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    # Завантаження сторінки:
    driver.get("http://testsite.light-it.io/#/auth/sign-in")

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


    # Вибір зі списку меню мови
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/qa-root/qa-dashboard/qa-header/div/div[2]/div/button[1]/span/span"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"cdk-overlay-0\"]/div/div/button[2]"))).click()

    time.sleep(5)

    text_all_fr_check = driver.find_element("xpath", "/html/body/qa-root/qa-dashboard/div/div/div/div/div[1]/div[1]/h2")
    # Отримаемо результат зміни мови:
    prooftextchange = text_all_fr_check.text
    # Тестування:
    check.equal(prooftextchange, "Liste des commandes")

    time.sleep(5)

    if text_all_fr_check is None:
        print("Елемент не знайдено!")
        time.sleep(5)
    else:
        print(str(text_all_fr_check.text))
        print("Елемент знайдено!")
        time.sleep(5)

    time.sleep(3)


if __name__ == '__main__':
    test_case_lang()