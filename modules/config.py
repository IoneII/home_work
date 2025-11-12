from selenium import webdriver


url = ('https://anketa.minzdrav.gov.ru/ambulator/0')
driver = webdriver.Firefox()
x,y = 612, 480  #Координаты чекбокса "я не робот"
REGION_NAME = "Краснодарский край"
INSTITUTION_NAME = "Городская больница города Анапы"

