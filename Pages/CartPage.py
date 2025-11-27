from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    cart_title = "//span[@class='title']"

    def __init__(self, driver):
        self.driver = driver

    def accept_alert(self, timeout=5):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alert accepted.")
        except NoAlertPresentException:
            print("No alert found to accept.")

    def cart_title_check(self):
        return self.driver.find_element(By.XPATH, self.cart_title).text