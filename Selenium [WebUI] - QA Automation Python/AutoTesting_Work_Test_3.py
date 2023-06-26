"""

Auto Test Python №3:

Авторизація на сайті + Створення товару

"""

import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
    # Пошук кнопки для створення товару:
    button_add_order = driver.find_element("xpath", "/html/body/qa-root/qa-dashboard/div/div/div/div/div[1]/div[1]/button/span")

    time.sleep(5)
    # Натискання на кнопку створення товару:
    ActionChains(driver).move_to_element(button_add_order).click(button_add_order).perform()

    time.sleep(5)

    # Поиск элементов в форме и присваивание к переменным.
    input_frame_name = driver.find_element("xpath", "//*[@id=\"name\"]/div/div/input")
    input_frame_quantity = driver.find_element("xpath", "//*[@id=\"quantity\"]/div/div/input")
    input_frame_cost = driver.find_element("xpath", "//*[@id=\"cost\"]/div/div/input")
    select_frame_status = driver.find_element("xpath", "//*[@id=\"status\"]/div/qa-field/div")
    select_frame_bid = driver.find_element("xpath", "//*[@id=\"type\"]/div/qa-field/div")
    input_frame_button = driver.find_element("xpath", "//*[@id=\"mat-dialog-0\"]/qa-add-order/mat-dialog-actions/div/button")

    # Дії з формами, заповнення значень:
    input_frame_name.send_keys("Testtt 44")
    input_frame_quantity.send_keys("20")
    input_frame_cost.send_keys("45")
    # Вибір зі списку меню!
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"status\"]/div/qa-field/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"status\"]/div/qa-list/div/qa-item[1]/div/div/span"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"type\"]/div/qa-field/div"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"type\"]/div/qa-list/div/qa-item[1]/div/div/span"))).click()

    time.sleep(5)
    # Натискання на кнопку створення товару:
    ActionChains(driver).move_to_element(input_frame_button).click(input_frame_button).perform()

    time.sleep(5)

    # Завантаження сторінки Dashboard:
    driver.get("http://testsite.light-it.io/#/")

    time.sleep(5)

    product_check = driver.find_element("xpath", "//*[contains(text(), 'Testtt 44')]")
    # Отримуемо текст елементу
    proofcheckitem = product_check.text
    # Тестування:
    check.equal(proofcheckitem, "Testtt 44")

    time.sleep(5)

    if product_check is None:
        print("Елемент не знайдено!")
        time.sleep(5)
    else:
        print(str(product_check.text))
        print("Елемент знайдено!")
        time.sleep(5)

    time.sleep(3)


if __name__ == '__main__':
    test_case()