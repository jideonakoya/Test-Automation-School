import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testifyltd.com/contact")
    form = driver.find_element(By.TAG_NAME, "form")
    print("Form States:", form.is_enabled(), form.is_displayed())
    submit_button = form.find_element(By.TAG_NAME, 'button')
    time.sleep(2)
    print("Submit button states", submit_button.is_enabled(), submit_button.is_displayed())
    time.sleep(2)


if __name__ == "__main__":
    main()