import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_q2_login():

    # ✅ Setup Chrome (CI-friendly)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # important for GitHub
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 25)

    try:
        print("🚀 Starting Q2 Login Test...")

        # ✅ Open login page
        driver.get("https://secure.cambridgesavings.com/cambridgesavingsonlinebanking/uux.aspx#/login")

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(5)

        print("✅ Login page loaded")

        # ✅ Simple validation (page loaded correctly)
        assert "login" in driver.current_url.lower()

        print("✅ TEST PASSED — Page loaded successfully")

    finally:
        driver.quit()
        print("🧹 Browser closed")
