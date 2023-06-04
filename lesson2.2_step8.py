from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    input0 = browser.find_element(By.CSS_SELECTOR, ".form-control:nth-child(2)")
    input0.send_keys("Александр")
    
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control:nth-child(4)")
    input1.send_keys("Овечкин")
    
    input2 = browser.find_element(By.CSS_SELECTOR, ".form-control:nth-child(6)")
    input2.send_keys("ovechkin_alex_1996@mail.ru")
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    inputFile = browser.find_element(By.CSS_SELECTOR, "#file")
    inputFile.send_keys(file_path)
    
    
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
