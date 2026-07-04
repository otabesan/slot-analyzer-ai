from pathlib import Path

# プロジェクトのルート
BASE_DIR = Path(__file__).resolve().parent

# 保存先
DATA_DIR = BASE_DIR / "data"
DB_DIR = BASE_DIR / "db"
OUTPUT_DIR = BASE_DIR / "output"

# 店舗
STORE_NAME = "エスパス日拓新宿歌舞伎町店"

# みんレポ店舗ページ
STORE_URL = "https://min-repo.com/tag/エスパス日拓新宿歌舞伎町店/"

# User-Agent
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
