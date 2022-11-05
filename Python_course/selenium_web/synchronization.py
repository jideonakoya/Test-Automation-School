import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def element_to_be_visible(driver):
    web_driver_wait = WebDriverWait(driver, 5)
    web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="about-konga"]/li[2]/a')))
    academy_link = driver.find_element(By.XPATH, '//*[@id="about-konga"]/li[2]/a')
    academy_link.click()


def to_be_clickable(driver):
    web_driver_wait = WebDriverWait(driver, 20)
    web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="about-konga"]/li[2]/a')))
    academy_link = driver.find_element(By.XPATH, '//*[@id="about-konga"]/li[2]/a')
    academy_link.click()


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.konga.com")
    #to_be_clickable(driver)
    element_to_be_visible(driver)


if __name__ == "__main__":
    main()

