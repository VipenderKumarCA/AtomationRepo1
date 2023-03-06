from selenium.webdriver.common.by import By
from base.seleniumDriver import SeleniumDriver
import time


class Login(SeleniumDriver):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
    signIn = "(//a[@class = 'dynamic-link'])[4]"
    email = "(//input[@id='email'])[1]"
    password = "password"
    login__ = "login"
    allCourses = "//a[text()='ALL COURSES']"
    dropdown = "//span[@class='caret']"
    logoutButton = "//a[@href='/logout']"

    def clickSignin(self):
        self.clickElement(self.signIn, By.XPATH)

    def getUserName(self):
        return self.getElement(By.XPATH, self.email)

    def username(self, text):
        self.enterInElement(self.getUserName(), text)

    def getPassword(self):
        return self.getElement(By.ID, self.password)

    def inputPassword(self, value):
        self.enterInElement(self.getPassword(), value)

    def clickLogin(self):
        self.clickElement(self.login__, By.ID)

    def clickAllCourses(self):
        self.clickElement(self.allCourses, By.XPATH)

    def loginLetsKodeit(self, text, value):
        self.clickSignin()
        self.username(text)
        time.sleep(3)
        self.inputPassword(value)
        self.clickLogin()
        self.clickAllCourses()

    def logout(self):
        self.clickElement(self.dropdown, By.XPATH)
        self.clickElement(self.logoutButton, By.XPATH)