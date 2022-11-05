import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.konga.com")
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="about-konga"]/li[2]/a').click()
    time.sleep(4)
    driver.back()
    time.sleep(9)
    driver.forward()
    time.sleep(4)


if __name__ == "__main__":
    main()