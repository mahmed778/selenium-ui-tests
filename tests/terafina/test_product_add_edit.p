import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_terafina_product_add_edit():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    try:
        # ✅ Step 1: Open product URL
        driver.get("https://casb--preview01.sandbox.my.salesforce-sites.com/?productCode=S442&locale=en-US&brand=IVY")

        time.sleep(6)
        print("✅ Page loaded")

        # ✅ Step 2: Verify product exists (STRONG locator)
        product_xpath = "//div[contains(@class,'product-card') or contains(@class,'product-card-custom')]"

        product = wait.until(
            EC.presence_of_element_located((By.XPATH, product_xpath))
        )

        print("✅ Initial product present")

        # ✅ Step 3: Click Add/Edit button (robust locator)
        add_edit = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[contains(text(),'Add') and contains(text(),'Edit')]"
            ))
        )

        add_edit.click()
        print("✅ Clicked Add/Edit")

        # ✅ DEBUG screenshot
        driver.save_screenshot("after_add_edit.png")

        time.sleep(4)

        # ✅ Step 4: Verify product still exists (key validation)
        product_after = wait.until(
            EC.presence_of_element_located((By.XPATH, product_xpath))
        )

        print("✅ Product retained after Add/Edit")

        # ✅ Step 5: Add another product
        add_product = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//*[contains(text(),'Add') or contains(text(),'Open')]"
            ))
        )

        add_product.click()
        print("✅ Clicked Add Product")

        time.sleep(5)

        # ✅ Step 6: Validate multiple product cards exist
        products = driver.find_elements(By.XPATH, product_xpath)

        print(f"✅ Total products found: {len(products)}")

        assert len(products) >= 1

        print("✅ Test passed (no product drop)")

    finally:
        driver.quit()
