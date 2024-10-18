from selenium import webdriver
# For Chrome
from selenium.webdriver.chrome.service import Service
# Locator things for webpage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# Wait for the cookie consent button to be present (optional but recommended)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
# Keep browser windwow open after program runs, un-comment for debugging
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

# Un-comment when actually running the bot (to use selenium wihtout actualy opening the window)
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# Init the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Test serach query, un-comment for dev purposes
search_query = {
    "search_phrase": "approt",
    "location": "everywhere"
}

# MAIN FUNCTION
def seach_from_kide_app(search_phrase, location="everywhere"):

    driver.get("https://kide.app/")

    # Wait until the cookie accept button is visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/header/o-consent/o-content/o-material/o-material__footer/button[2]"))
    )

    cookie_accept_button = driver.find_element(By.XPATH, "/html/body/header/o-consent/o-content/o-material/o-material__footer/button[2]")
    print(cookie_accept_button.get_attribute("innerHTML"))
    cookie_accept_button.click()



seach_from_kide_app(search_query["search_phrase"], search_query["location"])