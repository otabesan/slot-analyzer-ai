import requests
from bs4 import BeautifulSoup

URL = "https://min-repo.com/tag/エスパス日拓新宿歌舞伎町店/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers, timeout=20)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "lxml")

print(soup.title.text)
