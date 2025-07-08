from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from utils.utils import *
from config.settings import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

iFrame = By.XPATH, "//iframe[contains(@name, 'WacFrame_Excel')]"
searchBar = By.XPATH, "//input[@id='TellMe-SearchBox']"
searchFind = By.XPATH, "//span[text()='Ctrl+F']"

def checkForRedFlagTerms(driver: WebDriver):
    driver.switch_to.frame(iFrame)
    logger.info("We are in iframe")

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('f').key_up(Keys.CONTROL).perform()
    logger.info("find open")

    inputBox = wait_for_visibility_of_element(driver, searchBar)
    inputBox.clear()
    inputBox.send_keys("find")

    findOption = wait_for_visibility_of_element(driver, searchFind)
    findOption.click()

    