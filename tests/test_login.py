from pages.login_page import LoginPage
from utilities.config import Config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class TestLogin:
    def test_login_successful(self, driver):
        url = f"{Config.MAIN_URL}/login"
        email = Config.EMAIL
        password = Config.PASSWORD

        login_page = LoginPage()
        login_page.login(driver, url, email, password)

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//main//h1[text()='Соберите бургер']")))

        assert Config.MAIN_URL in driver.current_url

        time.sleep(3)
