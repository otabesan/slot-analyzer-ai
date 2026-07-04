import requests
from bs4 import BeautifulSoup

URL = "https://min-repo.com/3206448/"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def clean(text):
    return text.replace("\n", "").replace("\t", "").strip()


res = requests.get(URL, headers=HEADERS, timeout=20)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

table = soup.find("table", class_="kishu")

rows = table.find_all("tr")

for row in rows[:30]:
    cols = [clean(c.get_text()) for c in row.find_all(["th", "td"])]
    print(cols)