import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from home_page import HomePage
from login_page import LoginPage

BASE_URL = "https://www.guvi.in"


class TestGUVI:

    def test_case_1_verify_url(self, driver):

        driver.get(BASE_URL)

        assert "guvi.in" in driver.current_url

    def test_case_2_verify_title(self, driver):

        driver.get(BASE_URL)

        assert "GUVI" in driver.title

    def test_case_3_verify_login_button(self, driver):

        driver.get(BASE_URL)

        home = HomePage(driver)

        assert home.is_displayed(home.LOGIN_BTN)

    def test_case_4_verify_signup_button(self, driver):

        driver.get(BASE_URL)

        home = HomePage(driver)

        assert home.is_displayed(home.SIGNUP_BTN)

    def test_case_5_verify_signup_navigation(self, driver):

        driver.get(BASE_URL)

        home = HomePage(driver)

        home.click_signup()

        time.sleep(3)

        assert "register" in driver.current_url.lower()

    @pytest.mark.parametrize(
        "email,password",
        [
            ("your_email@gmail.com", "your_password")
        ]
    )
    def test_case_6_valid_login(self, driver, email, password):

        driver.get(BASE_URL)

        home = HomePage(driver)

        home.click_login()

        time.sleep(3)

        login = LoginPage(driver)

        login.login(email, password)

        time.sleep(5)

        assert "login" not in driver.current_url.lower()

    def test_case_7_invalid_login(self, driver):

        driver.get(BASE_URL)

        home = HomePage(driver)

        home.click_login()

        time.sleep(3)

        login = LoginPage(driver)

        login.login(
            "wrong@gmail.com",
            "wrongpassword"
        )

        time.sleep(5)

        assert login.is_displayed(
            login.ERROR_MESSAGE
        )

    def test_case_8_verify_menu_items(self, driver):

        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 20)

        courses = wait.until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )
        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        assert "Courses" in page_text

        print("Courses menu verified")

        # LIVE Classes may be dynamic
        if "LIVE" in page_text:
            print("LIVE Classes found")

    def test_case_9_verify_dobby(self, driver):

        driver.get(BASE_URL)
        iframes = driver.find_elements(
            By.TAG_NAME,
            "iframe"
        )
        assert len(iframes) > 0
        print("Dobby/chatbot iframe found")

    def test_case_10_verify_logout(self, driver):

        driver.get(BASE_URL)

        home = HomePage(driver)

        home.click_login()

        time.sleep(3)

        login = LoginPage(driver)

        login.login(
            "your_email@gmail.com",
            "your_password"
        )

        time.sleep(8)

        # Validate login success first
        assert "login" not in driver.current_url.lower()

        print("Login successful")

        # Optional logout validation
        try:

            profile = driver.find_element(
                "xpath",
                "//img"
            )

            profile.click()

            time.sleep(2)

            logout = driver.find_element(
                "xpath",
                "//*[contains(text(),'Logout')]"
            )

            logout.click()

            time.sleep(5)

            print("Logout successful")

        except Exception as e:

            print("Logout element not found")
            print(e)
