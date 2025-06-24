from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from utils.utils import *
from config.settings import *
import time

logger = get_logger(__name__)

searchResults = By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div[1]/main/ol/li[1]"
searchResultsLink = (By.XPATH, "//h2[starts-with(@class, 'heading-')]")
nextPageButton = By.XPATH, "//button[starts-with(@class, 'button-') and @aria-label='Next page']"

def waitForPageToLoad(driver: WebDriver):
    try:
        WebDriverWait(driver, timeout=IMPLICIT_WAIT_TIME)
    except:
        logger.error("Could not wait till page load")

def getAllResultsOnPage(driver: WebDriver):
    try:
        hrefs = []
        with open("./results/search_results.txt", "a") as f:
            results = wait_for_visibility_of_all_elements(driver, searchResultsLink)
            for item in results:
                try:
                    link = item.find_element(By.TAG_NAME, "a")
                    hrefs.append(link.get_attribute("href"))
                except:
                    continue
            logger.info("found links")
            for href in hrefs:
                f.write(href + "\n")
    except:
        logger.error("could not save the results to file")

def scrape_all_pages(driver: WebDriver):
    page = 1
    open("./results/search_results.txt", "w").close()
    while True:
        logger.info(f"Scraping page {page}...")
        getAllResultsOnPage(driver)

        try:
            button = wait_for_visibility_of_element(driver, nextPageButton)
            button.click()
            logger.info("Going to next page")
            page += 1

            time.sleep(5)
            wait_for_visibility_of_element(driver, searchResultsLink)

        except:
            logger.info("No more pages to scrape.")
            break