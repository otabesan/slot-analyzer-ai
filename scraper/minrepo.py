import time
import requests
from bs4 import BeautifulSoup

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )
}


class MinRepoClient:
    def __init__(self, delay=2.0):
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        self.delay = delay

    def get(self, url: str):
        time.sleep(self.delay)

        response = self.session.get(
            url,
            timeout=20,
        )

        response.raise_for_status()

        return BeautifulSoup(response.text, "lxml")


if __name__ == "__main__":

    url = "https://min-repo.com/tag/エスパス日拓新宿歌舞伎町店/"

    client = MinRepoClient()

    soup = client.get(url)

    print(soup.title.text.strip())