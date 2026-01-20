from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------------- CONFIG ----------------
TINDER_URL = "https://tinder.com"
SWIPE_DELAY = 2  # seconds between swipes

# ---------------- DRIVER SETUP ----------------
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(TINDER_URL)

wait = WebDriverWait(driver, 30)

# ---------------- LOGIN (MANUAL) ----------------
print("👉 Please login manually (Google/Facebook/Phone)")
print("⏳ Waiting 40 seconds...")
time.sleep(40)

# ---------------- HANDLE POPUPS ----------------
def close_popup(xpath):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    except:
        pass

# Allow location
close_popup("//button[contains(text(),'Allow')]")

# Disable notifications
close_popup("//button[contains(text(),'Not interested')]")

# Close match popup
close_popup("//button[contains(@aria-label,'Back')]")

# ---------------- AUTO SWIPE ----------------
print("🔥 Starting auto swipe...")

while True:
    try:
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ARROW_RIGHT)  # Like
        print("❤️ Swiped Right")
        time.sleep(SWIPE_DELAY)

    except Exception as e:
        print("⚠️ Error occurred:", e)
        time.sleep(5)