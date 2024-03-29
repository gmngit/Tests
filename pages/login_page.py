from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    EMAIL = "//form/fieldset[1]//input"
    PASSWORD = "//form/fieldset[2]//input"
    LOGIN_BUTTON = "//form/button[text()='Войти']"

    def login(self, driver, url, email, password):
        # open page
        driver.get(url)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.EMAIL)))

        # fill in email field
        driver.find_element(By.XPATH, self.EMAIL).send_keys(email)

        # fill in password field
        driver.find_element(By.XPATH, self.PASSWORD).send_keys(password)

        # click on the button
        driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()
