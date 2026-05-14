import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_terafina_product_add_edit():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 25)

    try:
        print("🚀 Starting Test...")

        # ✅ Step 1: Open URL
        driver.get("https://casb--preview01.sandbox.my.salesforce-sites.com/?productCode=S442&locale=en-US&brand=IVY")

        # ✅ Step 2: Wait for page
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(5)

        print("✅ Page loaded")

        # ✅ Step 3: Confirm product is present
        wait.until(EC.presence_of_element_located((
            By.XPATH,
            "//div[contains(@class,'product')]"
        )))

        print("✅ Product found")

        driver.save_screenshot("initial.png")

        # ✅ Step 4: USE YOUR REAL XPATH
        add_edit_xpath = "/html/body/app-root/div/main/app-consumer/div/tf-stepper/div/div[1]/app-stepper-custom-header/div/div[1]/div/div[1]/div"

        add_edit = wait.until(
            EC.presence_of_element_located((By.XPATH, add_edit_xpath))
        )

        # ✅ Scroll and click (IMPORTANT)
        driver.execute_script("arguments[0].scrollIntoView(true);", add_edit)
        time.sleep(1)

        driver.execute_script("arguments[0].click();", add_edit)

        print("✅ Clicked Add/Edit (real element)")

        # ✅ Wait after click
        time.sleep(4)
        driver.save_screenshot("after_click.png")

        # ✅ Validate product still exists
        products = driver.find_elements(By.XPATH, "//div[contains(@class,'product')]")

        print(f"✅ Products after click: {len(products)}")

        assert len(products) >= 1

        print("✅ TEST PASSED — Product NOT dropped ✅")

    finally:
        driver.quit()
        print("🧹 Browser closed")
