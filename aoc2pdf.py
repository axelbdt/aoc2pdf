import io

import pdfkit
import pikepdf
import requests
from bs4 import BeautifulSoup
from pikepdf import Pdf

aoc_url_root = "https://adventofcode.com/"
year = 2021

aoc_year_url = f"{aoc_url_root}{year}/"

year_pdf = Pdf.new()

for day in range(1, 26):
    url = aoc_year_url + "day/" + str(day)

    html_start = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>AoC {year} {day}</title>
    </head>
    <body>
    """

    html_end = """
    </body>
    </html>
    """

    response = requests.get(url, timeout=3000)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        article = soup.find("article").prettify()
        full_html = html_start + article + html_end

        with pikepdf.open(io.BytesIO(pdfkit.from_string(full_html))) as day_pdf:
            year_pdf.pages.extend(day_pdf.pages)

filename = f"AoC {year}.pdf"
year_pdf.save(filename)
