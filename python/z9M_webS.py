import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

job_cards = soup.find_all("div", class_="card-content")  # Update this line to find all job cards

for job_element in job_cards:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    # Check if any of the elements is None before accessing text
    if title_element and company_element and location_element:
        print("Title:", title_element.text.strip())
        print("Company:", company_element.text.strip())
        print("Location:", location_element.text.strip())
        print()