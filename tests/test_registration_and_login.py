from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from utilities.config import Config
from utilities.data_generator import DataGenerator
from models.user import User
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class TestRegistrationAndLogin:
    def test_register_and_login_successful(self, driver):
        url_reg_page = f"{Config.MAIN_URL}/register"
        url_login_page = f"{Config.MAIN_URL}/login"
        user_data = User(
            name=DataGenerator.generate_name(),
            email=DataGenerator.generate_email(),
            password=DataGenerator.generate_password()
        )

        registration_page = RegistrationPage()
        login_page = LoginPage()

        registration_page.register(driver, url_reg_page, user_data.name, user_data.email, user_data.password)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//main//h2[text()='Вход']")))
        assert url_login_page in driver.current_url

        login_page.login(driver, url_login_page, user_data.email, user_data.password)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//main//h1[text()='Соберите бургер']")))
        assert Config.MAIN_URL in driver.current_url

        time.sleep(3)
