from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'fileadd.txt')           # добавляем к этому пути имя файла 


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)
    name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys("a")
    lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys("A")
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('d')

    addfile = browser.find_element(By.ID, 'file').send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(4)
    browser.quit()
