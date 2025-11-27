from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    user_name = "//input[@id = 'user-name']"
    password = "//input[@id = 'password']"
    button = "//input[@id = 'login-button']"


    def __init__(self,driver):
        self.driver = driver

    def accept_alert(self, timeout=5):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alert accepted.")
        except NoAlertPresentException:
            print("No alert found to accept.")

    def screenshot(self):
        self.driver.save_screenshot(".\\Screenshots\\"+ "Login.png")

    def set_username(self,username):
        self.driver.find_element(By.XPATH, self.user_name).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.XPATH, self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button).click()