from fixture.application import Application
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ClickON:

    def __init__(self):
        self.wd = None

    def click_on_elm(self):
        global element
        wd = self.wd
        try:
            element = wd.find_element_by()
        except:
            print("RETRYING CLICKON() for %s" % element)
            time.sleep(1)
            self.click_on_elm()
        else:
            element.click()
            time.sleep(3)

    def click_element_while_displayed(self):
        wd = self.wd
        element = wd.find_element(By.XPATH, "(//button[contains(@class, 'inbox')])[2]")
        try:
            while element.is_displayed():
                self.click_element_while_displayed()
        except:
            pass
