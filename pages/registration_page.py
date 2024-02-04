from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LocatorsRegistrationPage:
    NAME = "//form/fieldset[1]//input"
    EMAIL = "//form/fieldset[2]//input"
    PASSWORD = "//form/fieldset[3]//input"
    REGISTER_BUTTON = "//form/button[text()='Зарегистрироваться']"


class RegistrationPage(MainPage):
    def register(self, driver, url, name, email, password):
        # open page
        self.open_page(driver, url)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, LocatorsRegistrationPage.NAME)))
        assert url in driver.current_url

        # fill in name field
        name_input = self.find_elements(driver, LocatorsRegistrationPage.NAME)
        name_input.send_keys(name)
        try:
            assert len(name_input.get_attribute('value')) != 0
        except AssertionError:
            print('AssertionError: name field cannot be empty!')

        # fill in email field
        email_input = self.find_elements(driver, LocatorsRegistrationPage.EMAIL)
        email_input.send_keys(email)
        try:
            assert "@" and "." in email_input.get_attribute('value')
        except AssertionError:
            print('AssertionError: Expected format of email field: login@domen')

        # fill in password field
        password_input = self.find_elements(driver, LocatorsRegistrationPage.PASSWORD)
        password_input.send_keys(password)
        try:
            assert len(password_input.get_attribute('value')) >= 6
        except AssertionError:
            print('AssertionError: password field should be more than 6 symbols')

        # click on the button
        register_button = self.find_elements(driver, LocatorsRegistrationPage.REGISTER_BUTTON)
        register_button.click()
