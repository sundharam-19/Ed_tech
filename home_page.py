from selenium.webdriver.common.by import By
from base_page import BasePage


class HomePage(BasePage):

    LOGIN_BTN = (By.XPATH, "//a[contains(text(),'Login')]")

    SIGNUP_BTN = (
        By.XPATH,
        "//a[contains(text(),'Sign Up')]"
    )

    COURSES = (
        By.XPATH,
        "//a[contains(@href,'courses')]"
    )

    LIVE_CLASSES = (
        By.XPATH,
        "//*[contains(text(),'LIVE')]"
    )

    PRACTICE = (
        By.XPATH,
        "//*[contains(text(),'Practice')]"
    )

    DOBBY = (
        By.XPATH,
        "//iframe"
    )

    PROFILE_ICON = (
        By.XPATH,
        "//img[contains(@alt,'profile')]"
    )

    LOGOUT = (
        By.XPATH,
        "//div[contains(text(),'Logout')]"
    )

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def click_signup(self):
        self.click(self.SIGNUP_BTN)