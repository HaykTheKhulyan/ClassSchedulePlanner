from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

opts = Options()
browser = Chrome(options=opts)

browser.get('https://act.ucsd.edu/scheduleOfClasses')
select = Select(browser.find_element(By.ID, "selectedTerm"))
select.select_by_visible_text('Spring Quarter 2022')