import time
import random
from selenium.webdriver.common.by import By
from modules.config import driver

def voting():
    xml_path = '/html/body/div[1]/div/div[2]/main/div[2]/div/div[2]/div'
    question_4 = {
        'по телефону мед организации': f'{xml_path}[4]/div[2]/div[2]/div[1]/div/div/label/p',
        'по телефону кол-центра': f"{xml_path}[4]/div[2]/div[2]/div[2]/div/div/label/p",
        "при обращении в регистратуру": f"{xml_path}[4]/div[2]/div[2]/div[3]/div/div/label/p",
        "лечашим врачом на приеме при посещении": f"{xml_path}[4]/div[2]/div[2]/div[4]/div/div/label/p"}
    random_values = random.choice(list(question_4.values()))

    xml_path_dict = {1: f'{xml_path}[1]/div[2]/div[2]/div[4]/div/div',
                     2: f'{xml_path}[1]/div[2]/div[2]/div[6]/button',
                     3: f'{xml_path}[2]/div[2]/div[2]/div[6]/div/div/label/p',
                     4: f'{xml_path}[2]/div[2]/div[2]/div[7]/button[2]',
                     5: f'{xml_path}[3]/div[2]/div[2]/div[1]/div/label[1]',
                     6: f'{xml_path}[3]/div[2]/div[2]/div[2]/button[2]',
                     8: f'{xml_path}[4]/div[2]/div[2]/div[6]/button[2]',
                     9: f'{xml_path}[5]/div[2]/div[2]/div[1]/div/label[1]',
                     10: f'{xml_path}[5]/div[2]/div[2]/div[2]/button[2]',
                     11: f'{xml_path}[6]/div[2]/div[2]/div[1]/div/label[1]',
                     12: f'{xml_path}[6]/div[2]/div[2]/div[2]/button[2]',
                     13: f'{xml_path}[7]/div[2]/div[2]/div[1]/div/label[1]',
                     14: f'{xml_path}[7]/div[2]/div[2]/div[2]/button[2]',
                     15: f'{xml_path}[8]/div[2]/div[2]/div[1]/div/label[1]',
                     16: f'{xml_path}[8]/div[2]/div[2]/div[2]/button[2]',
                     17: f'{xml_path}[9]/div[2]/div[2]/div[1]/div/label[1]',
                     18: f'{xml_path}[9]/div[2]/div[2]/div[2]/button[2]',
                     19: f'{xml_path}[10]/div[2]/div[2]/div[1]/div/label[2]',
                     # 10 информация на сайте мед организации(нет)
                     20: f'{xml_path}[10]/div[2]/div[2]/div[2]/button[2]',
                     21: f'{xml_path}[11]/div[2]/div[2]/div[1]/div/label[1]',
                     22: f'{xml_path}[11]/div[2]/div[2]/div[2]/button[2]',
                     23: f'{xml_path}[12]/div[2]/div[2]/div[1]/div/label[2]',  # 12 про инвалидность(нет)
                     24: f'{xml_path}[12]/div[2]/div[2]/div[2]/button[2]',
                     25: f'{xml_path}[13]/div[2]/div[2]/div[1]/div/label[1]',  # 13 вопрос про доп исследования(да)
                     26: f'{xml_path}[13]/div[2]/div[2]/div[2]/button[2]',
                     27: f'{xml_path}[14]/div[2]/div[2]/div[6]/div/div/label/p',
                     28: f'{xml_path}[14]/div[2]/div[2]/div[7]/button[2]',
                     29: f'{xml_path}[15]/div[2]/div[2]/div[1]/div/label[1]',
                     30: f'{xml_path}[15]/div[2]/div[2]/div[2]/button[2]',
                     31: f'{xml_path}[16]/div[2]/div[2]/div[1]/div/label[1]',
                     32: f'{xml_path}[16]/div[2]/div[2]/div[2]/button[2]',
                     33: f'{xml_path}[17]/div[2]/div[2]/div[1]/div/label[1]',
                     34: f'{xml_path}[17]/div[2]/div[2]/div[2]/button[2]',
                     35: f'{xml_path}[18]/div[2]/div[2]/div[1]/div/label[1]',
                     36: f'{xml_path}[18]/div[2]/div[2]/div[2]/button[2]',
                     37: f'{xml_path}[19]/div[2]/div[2]/div[1]/div/label[2]',  # 19 вопрос про электронные сервисы(нет)
                     38: f'{xml_path}[19]/div[2]/div[2]/div[2]/button[2]'
                     }

    for i in range(1, 39):  # цикл перебирающий ответы до последней страницы
        if i != 7:
            next_click = driver.find_element(By.XPATH, xml_path_dict.get(i)).click()

        else:
            next_click = driver.find_element(By.XPATH, random_values).click()

    next_click = driver.find_element(By.CSS_SELECTOR,
                                     'div.box:nth-child(20) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)').click()
    time.sleep(2)
    next_click = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div[2]/main/div[3]/div/div[2]/div[2]/div/button').click()  # копирование кода анкеты
    next_click = driver.find_element(By.CSS_SELECTOR, 'button.btn:nth-child(4)').click()
    time.sleep(2)