from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LocatorsRegistrationPage:
    NAME = "//form/fieldset[1]//input"
    EMAIL = "//form/fieldset[2]//input"
    PASSWORD = "//form/fieldset[3]//input"
    REGISTER_BUTTON = "//form/button[text()='Зарегистрироваться']"


class RegistrationPage():
    def register(self, driver, url, name, email, password):
        # open page
        driver.get(url)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, LocatorsRegistrationPage.NAME)))

        # fill in name field
        driver.find_element(By.XPATH, LocatorsRegistrationPage.NAME).send_keys(name)

        # fill in email field
        driver.find_element(By.XPATH, LocatorsRegistrationPage.EMAIL).send_keys(email)

        # fill in password field
        driver.find_element(By.XPATH, LocatorsRegistrationPage.PASSWORD).send_keys(password)

        # click on the button
        driver.find_element(By.XPATH, LocatorsRegistrationPage.REGISTER_BUTTON).click()
