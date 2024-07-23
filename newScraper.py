from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

website = "https://hprera.nic.in/PublicDashboard"

chrome_options = Options()

chrome_driver_path = "D:/chromedriver/chromedriver.exe"  # Update this path

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(website)

WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//div[@class="shadow py-3 px-3 font-sm radius-3 mb-2"]')))

# Function 
def extract_project_details(project_element):
    details = {}
    details['Project Name'] = project_element.find_element(By.XPATH, './/span[@class="font-lg fw-600"]').text.strip()
    details['RERA Number'] = project_element.find_element(By.XPATH, './/a[@title="View Application"]').text.strip()
    details['Type'] = project_element.find_elements(By.TAG_NAME, 'span')[2].text.strip()
    contact_info = project_element.find_elements(By.CSS_SELECTOR, '.mt-1 span')
    details['Contact'] = contact_info[0].text.strip()
    details['Email'] = contact_info[1].text.strip()
    details['Address'] = contact_info[2].text.strip()
    details['Validity'] = project_element.find_element(By.CSS_SELECTOR, '.text-orange').text.strip()

    return details

project_elements = driver.find_elements(By.XPATH, '//div[@class="shadow py-3 px-3 font-sm radius-3 mb-2"]')

if not project_elements:
    print("No project elements found.")
else:
    print(f"Found {len(project_elements)} project elements.")

projects = []
for project_element in project_elements[:6]:
    details = extract_project_details(project_element)
    projects.append(details)

for i, project in enumerate(projects, start=1):
    print(f"Project {i}:")
    print(f"Project Name: {project['Project Name']}")
    print(f"RERA Number: {project['RERA Number']}")
    print(f"Type: {project['Type']}")
    print(f"Contact: {project['Contact']}")
    print(f"Email: {project['Email']}")
    print(f"Address: {project['Address']}")
    print(f"Validity: {project['Validity']}")
    print('-' * 40)

driver.quit()
