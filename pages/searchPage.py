from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from utils.utils import *
from config.settings import *
import time

logger = get_logger(__name__)

searchResults = By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div[1]/main/ol/li[1]"
searchResultsLink = (By.XPATH, "//h2[starts-with(@class, 'heading-')]")
nextPageButton = By.XPATH, "//button[starts-with(@class, 'button-') and @aria-label='Next page']"
fileTypeButton = By.XPATH, "//button[@aria-label='Filter by File type']"
deSelectAll = By.XPATH, "//button[.//span[text()='Deselect all']]"
powerPoint = By.XPATH, "//span[@title='PowerPoint']"
word = By.XPATH, "//span[@title='Word']"
excel = By.XPATH, "//span[@title='Excel']"
oneNote = By.XPATH, "//span[@title='OneNote']"
loop = By.XPATH, "//span[@title='Loop']"
pdf = By.XPATH, "//span[@title='PDF']"
photo = By.XPATH, "//span[@title='Photo']"
video = By.XPATH, "//span[@title='Video']"
webPage = By.XPATH, "//span[@title='Web Page']"
other = By.XPATH, "//span[@title='Other']"
applyButton = By.XPATH, "//span[text()='Apply']"

def waitForPageToLoad(driver: WebDriver):
    try:
        WebDriverWait(driver, timeout=IMPLICIT_WAIT_TIME)
    except:
        logger.error("Could not wait till page load")

def getAllResultsOnPage(driver: WebDriver, type: str):
    try:
        hrefs = []
        with open(f"./results/{type}_search_results.txt", "a") as f:
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

def scrape_all_pages(driver: WebDriver, type: str):
    page = 1
    while True:
        logger.info(f"Scraping page {page}...")
        getAllResultsOnPage(driver, type)

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

def scrapeAllPagesByFileType(driver: WebDriver):
    types = ["powerpoint", "word", "excel", "onenote", "loop", "pdf", "photo", "video", "webpage", "other"]

    typeButtonMapping = {
        "powerpoint": powerPoint,
        "word": word,
        "excel": excel,
        "onenote": oneNote,
        "loop": loop,
        "pdf": pdf,
        "photo": photo,
        "video": video,
        "webpage": webPage,
        "other": other,
    }


    for type in types:
        # Clear the file
        open(f"./results/{type}_search_results.txt", "w").close()
        
        # Get the locator from the mapping
        locator = typeButtonMapping.get(type)
        if locator:
            filter_button = wait_for_visibility_of_element(driver, fileTypeButton)
            filter_button.click()

            deselect_button = wait_for_visibility_of_element(driver, deSelectAll)
            deselect_button.click()
            
            button = wait_for_visibility_of_element(driver, locator)
            button.click()

            apply = wait_for_visibility_of_element(driver, applyButton)
            apply.click()

            time.sleep(5)
            scrape_all_pages(driver, type)