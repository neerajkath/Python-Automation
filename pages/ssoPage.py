from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from utils.utils import *
from config.settings import *

logger = get_logger(__name__)

emaiInputBox = By.ID, "i0116"
nextButton = By.ID, "idSIButton9"
passwordInputBox = By.ID, "i0118"

def enterEmail(driver: WebDriver):
    try:
        inputBox = wait_for_visibility_of_element(driver, emaiInputBox)
        inputBox.clear()
        inputBox.send_keys(TEST_USERNAME)
        clickNextButton(driver)
        logger.info("email has been entered")
    except:
        logger.error("Failed to enter email")

def enterPassword(driver: WebDriver):
    try:
        inputBox = wait_for_visibility_of_element(driver, passwordInputBox)
        inputBox.clear()
        inputBox.send_keys(TEST_PASSWORD)
        clickNextButton(driver)
        logger.info("password has been entered")
    except:
        logger.error("Failed to enter email")

def clickNextButton(driver: WebDriver):
    try:
        button = wait_for_visibility_of_element(driver, nextButton)
        button.click()
        logger.info("next buttton is clicked")
    except:
        logger.error("Can not click next button")