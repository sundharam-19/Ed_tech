from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def is_displayed(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()