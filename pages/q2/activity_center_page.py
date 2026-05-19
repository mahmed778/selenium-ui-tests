from selenium.webdriver.common.by import By
import time


class ActivityCenterPage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_activity_center(self):
        link = self.driver.execute_script("""
            return Array.from(document.querySelectorAll('a'))
                .find(a => a.innerText.toLowerCase().includes('activity'))
        """)
        if link:
            link.click()
            print("✅ Navigated to Activity Center")
        else:
            print("❌ Activity link not found")

        time.sleep(5)

    def get_transactions(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class,'transaction')]")

    def validate_transactions_exist(self):
        txns = self.get_transactions()
        assert len(txns) > 0
        print(f"✅ Transactions found: {len(txns)}")

    def validate_no_prenote(self):
        html = self.driver.page_source.lower()
        assert "prenote" not in html
        print("✅ No prenote label found")

    def open_first_transaction(self):
        txns = self.get_transactions()
        if txns:
            txns[0].click()
            print("✅ Opened transaction")
            time.sleep(3)

    def search_transactions(self):
        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        if inputs:
            inputs[0].send_keys("test")
            print("✅ Search executed")
            time.sleep(3)

    def simple_wait(self):
        time.sleep(3)
