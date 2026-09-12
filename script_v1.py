import logging
import os
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("browser.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)

LOGIN_URL = os.environ.get("LOGIN_URL")
if not LOGIN_URL:
    raise EnvironmentError("LOGIN_URL environment variable is not set.")


def open_login_page() -> webdriver.Chrome:
    """Open the visa appointment login page and return the active browser."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    logger.info("Navigating to LOGIN_URL: %s", LOGIN_URL)
    driver.get(LOGIN_URL)

    WebDriverWait(driver, 30).until(
        lambda browser: browser.execute_script("return document.readyState")
        == "complete"
    )
    logger.info("Page load complete.")
    return driver


browser = open_login_page()

logger.info("Browser content:\n%s", browser.page_source)
print(browser.page_source)
