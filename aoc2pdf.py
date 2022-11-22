import requests
from bs4 import BeautifulSoup

aoc_url_root = "https://adventofcode.com/"
year = 2021

aoc_year_url = f"{aoc_url_root}{str(year)}/"

# for day in range(1, 26):
url = aoc_year_url + "day/" + str(1)

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup.prettify())
