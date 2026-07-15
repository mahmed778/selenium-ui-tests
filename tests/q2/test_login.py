import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_q2_login():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    try:
        print(" Starting Q2 Login Test...")

        driver.get("https://secure.cambridgesavings.com/cambridgesavingsonlinebanking/uux.aspx#/login")
        time.sleep(5)

        print(" Page loaded")

        #  Find all q2-input shadow hosts
        hosts = driver.find_elements(By.CSS_SELECTOR, "q2-input")

        username_field = None
        password_field = None

        #  Extract actual input fields from shadow DOM
        for host in hosts:
            try:
                shadow_root = driver.execute_script(
                    "return arguments[0].shadowRoot", host
                )

                if shadow_root:
                    input_el = shadow_root.find_element(By.CSS_SELECTOR, "input")
                    field_type = input_el.get_attribute("type")

                    if field_type == "text" and username_field is None:
                        username_field = input_el

                    elif field_type == "password" and password_field is None:
                        password_field = input_el

            except:
                continue

        #  Enter credentials
        if username_field:
            username_field.send_keys("mahmedcsb")
            print(" Username entered")
        else:
            print(" Username field not found")

        if password_field:
            password_field.send_keys("Cambridge3!!")
            print(" Password entered")
        else:
            print(" Password field not found")

        #  Click login button (JS-based, stable)
        login_button = driver.execute_script("""
            return Array.from(document.querySelectorAll('button'))
                .find(b => b.innerText.toLowerCase().includes('log'))
        """)

        if login_button:
            driver.execute_script("arguments[0].click();", login_button)
            print(" Login button clicked")
        else:
            print(" Login button not found")

        #  Wait after login
        time.sleep(10)

        #  Basic validation (URL changed or page updated)
        current_url = driver.current_url.lower()
        print(" Current URL:", current_url)

        assert "login" not in current_url or "dashboard" in current_url

        print(" LOGIN TEST PASSED ")

    finally:
        driver.quit()
        print(" Browser closed")
