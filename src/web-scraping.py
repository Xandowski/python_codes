from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

PATH = "C:/Program Files (x86)/msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("")

try:
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "identifier"))
    )
    search.send_keys("")
    search.send_keys(Keys.RETURN)
    time.sleep(5)
except SystemExit:
    driver.quit()
    raise

driver.quit()
