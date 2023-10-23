import requests
from bs4 import BeautifulSoup


class Scrape:
    def __init__(self):  # Fixed the typo here
        self.url = 'https://www.sslproxies.org/'

    def scrape(self):
        ips = []
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, 'html.parser')
        table_rows = soup.findAll('table')[0].findAll('tr')
        table_rows = table_rows[1:-1]
        for row in table_rows:
            cells = row.findAll('td')
            for cell in cells:
                cell = cell.get_text()
            ips.append(cells[0].text + ":" + cells[1].text)

            # ips.append(row.findAll('td')[0] + ":" + row.findAll('td')[1])
        return ips




