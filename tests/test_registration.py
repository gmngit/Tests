from pages.registration_page import RegistrationPage
from utilities.config import Config
from utilities.data_generator import DataGenerator
from models.user import User
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class TestRegistration:

    def test_register_successful(self, driver):
        url = f"{Config.MAIN_URL}/register"
        user_data = User(
            name=DataGenerator.generate_name(),
            email=DataGenerator.generate_email(),
            password=DataGenerator.generate_password()
        )

        registration_page = RegistrationPage()
        registration_page.register(driver, url, user_data.name, user_data.email, user_data.password)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//main//h2[text()='Вход']")))

        assert f"{Config.MAIN_URL}/login" in driver.current_url

        time.sleep(3)
