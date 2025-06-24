from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from utils.utils import *
from config.settings import *

logger = get_logger(__name__)

sharepointTitle = By.CSS_SELECTOR, "#O365_AppName > span"
inputSearchBox = By.ID, "ms-searchux-input-0"
searchButton = By.CSS_SELECTOR, "#O365_SearchBoxContainer_container > div > form > button.submitSearchButton-100 > span"

def enterSearchKeyword(driver: WebDriver):
    try:
        searchBox = wait_for_visibility_of_element(driver, inputSearchBox)
        searchBox.clear()
        searchBox.send_keys(SEARCH_KEYWORD)
        logger.info(f"Search Keyword {SEARCH_KEYWORD} entered in the searchbar")
        clickSearchButton(driver)
    except:
        logger.error("Could notenter Search Keyword")

def clickSearchButton(driver: WebDriver):
    try:
        button = wait_for_visibility_of_element(driver, searchButton)
        button.click()
        logger.info("Search Initiated")
    except:
        logger.error("Could not click search button")