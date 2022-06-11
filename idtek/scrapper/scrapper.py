import requests
from bs4 import BeautifulSoup

# Poatek team page
URL = "https://poatek.com/our-team"

# Retrieve Poatek Team page data using requests
try:
    page = requests.get(URL)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

# Retrieve the page html data with Beautiful Soup
soup = BeautifulSoup(page.content, "html.parser")

# Get the Data from the div with all the contributors
contributors = soup.find_all("div", {"class": "team team_vertical"})

for contributor in contributors:
    try:
        contributor_name = contributor.find("h4", class_='').contents[0]
    except IndexError as e:
        print(e)
        print("\nContributor name not found inside div")
        break
    
    try:
        contributor_img_url = contributor.findAll("img")[0]['src']
    except IndexError as e:
        print(f"\nCouldn't find {contributor_name}'s img file")
    except KeyError as e:
        print(f"\nCouldn't find {contributor_name}'s image src url")
        
    
    print(f"\n{contributor_name}: {contributor_img_url}")