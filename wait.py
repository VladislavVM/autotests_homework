from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    button1 = browser.find_element(By.ID, 'book')
    wait1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button1.click()
    browser.execute_script("window.scrollBy(0, 400);")
    task = browser.find_element(By.ID, 'input_value').text
    
    y = calc(task)
    answer = browser.find_element(By.ID, 'answer').send_keys(y)
    button2 = browser.find_element(By.ID, 'solve').click()
finally:
    time.sleep(5)
    browser.quit()
