from selenium import webdriver


def main():
    driver = webdriver.Edge(executable_path=r"C:\Users\jide.onakoya.LAPTOP-EFVA62JM\Desktop\Dev\web Driver\edgedriver_win64/msedgedriver.exe")
    driver.get("https://www.google.com")
    driver.close()


main()