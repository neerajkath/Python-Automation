from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from utils.utils import *
from config.settings import *

searchBar = By.XPATH, ""

def checkForRedFlagTerms(driver: WebDriver):
    inputBox = wait_for_visibility_of_element(driver, searchBar)
    inputBox.clear()
    inputBox.send_keys()