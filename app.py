from config import STORE_NAME, STORE_URL
from database.db import create_database, save_report_links, count_report_links
from scraper.minrepo import MinRepoClient


def main():
    print("=" * 40)
    print(STORE_NAME)
    print("スロット分析ツール")
    print("=" * 40)

    create_database()

    client = MinRepoClient()
    reports = client.get_report_links(STORE_URL)

    saved_count = save_report_links(reports)
    total_count = count_report_links()

    print(f"取得した営業日URL: {len(reports)}件")
    print(f"新規保存: {saved_count}件")
    print(f"DB内の営業日URL合計: {total_count}件")


if __name__ == "__main__":
    main()