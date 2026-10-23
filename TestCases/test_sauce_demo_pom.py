from Pages.Loginpage import Login
from Pages.FirstPage import FirstPage
from Utilities.readProperties import ReadConfig


class TestSauceDemoLogin:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_valid_login(self, setup):
        """Valid Login Test

        Steps:
        - verify login page displayed
        - enter credentials and login
        - assert page title and products header after login
        - close browser
        """
        driver = setup
        lp = Login(driver)

        # verify we are on the login page
        assert lp.is_login_page_displayed(), "Login page was not displayed"

        # perform login
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login()

        # verify landing page — use FirstPage POM to read header text
        fp = FirstPage(driver)
        assert fp.prod_click() == "Products", "Expected to land on Products page after login"

        # also assert browser title is correct
        assert lp.get_page_title() == "Swag Labs", "Unexpected page title after login"

        # close the browser as requested
        driver.quit()

    def test_invalid_login(self, setup):
        """Invalid Login Test

        Steps:
        - enter valid username and incorrect password
        - click login
        - verify error message shown and remain on login page
        - close browser
        """
        driver = setup
        lp = Login(driver)

        # enter username and incorrect password
        lp.set_username(self.username)
        lp.set_password("incorrect_password")
        lp.click_login()

        # verify error message contains Epic sadface (Sauce Demo standard text)
        err_text = lp.get_login_error_message()
        assert "Epic sadface" in err_text, f"Expected error message to contain 'Epic sadface', got: {err_text}"

        # assert still on login page
        assert lp.is_login_page_displayed(), "User should remain on login page after failed login"

        # take a screenshot of the failed/invalid login state and close the browser
        # saved to .\Screenshots\Invalid.png
        lp.screenshot("Invalid.png")
        driver.quit()


