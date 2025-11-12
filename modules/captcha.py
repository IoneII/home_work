import time
import pyautogui
from selenium.webdriver.common.by import By
from modules.config import driver, url, x, y


def captcha():
    driver.maximize_window()
    driver.get(url=url)
    time.sleep(5)
    pyautogui.click(x, y)
    print(f"✅ Клик выполнен в точке ({x}, {y})")
    time.sleep(1)
    elements = driver.find_elements(By.CSS_SELECTOR, '.mondrian__block')
    for element in elements:
        if 'халате' in str(element.text):
            print("халат найден, пытаюсь кликнуть")
            element.click()
            time.sleep(0.2)
    next_click = driver.find_element(By.XPATH, '//*[@id="recaptcha-app"]/div/div/div/button').click()  # Готово
    time.sleep(0.2)
