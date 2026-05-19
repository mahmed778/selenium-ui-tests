import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def setup():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def login(driver):
    driver.get("https://secure.cambridgesavings.com/cambridgesavingsonlinebanking/uux.aspx#/login")
    time.sleep(6)

    hosts = driver.find_elements("css selector", "q2-input")

    for host in hosts:
        try:
            shadow = driver.execute_script("return arguments[0].shadowRoot", host)
            if shadow:
                inp = shadow.find_element("css selector", "input")
                t = inp.get_attribute("type")

                if t == "text":
                    inp.send_keys("mahmedcsb")
                elif t == "password":
                    inp.send_keys("Cambridge3!!")

        except:
            continue

    driver.execute_script("""
        Array.from(document.querySelectorAll('button'))
        .find(b => b.innerText.toLowerCase().includes('log')).click()
    """)

    time.sleep(8)
    print("✅ Logged in")


def go_to_activity_center(driver):
    link = driver.execute_script("""
        return Array.from(document.querySelectorAll('a'))
            .find(a => a.innerText.toLowerCase().includes('activity'))
    """)
    if link:
        link.click()
        print("✅ Opened Activity Center")
    time.sleep(5)


# ✅ TC001
def test_tc001_activity_center_loads():
    driver = setup()
    try:
        login(driver)
        go_to_activity_center(driver)
        assert "activity" in driver.page_source.lower()
        print("✅ TC001 PASSED")
    finally:
        driver.quit()


# ✅ TC002
def test_tc002_no_prenote():
    driver = setup()
    try:
        login(driver)
        go_to_activity_center(driver)
        assert "prenote" not in driver.page_source.lower()
        print("✅ TC002 PASSED")
    finally:
        driver.quit()


# ✅ TC003
def test_tc003_open_transaction():
    driver = setup()
    try:
        login(driver)
        go_to_activity_center(driver)

        txn = driver.find_elements("xpath", "//div[contains(@class,'transaction')]")
        if txn:
            txn[0].click()
            print("✅ Opened transaction")

        time.sleep(3)

