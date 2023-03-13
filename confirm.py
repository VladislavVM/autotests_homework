from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = 'http://suninjuly.github.io/alert_accept.html'

try:
  browser = webdriver.Chrome()
  browser.get(link)
  time.sleep(2)
  button1 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
  confirm = browser.switch_to.alert.accept()
  task1 = browser.find_element(By.ID, 'input_value').text
  y = calc(task1)
  answer1 = browser.find_element(By.ID, 'answer').send_keys(y)
  button2 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
  time.sleep(5)
  browser.quit()
