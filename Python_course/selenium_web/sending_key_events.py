import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_key_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    send_key_to_element(driver.find_element(By.NAME, "firstname"), "Jide")
    send_key_to_element(driver.find_element(By.NAME, "lastname"), "O")
    send_key_to_element(driver.find_element(By.NAME, "email"), "lethridge@arxxwalls.com")
    send_key_to_element(driver.find_element(By.NAME, "phone"), Keys.CONTROL, "v")
    time.sleep(4)


if __name__ == '__main__':
    main()
