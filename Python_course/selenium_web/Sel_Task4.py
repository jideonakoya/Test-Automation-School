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
    driver.get("https://www.facebook.com")
    form = driver.find_element(By.TAG_NAME, "form")
    send_key_to_element(driver.find_element(By.NAME, "email"), "lethridge@arxxwalls.com")
    send_key_to_element(driver.find_element(By.NAME, "pass"), "Ilikechocol@tes")
    form.find_element(By. TAG_NAME, "button").click()
    time.sleep(10)


if __name__ == '__main__':
    main()
