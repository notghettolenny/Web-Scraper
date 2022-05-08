from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib.parse import urljoin

job_list = "https://www.indeed.com/jobs?q=data+scientist&l=New+York&start=10"
job_urls = []

driver = webdriver.Chrome("C:/Users/lenny/Downloads/chromedriver_win32/chromedriver.exe") # change path to location of chromedriver on local device
driver.set_page_load_timeout(15)
driver.get(job_list)

job_soup = BeautifulSoup(driver.page_source, "html.parser")

job_tbl = job_soup.find(id = "resultsCol")

for link in job_tbl.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['turnstileLink']):
    job_url = urljoin(job_list, link.attrs['href'])
    job_urls.append(job_url)

for x in range(len(job_urls)):

    job_page = requests.get(job_urls[x])
    
    soup = BeautifulSoup(job_page.text, "html.parser")

    job_title = soup.find(class_='jobtitle').get_text()
    print("Title:", job_title)
    job_location = soup.find(class_='location').get_text()
    print("Location:", job_location)
    job_company = soup.find(class_='company').get_text()
    print("Company:", job_company)
    print("URL:", job_urls[x], "\n")
