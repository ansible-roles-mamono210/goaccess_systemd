import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)
driver.get('http://goaccess/report.html')

w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")
driver.set_window_rect(width=w, height=h)

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./screenshot.png")

driver.save_screenshot(filename)

driver.quit()