from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    EMAIL = "//form/fieldset[1]//input"
    PASSWORD = "//form/fieldset[2]//input"
    LOGIN_BUTTON = "//form/button[text()='Войти']"


class LoginPage(MainPage):
    def login(self, driver, url, email, password):
        # open page
        self.open_page(driver, url)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, LocatorsLoginPage.EMAIL)))
        assert url in driver.current_url

        # fill in email field
        self.find_elements(driver, LocatorsLoginPage.EMAIL).send_keys(email)

        # fill in password field
        self.find_elements(driver, LocatorsLoginPage.PASSWORD).send_keys(password)

        # click on the button
        self.find_elements(driver, LocatorsLoginPage.LOGIN_BUTTON).click()
