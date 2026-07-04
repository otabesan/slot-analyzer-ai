from config import STORE_NAME
from database.db import create_database

print("=" * 40)
print(STORE_NAME)
print("スロット分析ツール")
print("=" * 40)

create_database()
