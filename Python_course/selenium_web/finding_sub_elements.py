import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.gennesaretresources.com/contact.php");
    forms = driver.find_element(By.TAG_NAME, "form")
    print("Found:", len(forms))


if __name__ == "__main__":
    main()

