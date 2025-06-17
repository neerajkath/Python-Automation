import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import *

def get_logger(name):
    """Returns a configured logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Ensure handlers are not duplicated if logger is called multiple times
    if not logger.handlers:
        # Create handlers
        c_handler = logging.StreamHandler() # Console handler
        f_handler = logging.FileHandler(os.path.join(PROJECT_ROOT, "config", "test_automation.log")) # File handler

        # Create formatters and add it to handlers
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
    return logger

def get_driver(browser_name, headless=False):
    driver = None
    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu") # Recommended for headless
        options.add_argument("--window-size=1920,1080") # Set a window size for headless
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications") # Common option
        options.add_argument("--incognito") # Example option


    # Try webdriver_manager first
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    logger.info("Chrome driver initialized using WebDriverManager.")
    
    if driver:
        driver.maximize_window()
    return driver

def wait_for_visibility_of_element(driver, by_locator, timeout=EXPLICIT_WAIT_TIME):
    """
    Waits for an element to be visible on the page.
    Useful for dynamic content or elements that take time to load and appear.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(by_locator)
        )
        logger.info(f"Element {by_locator} is visible after waiting.")
        return element
    except Exception as e:
        logger.error(f"Element {by_locator} was not visible after {timeout} seconds. Error: {e}")
        raise # Re-raise the exception if the element doesn't become visible

# Initialize a base logger for the module
logger = get_logger(__name__)