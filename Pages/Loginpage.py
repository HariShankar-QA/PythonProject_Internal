from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    # locators stored as class attributes
    user_name = "//input[@id = 'user-name']"
    password = "//input[@id = 'password']"
    button = "//input[@id = 'login-button']"
    error_message = "//h3[@data-test='error']"

    def __init__(self, driver, timeout: int = 10):
        """Initialize page with a WebDriver and a WebDriverWait instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def accept_alert(self, timeout=5):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            # no alert is fine; keep silent for test runs
            pass

    def screenshot(self, name: str = "Login.png"):
        self.driver.save_screenshot(f".\\Screenshots\\{name}")

    def set_username(self, username: str):
        """Enter username using an explicit wait for visibility."""
        elem = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.user_name))
        )
        elem.clear()
        elem.send_keys(username)

    def set_password(self, password: str):
        """Enter password using an explicit wait for visibility."""
        elem = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.password))
        )
        elem.clear()
        elem.send_keys(password)

    def click_login(self):
        """Click the login button using an explicit wait for clickability."""
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button)))
        btn.click()

    def get_page_title(self) -> str:
        """Return the browser page title."""
        return self.driver.title

    def get_login_error_message(self) -> str:
        """Return the visible login error message text.

        Raises TimeoutException if no error message appears within the wait timeout.
        """
        try:
            err = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.error_message)))
            return err.text
        except TimeoutException:
            return ""

    def is_login_page_displayed(self) -> bool:
        """Return True when the primary login elements are present/visible."""
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.user_name)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button)))
            return True
        except TimeoutException:
            return False
