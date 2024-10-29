from robocorp.tasks import task
from robocorp import browser

@task
def robot_spare_bin_python():
    open_website()
    selected_filters = configure_filters()
    select_filters(**selected_filters)
    search_courses()

def open_website():
    """Navigate to the given URL."""
    browser.goto("https://campusonline.fi/opintojaksot/")

def configure_filters():
    """Configure user-selected filters."""
    semesters = ['spring', 'summer', 'fall', 'continous']
    selected_semesters = select_semester(semesters)
    levels = ['amk']
    selected_level = select_level(levels)
    languages = ['finnish', 'english']
    selected_languages = select_language(languages)
    fields = ['kaikki']
    selected_fields = select_field(fields)
    return {
        'selected_semesters': selected_semesters,
        'selected_level': selected_level,
        'selected_languages': selected_languages,
        'selected_fields': selected_fields
    }

def select_semester(semesters):
    return {semester: semester in (sem.lower() for sem in semesters) for semester in ['spring', 'summer', 'fall', 'continous']}

def select_level(levels):
    return {level: level in (lvl.lower() for lvl in levels) for level in ['amk', 'yamk']}

def select_language(languages):
    return {language: language in (lang.lower() for lang in languages) for language in ['finnish', 'swedish', 'english', 'other']}

def select_field(fields):
    return {field: field in (f.lower() for f in fields) for field in ['kaikki', 'humanistinen', 'kielet', 'kulttuuri', 'luonnontiede', 'ymparistoala', 'matkailu', 'sote', 'tekniikka', 'yhteiskunta', 'yrittajyys']}

def select_filters(selected_semesters, selected_level, selected_languages, selected_fields):
    """Select filters based on user input."""
    page = browser.page()
    page.click("#course-full")

    # Generic function to click filter selectors
    def click_selectors(selectors, selected_items):
        for item, is_selected in selected_items.items():
            if is_selected:
                page.click(selectors[item])

    semester_selectors = {
        'spring': "#spring",
        'summer': "#summer",
        'fall': "#fall",
        'continous': "#continous",
    }
    click_selectors(semester_selectors, selected_semesters)

    level_selectors = {
        'amk': "#course-level-1",
        'yamk': "#course-level-2",
    }
    click_selectors(level_selectors, selected_level)

    language_selectors = {
        'finnish': "#fi",
        'swedish': "#sv",
        'english': "#en",
        'other': "#ot",
    }
    click_selectors(language_selectors, selected_languages)

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
    click_selectors(field_selectors, selected_fields)

def search_courses():
    """Submit the search request with selected filters."""
    page = browser.page()
    page.click("#submit")

def fetch_course_details():
    """Fetch and return course details from the page."""
    page = browser.page()
    course_divs = page.locator("body > div > div.row.favourite-courses > div")
    count = course_divs.count()
    courses_info = []

    for i in range(count):
        course_div = course_divs.nth(i)
        course_data = {
            "institution": course_div.locator(".campus span").inner_text().strip(),
            "points": course_div.locator(".points.bold").inner_text().strip(),
            "name": course_div.locator("h4").inner_text().strip(),
            "date": course_div.locator(".course-date.bold").inner_text().strip(),
            "language": course_div.locator("span:has-text('Opintojakson kieli:') + span").inner_text().strip(),
            "level": course_div.locator("span:has-text('Taso:') + span").inner_text().strip(),
            "enrollment period": course_div.locator("span:has-text('Ilmoittautumisaika:') + span").inner_text().strip()
        }
        courses_info.append(course_data)
    
    return courses_info