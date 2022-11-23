# Using the chrome browser navigate to https://facebook.com/ fill in the email/phone and password text box
# then click on the login button.

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
    driver.get("https://www.facebook.com/")
    send_key_to_element(driver.find_element(By.NAME, "email"), "merrylink@candassociates.com")
    send_key_to_element(driver.find_element(By.NAME, "pass"), "P@ssword")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

    time.sleep(7)


if __name__ == '__main__':
    main()
