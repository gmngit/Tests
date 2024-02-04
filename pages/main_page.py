from selenium.webdriver.common.by import By


class LocatorsMainPage:
    TITLE = "//main//h1[text()='Соберите бургер']"
    PERSONAL_ACCOUNT_BUTTON = "//header/nav[1]/a[1]"
    LOGIN_BUTTON = "//main//button[text()='Войти в аккаунт']"


class MainPage:
    def open_page(self, driver, url):
        driver.get(url)

    def find_elements(self, driver, locator):
        element = driver.find_element(By.XPATH, locator)
        return element
