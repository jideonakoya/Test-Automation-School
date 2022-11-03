import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_xpath(driver):
    form = driver.find_element(By.XPATH, "//form[1]")
    print("Form:", form)
    form_by_full_xpath = driver.find_element(By.XPATH, '//*[@id="emailAddress"]')
    print("Form By Full Xpath", form_by_full_xpath)
    search_box = driver.find_element(By.XPATH, '//*[@id="jsSearchInput"]')
    print("Search Box:", search_box)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.konga.com/help/contact-us")
    locate_by_xpath(driver)


if __name__ == '__main__':
    main()
