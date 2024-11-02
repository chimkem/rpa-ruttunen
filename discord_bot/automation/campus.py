from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_from_campusonline(semester, level, language, field, number):
    """
    This function navigates to the CampusOnline course page, selects filters based on input,
    submits the search, and retrieves course details.
    """
    
    # Run options for selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    try:
        # Open Website
        driver.get("https://campusonline.fi/opintojaksot/")
        print("Navigated to CampusOnline.")

        # Handle cookie consent
        try:
            cookie_consent = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonDecline"))
            )
            cookie_consent.click()
            print("Cookie consent clicked.")
        except Exception as e:
            print("No cookie consent dialog found or could not be clicked.")

        # Click available courses
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#course-full"))).click()
        print("Expanded course filters.")

        # Function to click checkboxes with selected filters
        def click_checkbox(selectors, selected_items):
            for index, is_selected in enumerate(selected_items):
                if is_selected:
                    try:
                        checkbox = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selectors[index]))
                        )
                        checkbox.click()
                        print(f"Checkbox {selectors[index]} clicked.")
                    except Exception as e:
                        print(f"Could not click checkbox {selectors[index]}: {e}")

        # Define selectors and options for filters
        semester_selectors = ["#spring", "#summer", "#fall", "#continous"]
        semester_options = ['spring', 'summer', 'fall', 'continous']
        semester_selection = [option == semester for option in semester_options]
        click_checkbox(semester_selectors, semester_selection)

        level_selectors = ["#course-level-1", "#course-level-2"]
        level_options = ['amk', 'yamk']
        level_selection = [option == level for option in level_options]
        click_checkbox(level_selectors, level_selection)

        language_selectors = ["#fi", "#sv", "#en", "#ot"]
        language_options = ['finnish', 'swedish', 'english', 'other']
        language_selection = [option == language for option in language_options]
        click_checkbox(language_selectors, language_selection)

        field_selectors = [
            "#field-id0", "#field-id1", "#field-id2", "#field-id3", "#field-id4",
            "#field-id5", "#field-id6", "#field-id7", "#field-id8", "#field-id9", "#field-id10"
        ]
        field_options = ['kaikki', 'humanistinen', 'kielet', 'kulttuuri', 'luonnontiede',
                         'ymparistoala', 'matkailu', 'sote', 'tekniikka', 'yhteiskunta', 'yrittajyys']
        field_selection = [option == field for option in field_options]
        click_checkbox(field_selectors, field_selection)

        # Submit the search form
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit"))).click()
        print("Search form submitted.")

        # Wait for course elements to load
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card-content")))
            print("Course content loaded.")
        except Exception as e:
            print("Timeout while waiting for course content.")
            pass
        
        # Find all elements with ".card-content" selector
        course_divs = driver.find_elements(By.CSS_SELECTOR, ".card-content")
        courses_info = []

        # Loop for populating courses_info lists
        for course_div in course_divs[:number]:
            try:
                course_data = {
                    "institution": course_div.find_element(By.CSS_SELECTOR, ".campus span").text.strip(),
                    "points": course_div.find_element(By.CSS_SELECTOR, ".points.bold").text.strip(),
                    "name": course_div.find_element(By.TAG_NAME, "h4").text.strip(),
                    "date": course_div.find_element(By.CSS_SELECTOR, ".course-date.bold").text.strip(),
                    "language": course_div.find_element(By.XPATH, "div[span[text()='Opintojakson kieli:']]/span[2]").text.strip(),
                    "level": course_div.find_element(By.XPATH, "div[span[text()='Taso:']]/span[2]").text.strip(),
                    "enrollment_period": course_div.find_element(By.XPATH, "div[span[text()='Ilmoittautumisaika:']]/span[2]").text.strip(),
                    "link": course_div.find_element(By.CSS_SELECTOR, ".button black small").href()
                }
                courses_info.append(course_data)
                print(f"Course data collected: {course_data}")
            except Exception as e:
                print(f"Error retrieving course data: {e}")

    finally:
        # Close browser
        driver.quit()

    #Return course data
    return courses_info