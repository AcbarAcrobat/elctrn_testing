from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Application:

    def __init__(self):
        """These are launch artifacts"""
        self.wd = WebDriver('/home/tester/elctrn_testing/driver/chromedriver')
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        """This is fast method to the open home page."""
        wd = self.wd
        wd.get('http://localhost:4000/')

    def select_operator(self):
        wd = self.wd
        wd.get('http://localhost:4000/')
        wd.find_element(By.XPATH, "//select[@name]").click()
        wd.find_element(By.XPATH, "//option[@value=666]").click()
        wd.find_element(By.XPATH, "//button").click()

    def header_page(self):
        wd = self.wd
        try:
            accept_button = WebDriverWait(wd, 10) \
                .until(EC.presence_of_element_located((By.XPATH, "(//button[contains(@class, 'inbox')])[2]")))
            return accept_button.is_visible()
        except TimeoutException:
            return False

    def destroy(self):
        self.wd.quit()
