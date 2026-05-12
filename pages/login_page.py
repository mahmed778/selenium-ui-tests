from selenium.webdriver.common.by import By
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(
            "https://secure.cambridgesavings.com/cambridgesavingsonlinebanking/test/uux.aspx#/login"
        )
        time.sleep(6)
        print("✅ Page loaded")

    def get_all_shadow_roots(self, root):

        shadow_roots = []

        elements = root.find_elements(By.XPATH, ".//*")

        for el in elements:
            try:
                shadow = self.driver.execute_script(
                    "return arguments[0].shadowRoot", el
                )
                if shadow:
                    shadow_roots.append(shadow)
                    shadow_roots.extend(self.get_all_shadow_roots(shadow))
            except:
                continue

        return shadow_roots

    def login(self, username, password):

        time.sleep(3)

        print("🔍 Searching entire DOM + Shadow DOM...")

        # ✅ get main document
        main = self.driver

        # ✅ collect shadow roots
        shadow_roots = self.get_all_shadow_roots(main)

        print(f"Found {len(shadow_roots)} shadow roots")

        found_username = False
        found_password = False
        login_button = None

        # ✅ search in main DOM + all shadow roots
        all_scopes = [main] + shadow_roots

        for scope in all_scopes:
            try:
                inputs = scope.find_elements(By.CSS_SELECTOR, "input")

                for inp in inputs:
                    input_type = inp.get_attribute("type")

                    if input_type == "text" and not found_username:
                        inp.send_keys(username)
                        print("✅ Username entered")
                        found_username = True

                    elif input_type == "password" and not found_password:
                        inp.send_keys(password)
                        print("✅ Password entered")
                        found_password = True

                # ✅ find login button
                buttons = scope.find_elements(By.CSS_SELECTOR, "button")

                for btn in buttons:
                    if "log" in btn.text.lower():
                        login_button = btn

            except:
                continue

        # ✅ click found login button
        if login_button:
            login_button.click()
            print("✅ Login clicked")
        else:
            print("❌ Login button not found")
