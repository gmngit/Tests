from selenium import webdriver
from pages.main_page import MainPage, LocatorsMainPage
from pages.login_page import LoginPage, LocatorsLoginPage
from utilities.config import Config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class TestLogin:
    def test_login_successful(self):
        url = f"{Config.MAIN_URL}/login"
        email = Config.EMAIL
        password = Config.PASSWORD

        driver = webdriver.Chrome()

        login_page = LoginPage(driver)
        login_page.login(url, email, password)

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, LocatorsMainPage.TITLE)))

        assert Config.MAIN_URL in driver.current_url

        time.sleep(3)
        driver.quit()

    def test_from_main_page_to_login_page_by_personal_acc_button(self):
        url = Config.MAIN_URL

        driver = webdriver.Chrome()
        main_page = MainPage(driver)
        main_page.open_page(url)

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, LocatorsMainPage.PERSONAL_ACCOUNT_BUTTON)))

        main_page.find_elements(LocatorsMainPage.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, LocatorsLoginPage.EMAIL)))

        assert f"{Config.MAIN_URL}/login" in driver.current_url

        time.sleep(3)
        driver.quit()
        