from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (By.ID, "email")

    PASSWORD = (By.ID, "password")

    LOGIN_SUBMIT = (
        By.XPATH,
        "//a[contains(text(),'Login')]"
    )

    ERROR_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Incorrect')]"
    )

    def login(self, email, password):

        self.enter_text(self.EMAIL, email)

        self.enter_text(self.PASSWORD, password)

        self.click(self.LOGIN_SUBMIT)