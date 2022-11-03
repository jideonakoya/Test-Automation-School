import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_css_selector(driver):
    explore_courses = driver.find_element(By. CSS_SELECTOR, '#__next > main > section.relative.bg-primary.dark\:bg-\[\#013069\] > div > div > div:nth-child(1) > div > button')
    print("Explore courses button by css selector", explore_courses)


def locate_by_xpath(driver):
    subscribe_text = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[11]/div/div/div[1]/h2')
    print("Subscribe to receive updates:", subscribe_text)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    locate_by_css_selector(driver)
    locate_by_xpath(driver)


if __name__ == "__main__":
    main()



