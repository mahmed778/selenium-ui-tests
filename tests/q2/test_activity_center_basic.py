
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_login_with_mfa():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        print("🚀 Starting login test")

        driver.get("https://secure.cambridgesavings.com/cambridgesavingsonlinebanking/test/uux.aspx#/login")

        time.sleep(5)

        # ✅ USERNAME
        user_host = driver.find_element(By.CSS_SELECTOR, "q2-input[test-id='fldUsername']")
        user_shadow = driver.execute_script("return arguments[0].shadowRoot", user_host)
        username = user_shadow.find_element(By.CSS_SELECTOR, "input")

        # ✅ PASSWORD
        pass_host = driver.find_element(By.CSS_SELECTOR, "q2-input[test-id='fldPassword']")
        pass_shadow = driver.execute_script("return arguments[0].shadowRoot", pass_host)
        password = pass_shadow.find_element(By.CSS_SELECTOR, "input")

        # ✅ ENTER CREDS
        username.clear()
        username.send_keys("mahmedcsb")
        print("✅ Username entered")

        password.clear()
        password.send_keys("Cambridge3!!")
        print("✅ Password entered")

        time.sleep(2)

        # ✅ LOGIN BUTTON
        btn_host = driver.find_element(By.CSS_SELECTOR, "q2-btn[test-id='btnSubmit']")
        btn_shadow = driver.execute_script("return arguments[0].shadowRoot", btn_host)
        login_button = btn_shadow.find_element(By.CSS_SELECTOR, "button")

        login_button.click()
        print("✅ Login clicked")

        # ✅ 🔥 STOP HERE FOR OTP
        print("👉 Enter your OTP / MFA token in the browser")

        input("👉 After entering the OTP, press ENTER here to continue...")

        print("✅ OTP step completed")

        time.sleep(5)

        # ✅ VERIFY LOGIN SUCCESS
        if "login" not in driver.current_url.lower():
            print("✅ LOGIN SUCCESSFUL ✅")
        else:
            print("❌ STILL ON LOGIN PAGE")

        time.sleep(5)

    finally:
        driver.quit()
