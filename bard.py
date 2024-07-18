import os
import time
import pyperclip
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl


options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 100)
options.add_argument("--headless")
time.sleep(2)
driver.get("https://bard.google.com/")
time.sleep(5)
# Locate and click the Sign In button by its class name
sign_in_button = driver.find_element(By.XPATH,"//*[@id='gb']/div/div[1]/a")
sign_in_button.click()
time.sleep(5)
    # Close the browser when1 done
    # # Input email
email=wait.until(EC.visibility_of_element_located((By.NAME, 'identifier')))
email.send_keys("zingtech10@gmail.com")
time.sleep(10)
    # Click the "Next" button
    
wait = WebDriverWait(driver, 5)
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/ancestor::button")))
next_button.click()
time.sleep(5)
# Input password
password=wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@class="whsOnd zHQkBf"]')))
password.send_keys("zingtech@123")
    
time.sleep(2)
    # Click the "Next" button to log in
wait = WebDriverWait(driver, 5)
next_button_email= wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/ancestor::button")))
next_button_email.click()
time.sleep(5)

