import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'), override=True)

# --- Application URL ---
BASE_URL = os.getenv("BASE_URL")

# --- Browser Settings ---
BROWSER = os.getenv("BROWSER", "chrome")
# Convert string "True"/"False" from .env to boolean
HEADLESS_MODE = os.getenv("HEADLESS_MODE", "False").lower() == "true"

# --- Wait Times (in seconds) ---
# Convert string from .env to integer
IMPLICIT_WAIT_TIME = int(os.getenv("IMPLICIT_WAIT_TIME"))
EXPLICIT_WAIT_TIME = int(os.getenv("EXPLICIT_WAIT_TIME"))

# --- Test User Credentials (Example) ---
TEST_USERNAME = os.getenv("TEST_USERNAME")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

SEARCH_KEYWORD = os.getenv("SEARCH_KEYWORD")

# --- Paths ---
# Define PROJECT_ROOT relative to settings.py to ensure correct base path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))