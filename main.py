import csv
import requests
from bs4 import BeautifulSoup

url = "https://apps.ualberta.ca/catalogue"
response = requests.get(url)
faculty_urls = []
# Ensure the request was successful
if response.status_code == 200:
    main_page_soup = BeautifulSoup(response.text, 'html.parser')
    ul_tags = main_page_soup.find_all('ul')
    for i in ul_tags:
        if "Faculty of" in i.get_text():
                faculty_links = i
                break
    for li in faculty_links.find_all('li'):
         a_tag = li.find('a')
         if a_tag and a_tag.has_attr('href'):
              faculty_urls.append((requests.compat.urljoin(url, a_tag['href'])))
    

else:
    print("Failed to retrieve the webpage")
    exit()
departmenturls = []
for faculties in faculty_urls:
    AH_soup = BeautifulSoup((requests.get(faculties)).text,'html.parser')
    ul_tags = AH_soup.find_all('ul')
    departmentlinks = ul_tags[-1]
    
    for li in departmentlinks.find_all('li'):
            a_tag = li.find('a')
            if a_tag and a_tag.has_attr('href'):
                departmenturls.append((requests.compat.urljoin(url, a_tag['href'])))
filename = "departmenturls.csv"
with open(filename, 'w', newline='') as file:
    # Create a writer object from csv module
    csv_writer = csv.writer(file)
    
    # Write a header if needed
    csv_writer.writerow(['Department Links'])
    
    # Write links to the csv file, each link in a new row
    for link in departmenturls:
        csv_writer.writerow([link])