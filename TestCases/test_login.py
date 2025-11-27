from Pages.CartPage import CartPage
from Pages.Loginpage import Login
from Pages.FirstPage import FirstPage
from Utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
from Utilities.customLogger import LogGen
import time

class Test_001:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_login_case(self,setup):
        self.logger.info("Testing Login Case")
        lp = Login(setup)
        fp = FirstPage(setup)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()
        lp.accept_alert()
        self.logger.info("Logged In successfully")
        if fp.prod_click() == "Products":
            assert True
            self.logger.info("Login Successful")
        else:
            lp.screenshot()
            assert False
        time.sleep(2)

    def test_adding_to_cart(self,setup):
        lp = Login(setup)
        fp = FirstPage(setup)
        cp = CartPage(setup)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()
        lp.accept_alert()
        self.logger.info("Logged In successfully")
        fp.add_cart()
        fp.accept_alert()
        assert cp.cart_title_check() == "Your Cart"
        self.logger.info("Cart Check passed")







