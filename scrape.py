from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#configurations
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = chrome_options)
# Setting up pages
wd.get("https://www.wikipedia.org/")
input_element = wd.find_element(by = By.ID, value = "searchInput")
input_element.send_keys("asd")
search = wd.find_element(by = By.CLASS_NAME,value="pure-button")
wd.execute_script("arguments[0].click();",search)
link_element = wd.find_element(by=By.LINK_TEXT,value="Adaptive software development")
wd.execute_script("arguments[0].click();",link_element)
#Scraping
p_tags = wd.find_elements(by = By.TAG_NAME,value = "p")
text = ''
for para in p_tags:
    text+=para.text
#print(text)
elem = wd.find_elements(by=By.CSS_SELECTOR,value = "p>a")
link_dict = {}
for e in elem:
    link_dict[e.text] = e.get_attribute('href')
#print(link_dict)