import re
import time
from dataclasses import dataclass
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://min-repo.com"
STORE_URL = "https://min-repo.com/tag/エスパス日拓新宿歌舞伎町店/"

@dataclass
class ReportLink:
    date_text: str
    url: str

class MinRepoClient:
    def __init__(self, delay=2.0):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0"})
        self.delay = delay

    def get_soup(self, url):
        time.sleep(self.delay)
        res = self.session.get(url, timeout=20)
        res.raise_for_status()
        return BeautifulSoup(res.text, "lxml")

    def get_report_links(self, store_url):
        soup = self.get_soup(store_url)
        reports = []

        date_pattern = re.compile(r"^\d{1,2}/\d{1,2}\(.+\)$")
        url_pattern = re.compile(r"https://min-repo\.com/\d+/$")

        for a in soup.find_all("a", href=True):
            text = a.get_text(strip=True)
            full_url = urljoin(BASE_URL, a["href"])

            if date_pattern.match(text) and url_pattern.match(full_url):
                reports.append(ReportLink(text, full_url))

        return reports

if __name__ == "__main__":
    client = MinRepoClient()
    reports = client.get_report_links(STORE_URL)

    print(f"営業日URL数: {len(reports)}")
    for r in reports[:20]:
        print(r.date_text, r.url)