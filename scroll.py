from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
try:
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer').send_keys(y)
    time.sleep(1)
    browser.execute_script("window.scrollBy(0, 100);")
    time.sleep(1)

    check1 = browser.find_element(By.ID, 'robotCheckbox').click()

    radio1 = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio1)
    radio1.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(5)
finally:
   browser.quit()
