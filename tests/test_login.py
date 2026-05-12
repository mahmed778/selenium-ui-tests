import os
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    driver = get_driver()

    try:
        login_page = LoginPage(driver)

        # Open login page
        login_page.load()

        # Get credentials
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")

        # Perform login
        login_page.login(username, password)

        # Wait for dashboard element
        wait = WebDriverWait(driver, 20)

        dashboard = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@test-id='contentBlockName']")
            )
        )

        assert dashboard is not None

    finally:
        driver.quit()
