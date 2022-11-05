import time
from Sel_Task5_TAS import TestAutomationSimplified
from Sel_Task5_STST import SwitchToSoftwareTesting
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    test_automation_school = TestAutomationSimplified(driver)
    switch_soft_testing = SwitchToSoftwareTesting(driver)
    print(test_automation_school.title)
    print(switch_soft_testing.title)


if __name__ == '__main__':
    main()
