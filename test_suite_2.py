import unittest

class test_module2(unittest.TestCase):
    def test_1(self):
        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("a")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("b")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("c")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        text_elt = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual('Congratulations! You have successfully registered!', text_elt, "text not found or match")
        browser.quit()
       
    def test_2(self):
        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("a")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("b")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("c")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        text_elt = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual('Congratulations! You have successfully registered!', text_elt, "text not found or match")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
    print('all test passed')
