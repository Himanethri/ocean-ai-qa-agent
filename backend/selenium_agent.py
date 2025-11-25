def generate_selenium_script(test_case, html_content):
    script = f"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/ksris/OneDrive/Documents/Ocean AI Assignment/html/checkout.html")

time.sleep(2)

# Example interaction based on test case
discount = driver.find_element(By.ID, "discount_code")
discount.send_keys("SAVE15")

driver.find_element(By.ID, "pay_now").click()

time.sleep(3)
driver.quit()
"""
    return script
