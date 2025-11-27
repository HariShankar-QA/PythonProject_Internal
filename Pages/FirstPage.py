from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FirstPage:
    prod_title = "//span[@class = 'title']"
    sauce_labs_back_bag = "//button[@id = 'add-to-cart-sauce-labs-backpack']"
    add_to_cart = "//a[@class = 'shopping_cart_link']"
    menu = "//button[@id = 'react-burger-menu-btn']"
    logout = "//a[@id = 'logout_sidebar_link']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)     # ⬅️ ADD WAIT HERE

    def screenshot(self):
        self.driver.save_screenshot(".\\Screenshots\\First.png")

    def accept_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alert accepted.")
        except NoAlertPresentException:
            print("No alert found to accept.")

    def prod_click(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.prod_title))
        )
        return element.text

    def sauce_labs(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.sauce_labs_back_bag))
        )
        btn.click()

    def add_cart(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart))
        )
        btn.click()

    def menu_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.menu))
        ).click()

    def log_out(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.logout))
        ).click()

