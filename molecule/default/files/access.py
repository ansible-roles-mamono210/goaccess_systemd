import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

driver.get('http://goaccess/')
time.sleep(3)

driver.get('http://goaccess/')
time.sleep(3)

driver.get('http://goaccess/')
time.sleep(3)

driver.quit()
