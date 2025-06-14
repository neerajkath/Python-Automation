from utils.utils import *
from config.settings import *
from selenium.webdriver.common.by import By

logger = get_logger(__name__)

def main():
    logger.info("Starting Selenium automation task to find keywords in shared files")
    try:
        driver = get_driver(BROWSER, HEADLESS_MODE)
        logger.info(f"Successfully initialized {BROWSER} driver (headless: {HEADLESS_MODE}).")

        driver.get(BASE_URL)

        wait_for_visibility_of_element(driver, (By.CLASS_NAME, "lnXdpd"))
        logger.info("Google logo SVG is visible. Task successful.")

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

if __name__ == "__main__":
    main()