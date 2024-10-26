from robocorp.tasks import task
from robocorp import browser

@task
def robot_spare_bin_python():
    # Configure the browser to slow down actions for better visibility
    browser.configure(slowmo=200)
    
    # Get data from Campus Online about courses with selected filters
    open_website()  # Navigate to the given URL
    semesters = ['spring', 'summer', 'fall', 'continous']  # User-chosen options for semesters to filter
    selected_semesters = select_semester(semesters)  # Get a dictionary indicating selected semesters
    levels = ['amk'] # User-chosen option for level to filter
    selected_level = select_level(levels) # Get a dictionary indicating selected level
    languages = ['finnish', 'english'] # User-chosen options for languages to filter
    selected_languages = select_language(languages) # Get a dictionary indicating selected languages
    fields = ['kaikki']
    selected_fields = select_field(fields)
    select_filters(selected_semesters, selected_level, selected_languages, selected_fields)  # Apply the filters based on the selected semesters
    search_courses() # Search for courses based on selected filters
    filters_save_png()  # Save a screenshot of the filtered results

def open_website():
    # Navigate to the given URL
    browser.goto("https://campusonline.fi/opintojaksot/")
    
def select_semester(semesters):
    # Create a dictionary that indicates which semesters are selected
    # This checks if each semester is present in the user-chosen semesters
    return {semester: semester in (sem.lower() for sem in semesters) for semester in ['spring', 'summer', 'fall', 'continous']}

def select_level(levels):
    # Create a dictionary that indicates which level is selected
    # This checks if each level is present in the user-chosen levels
    return {level: level in (lvl.lower() for lvl in levels) for level in ['amk', 'yamk']}

def select_language(languages):
    # Create a dictionary that indicates which languages is selected
    # This checks if each language is present in the user-chosen languages
    return {language: language in (lang.lower() for lang in languages) for language in ['finnish', 'swedish', 'english', 'other']}

def select_field(fields):
    # Create a dictionary that indicates which fields are selected
    # This checks if each field is present in the user-chosen fields
    return {field: field in (f.lower() for f in fields) for field in ['kaikki', 'humanistinen', 'kielet', 'kulttuuri', 'luonnontiede', 'ymparistoala', 'matkailu', 'sote', 'tekniikka', 'yhteiskunta', 'yrittajyys']} 

def select_filters(selected_semesters, selected_level, selected_languages, selected_fields):
    # Select filters on the page based on the user's selected options
    page = browser.page()

    # Click on the checkbox to only show available courses
    page.click("#course-full")

    # Mapping of semester names to their corresponding selectors
    semester_selectors = {
        'spring': "#spring",
        'summer': "#summer",
        'fall': "#fall",
        'continous': "#continous",
    }

    # Iterate through the selected semesters and click the corresponding filters
    for semester, is_selected in selected_semesters.items():
        if is_selected:
            page.click(semester_selectors[semester])

    # Mapping of level names to their corresponding selectors
    level_selectors = {
        'amk': "#course-level-1",
        'yamk': "#course-level-2",
    }
    
    # Iterate through the selected level and click the corresponding filter
    for level, is_selected in selected_level.items():
        if is_selected:
            page.click(level_selectors[level])
    
    # Mapping of languages to their corresponding selectors         
    language_selectors = {
        'finnish': "#fi",
        'swedish': "#sv",
        'english': "#en",
        'other':   "#ot",
    }

    # Iterate through the selected languages and click the corresponding filters
    for language, is_selected in selected_languages.items():
        if is_selected:
            page.click(language_selectors[language])
    
    # Mapping of fields to their corresponding selectors
    field_selectors = {
        'kaikki': "#field-id0",
        'humanistinen': "#field-id1",
        'kielet': "#field-id2",
        'kulttuuri': "#field-id3",
        'luonnontiede': "#field-id4",
        'ymparistoala': "#field-id5",
        'matkailu': "#field-id6",
        'sote': "#field-id7",
        'tekniikka': "#field-id8",
        'yhteiskunta': "#field-id9",
        'yrittajyys': "#field-id10",
    }
    
    # Iterate through the selected fields and click the corresponding filters
    for field, is_selected in selected_fields.items():
        if is_selected:
            page.click(field_selectors[field])

def search_courses():
    # Submit search request with selected filters
    page = browser.page()

    # Click on the search button to show courses based on selected filters
    page.click("#submit")
            
def filters_save_png():
    # Take a screenshot of the page showing the selected filters
    page = browser.page()
    page.screenshot(path="output/selected_filters.png")