from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import json
import pprint

try:
    opts = Options()
    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = Chrome(options=opts)

    browser.get('https://act.ucsd.edu/scheduleOfClasses')
    select = Select(browser.find_element(By.ID, "selectedTerm"))
    select.select_by_visible_text('Spring Quarter 2022')

    # need to sleep here because executing the next line immediately after the
    # previous line leads to StaleElementReferenceException
    # i think this is because the next line does not give the webpage time to load
    # before trying to access the elements
    # see: https://selenium-python.readthedocs.io/waits.html
    # in the future, maybe implement a smarter waiting condition?
    time.sleep(0.1)

    subjects = Select(browser.find_element(By.ID, "selectedSubjects"))

    # the dictionary object used to encode the class schedule
    schedule = {}
    schedule["subjects"] = {}

    # printing helper for pretty dicts
    pp = pprint.PrettyPrinter(indent=2)

    for subject in subjects.options:
        schedule["subjects"][subject.get_attribute("value")] = {}
        #print(subject.get_attribute("value"))

    pp.pprint(schedule)

finally:
    browser.quit()