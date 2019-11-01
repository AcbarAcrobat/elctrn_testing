# # coding=utf-8
# import time
# from selenium import webdriver
# from config import capabilities
# from fixture.session import SessionHelper
# from fixture.locators import Locators
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.remote.file_detector import LocalFileDetector
#
#
# command_executor = "http://127.0.0.1:4444/wd/hub"
#
#
# class Application:
#
#     def __init__(self):
#         """These are launch artifacts"""
#         self.Locators = Locators
#         self.wd = webdriver.Remote(
#             command_executor=command_executor,
#             desired_capabilities=capabilities
#         )
#         self.wd.implicitly_wait(60)
#         self.session = SessionHelper(self)
#
#
#     def destroy(self):
#         self.wd.quit()