# SELENIUM IMPORTS
from selenium import webdriver
# For Chrome
from selenium.webdriver.chrome.service import Service
# Locator things for webpage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
# Wait for the cookie consent button to be present (optional but recommended)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# OTHER IMPORTS
from webdriver_manager.chrome import ChromeDriverManager


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
    # print(cookie_accept_button.get_attribute("innerHTML"))
    cookie_accept_button.click()

    # Search field by id. un-comment Xpath version if this breaks for some reason
    search_field = driver.find_element(By.ID, "input-1")
    # Search field by Xpath. un-comment of other option breaks for some reason
    # search_field2 = driver.find_element(By.XPATH, "/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[1]/o-input-container/input")
    search_field.send_keys(search_phrase)
    search_field.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/main/ui-view/o-page/o-section/o-content/o-grid[3]/div/o-grid[1]/div[2]/o-product-list/o-grid/*"))
    )

    # index = 1 
    # event_container = f'/html/body/main/ui-view/o-page/o-section/o-content/o-grid[3]/div/o-grid[1]/div[2]/o-product-list/o-grid'



    array_for_events = []
    for i in range(1, 6):
        event_name_xpath = f'/html/body/main/ui-view/o-page/o-section/o-content/o-grid[3]/div/o-grid[1]/div[2]/o-product-list/o-grid/div[{i}]/o-product-card/o-card/o-card__content/div[1]'
        event_name = driver.find_element(By.XPATH, event_name_xpath)

        event_location_xpath = f'/html/body/main/ui-view/o-page/o-section/o-content/o-grid[3]/div/o-grid[1]/div[2]/o-product-list/o-grid/div[{i}]/o-product-card/o-card/o-card__content/div[2]'
        event_location = driver.find_element(By.XPATH, event_location_xpath)

        event_price_xpath = f'/html/body/main/ui-view/o-page/o-section/o-content/o-grid[3]/div/o-grid[1]/div[2]/o-product-list/o-grid/div[{i}]/o-product-card/o-card/o-card__footer/div[2]'
        event_price = driver.find_element(By.XPATH, event_price_xpath)

        event_info = {}
        event_info["event_name"] = event_name.get_attribute("innerHTML")
        event_info["event_location"] = event_location.get_attribute("innerHTML")
        event_info["event_price"] = event_price.get_attribute("innerHTML")

        array_for_events.append(event_info)

        print(event_name.get_attribute("innerHTML"))
        print(event_location.get_attribute("innerHTML"))
        print(event_price.get_attribute("innerHTML"))

    print("Array for events:")
    print(array_for_events)


seach_from_kide_app(search_query["search_phrase"], search_query["location"])