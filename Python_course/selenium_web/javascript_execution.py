import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.konga.com")
    #driver.execute_script("alert('Hello World');")
    driver.execute_script("""
        const forms = document.getElementsByTagName('form');
        for (const form of forms) {
            form.style.backgroundColor = 'red';
            } 
    """)
    time.sleep(5)


if __name__ == '__main__':
    main()
