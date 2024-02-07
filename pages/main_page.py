from selenium.webdriver.common.by import By


class LocatorsMainPage:
    TITLE = "//main//h1[text()='Соберите бургер']"
    PERSONAL_ACCOUNT_BUTTON = "//header/nav[1]/a[1]"
    LOGIN_BUTTON = "//main//button[text()='Войти в аккаунт']"


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_elements(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element
