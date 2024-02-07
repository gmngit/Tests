from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    EMAIL = "//form/fieldset[1]//input"
    PASSWORD = "//form/fieldset[2]//input"
    LOGIN_BUTTON = "//form/button[text()='Войти']"


class LoginPage(MainPage):
    def login(self, url, email, password):
        # open page
        self.open_page(url)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, LocatorsLoginPage.EMAIL)))
        assert url in self.driver.current_url

        # fill in email field
        self.find_elements(LocatorsLoginPage.EMAIL).send_keys(email)

        # fill in password field
        self.find_elements(LocatorsLoginPage.PASSWORD).send_keys(password)

        # click on the button
        self.find_elements(LocatorsLoginPage.LOGIN_BUTTON).click()
