import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_link_text(driver):
    sell_link = driver.find_element(By.LINK_TEXT, "Sell on Konga")
    print("Sell Link", sell_link)


def locate_by_partial_link_text(driver):
    sell_link = driver.find_element(By.PARTIAL_LINK_TEXT, "ell on Kon")
    print("Sell Link|Partial:", sell_link)
    sell_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "ell on Kon")
    print("sell links:", len(sell_links))
    for sell_link in sell_links:
        print("A Sell link:", sell_link)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://konga.com")
    # locate_by_link_text(driver)
    locate_by_partial_link_text(driver)


if __name__ == '__main__':
    main()
