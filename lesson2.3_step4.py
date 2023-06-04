from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    btnStart = browser.find_element(By.CSS_SELECTOR, ".btn")
    btnStart.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    input1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = (int)(input1.text)
    y = calc(x)
        
    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(y)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
