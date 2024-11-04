# SELENIUM IMPORTS
from selenium import webdriver
# For Chrome
from selenium.webdriver.chrome.service import Service
# Locator things for webpage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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

  # 👀 Un-comment when in production. To use selenium wihtout actualy opening the window
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")



    # 👀 Comment when in production. Test serach query, un-comment for dev purposes.
    # search_query = {
    #     "search_phrase": "approt",
    #     "location": "everywhere"
    # }
        # Open website


# MAIN FUNCTION 💯
def seach_from_kide_app(search_phrase):

        # Init the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://kide.app/")

    # Wait until the cookie accept button is visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/header/o-consent/o-content/o-material/o-material__footer/button[2]"))
    )
    cookie_accept_button = driver.find_element(By.XPATH, "/html/body/header/o-consent/o-content/o-material/o-material__footer/button[2]")
    cookie_accept_button.click()

    # Search field by id. Make CSS / Xpath version if this breaks for some reason
    search_field = driver.find_element(By.ID, "input-1")
    search_field.send_keys(search_phrase)
    search_field.send_keys(Keys.RETURN)

# Find search results and return an array of objects.
    # Wait 10 seconds for element/container that contains the search results. If does not appear, no search results and return 0.
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/ui-view/o-page/o-section/o-content/o-grid[3]/div/o-grid[1]"))
        )
    except:
        print("No event's were found!💀")
        return 0        

    # Initialize array for events
    array_for_events = []

    # Contains array of all DIV elements. They contain information for single event.
    all_events = driver.find_elements(By.CSS_SELECTOR, "o-grid.o-margin-bottom--half-gutter:nth-child(1) > div:nth-child(2) > o-product-list:nth-child(1) > o-grid:nth-child(1) > *")

    # print(f"This is the length of all_events array where ALL THE EVENT DIV'S ARE STORED: {len(all_events)} \n")

    for event in all_events[:5]:
        # Relative CSS selectors for items inside each DIV (which contains single event)
        title_selector = event.find_element(By.CSS_SELECTOR, "* > o-product-card:nth-child(1) > o-card:nth-child(1) > o-card__content:nth-child(2) > div:nth-child(1)")
        title = title_selector.get_attribute("innerHTML")
        # print(title)
        time_and_place_selector = event.find_element(By.CSS_SELECTOR, "* > o-product-card:nth-child(1) > o-card:nth-child(1) > o-card__content:nth-child(2) > div:nth-child(2)")
        time_and_place = time_and_place_selector.get_attribute("innerHTML")
        # print(time_and_place)
        price_selector = event.find_element(By.CSS_SELECTOR, "* > o-product-card:nth-child(1) > o-card:nth-child(1) > o-card__footer:nth-child(3) > div:nth-child(4)")
        price = price_selector.get_attribute("innerHTML")
        price_cleaned = price.replace("&nbsp;", "").strip()
        # print(price)

        # Initialize object for event informationn
        event_info = {}
        event_info["event_name"] = title
        event_info["event_location"] = time_and_place
        event_info["event_price"] = price_cleaned
        array_for_events.append(event_info)

        # Debugging prints for CONTENT and LENGTH of the array containen event infoamtion
        # print(f"This is the CONTENT for array_for_events AFTER APPENDING NEW EVENT it\n {array_for_events}\n")
        # print(f"This is the LENGTH for array_for_events AFTER appending new event: {len(array_for_events)} \n")

    print(f"This is the CONTENT for array_for_events BEFORE RETURN:\n\n {array_for_events}\n")
    driver.quit()
    return array_for_events

# 👀 Comment when in production. Running function for test/dev purposes.
# seach_from_kide_app(search_query["search_phrase"])















# TESTING AREA TESTING AREA TESTING AREA TESTING AREA TESTING AREA TESTING AREA TESTING AREA TESTING AREA TESTING AREA TESTING AREA TESTING AREA TESTING AREA TESTING AREA 

# Search for the specific phrase in the entire document
# search_phrase = "Check your keywords for typos or try using another keyword"
# xpath_query = f'//*[contains(text(), "{search_phrase}")]'

# perse = "/html/body/main/ui-view/o-page/o-section/o-content/o-grid[2]/div[3]/div/sh"

# thing = driver.find_element(By.XPATH, perse)
# print("that thangggg")
# print(thing)




# if results_array_length == 1:
#     event_name_xpath = f'/html/body/main/ui-view/o-page/o-section/o-content/o-grid[3]/div/o-grid[1]/div[2]/o-product-list/o-grid/div/o-product-card/o-card/o-card__content/div[1]'
#     event_name = driver.find_element(By.XPATH, event_name_xpath)

#     event_location_xpath = f'/html/body/main/ui-view/o-page/o-section/o-content/o-grid[3]/div/o-grid[1]/div[2]/o-product-list/o-grid/div/o-product-card/o-card/o-card__content/div[2]'
#     event_location = driver.find_element(By.XPATH, event_location_xpath)

#     event_price_xpath = f'/html/body/main/ui-view/o-page/o-section/o-content/o-grid[3]/div/o-grid[1]/div[2]/o-product-list/o-grid/div/o-product-card/o-card/o-card__footer/div[2]'
#     event_price = driver.find_element(By.XPATH, event_price_xpath)
#     price_cleaned = event_price.get_attribute("innerHTML").replace("&nbsp;", "").strip()

#     event_info = {}
#     event_info["event_name"] = event_name.get_attribute("innerHTML")
#     event_info["event_location"] = event_location.get_attribute("innerHTML")
#     event_info["event_price"] = price_cleaned

#     array_for_events.append(event_info)
#     #print(array_for_events)
#     return
# return