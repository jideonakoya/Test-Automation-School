from selenium.webdriver.common.by import By


class TestAutomationSimplified:

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
        self.title = driver.find_element(By.CSS_SELECTOR, '#__next > main > section.relative.bg-primary.dark\:bg-\[\#013069\].automation-simplified-top-section > div > div > div.w-full.lg\:w-6\/12.pt-6 > h1')
