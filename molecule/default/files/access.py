import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX.copy()
)
driver.get('http://goaccess/')
time.sleep(3)

driver.get('http://goaccess/')
time.sleep(3)

driver.get('http://goaccess/')
time.sleep(3)

driver.quit()
