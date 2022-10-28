from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\Users\jide.onakoya.LAPTOP-EFVA62JM\Desktop\Dev\web Driver\geckodriver-v0.32.0-win32\geckodriver.exe', options=options)
driver.get('http://google.com/')