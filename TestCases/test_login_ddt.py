from Pages.CartPage import CartPage
from Pages.Loginpage import Login
from Pages.FirstPage import FirstPage
from Utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
from Utilities.customLogger import LogGen
import time
from Utilities import XLUtilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_002:
    base_url = ReadConfig.getApplicationURL()
    path = ".//Test Data/Login.xlsx"
    logger = LogGen.loggen()

    def test_login_case_ddt(self, setup):
        self.logger.info("Testing Login Case DDT")

        self.driver = setup
        self.driver.get(self.base_url)      # ⬅️ MISSING EARLIER

        self.lp = Login(self.driver)
        self.fp = FirstPage(self.driver)

        self.rows = XLUtilities.getRowCount(self.path, 'Sheet1')
        result_list = []

        for r in range(2, self.rows + 1):
            user = XLUtilities.readData(self.path, 'Sheet1', r, 1)
            password = XLUtilities.readData(self.path, 'Sheet1', r, 2)
            expected = XLUtilities.readData(self.path, 'Sheet1', r, 3)

            self.lp.set_username(user)
            self.lp.set_password(password)
            self.lp.click_login()

            # ------ CHECK LOGIN SUCCESS ------
            try:
                WebDriverWait(self.driver, 4).until(
                    EC.presence_of_element_located((By.XPATH, "//span[text()='Products']"))
                )
                login_success = True
            except:
                login_success = False

            # ------ VALIDATION ------
            if login_success and expected == "Pass":
                result_list.append("Pass")

                # logout only if successfully logged in
                self.fp.menu_button()
                self.fp.log_out()

            elif (not login_success) and expected == "Fail":
                result_list.append("Pass")

            else:
                result_list.append("Fail")

            # reset state
            self.driver.get(self.base_url)

        assert "Fail" not in result_list