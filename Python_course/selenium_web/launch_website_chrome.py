from selenium import webdriver


def main():
    driver = webdriver.Chrome(executable_path="C:/Users/jide.onakoya.LAPTOP-EFVA62JM/Desktop/Dev/web Driver/chromedriver_win32/chromedriver.exe")
    driver.get("https://www.google.com")
    driver.close()


main()

