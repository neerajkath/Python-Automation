from utils.utils import *
from config.settings import *
from pages import ssoPage, homePage, searchPage, excel
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver

logger = get_logger(__name__)
results_folder = "./results"

def main():
    logger.info("Starting Selenium automation task to find keywords in shared files")
    try:
        driver = get_driver(BROWSER, HEADLESS_MODE)
        logger.info(f"Successfully initialized {BROWSER} driver (headless: {HEADLESS_MODE}).")

        logger.info(f"Redirecting to {BASE_URL}")
        driver.get(BASE_URL)

        ssoPage.enterEmail(driver)
        ssoPage.enterPassword(driver)

        wait_for_visibility_of_element(driver, homePage.sharepointTitle)
        homePage.enterSearchKeyword(driver)

        searchPage.scrapeAllPagesByFileType(driver)
        logger.info("We have successfully collected all the links")

        scanForSensitiveTermsInFiles(driver)

        return True # Indicate task success

    except Exception as e:
        logger.error(f"An error occurred during the Google wait task: {e}")
        return False # Indicate task failure
    
    finally:
        if driver:
            logger.info("Automation finished. Quitting driver.")
            driver.quit()
        else:
            logger.warning("Driver was not initialized, skipping quit.")

def scanForSensitiveTermsInFiles(driver: WebDriver):
    for filename in os.listdir(results_folder):
        filepath = os.path.join(results_folder, filename)

        if not filename.endswith("_search_results.txt"):
            continue  # Skip irrelevant files

        logger.info(f"\nProcessing file: {filename}")
        with open(filepath, "r") as f:
            links = [line.strip() for line in f if line.strip()]

        # Decide logic based on file type
        match filename:
            case f if "excel" in f:
                for link in links:
                    driver.execute_script("window.open('');")
                    windows = driver.window_handles
                    driver.switch_to.window(windows[-1])
                    driver.get(link)
                    excel.checkForRedFlagTerms(driver)
            # case f if "word" in f:
            #     for link in links:
            #         print(f"[WORD] -> {link}")
            #         # call word scanner
            # case f if "powerpoint" in f:
            #     for link in links:
            #         print(f"[PPT] -> {link}")
            #         # call ppt scanner
            # case f if "photo" in f or "image" in f:
            #     for link in links:
            #         print(f"[Image] -> {link}")
            #         # maybe OCR scanner
            # case _:
            #     for link in links:
            #         print(f"[Generic] -> {link}")
            #         # generic scan

if __name__ == "__main__":
    main()