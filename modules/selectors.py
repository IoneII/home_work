import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def select_region(driver, target_region):
    """Выбирает регион Краснодарский край"""
    # Ждём появления поля региона
    region_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[contains(@placeholder, 'субъект РФ')]"))
    )
    # Кликаем по полю, чтобы раскрыть список
    driver.execute_script("arguments[0].scrollIntoView(true);", region_field)
    driver.execute_script("arguments[0].click();", region_field)
    time.sleep(0.5)  # ждём появления списка

    # Получаем все элементы списка через JS
    elements = driver.execute_script("return document.querySelectorAll('ul.list li');")

    # Выбираем нужный регион
    for el in elements:
        text = driver.execute_script("return arguments[0].textContent;", el).strip()
        if target_region in text:
            driver.execute_script("arguments[0].click();", el)
            print(f"✅ Выбран регион: {text}")
            break


def select_institution(driver, target_institution):
    """Выбирает учреждение Городская больница города Анапы"""
    # Ждём появления поля МО (оно появляется после выбора региона)
    mo_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[contains(@placeholder, 'МО')]"))
    )

    # Кликаем по полю МО, чтобы раскрыть список
    driver.execute_script("arguments[0].scrollIntoView(true);", mo_field)
    driver.execute_script("arguments[0].click();", mo_field)
    time.sleep(1)  # ждём появления списка

    # Получаем все элементы списка через JS
    elements = driver.execute_script("return document.querySelectorAll('ul.list li');")

    # Выбираем нужное учреждение
    for el in elements:
        text = driver.execute_script("return arguments[0].textContent;", el).strip()
        if target_institution in text:
            driver.execute_script("arguments[0].click();", el)
            print(f"✅ Выбрано учреждение: {text}")
            time.sleep(0.5)
            break