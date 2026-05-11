import feedparser
from win11toast import toast
import urllib3
import requests
import io
import os

# セキュリティ回避
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HISTORY_FILE = "history.txt"
SOURCES = {
    "Yahoo IT": "https://news.yahoo.co.jp/rss/categories/it.xml",
    "Car Watch": "http://car.watch.impress.co.jp/docs/car.rdf",
}
KEYWORDS = ["AI", "車載", "自動車"]

def load_history():
    """過去に通知したURLをファイルから読み込む"""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f)
    return set()

def save_history(url):
    """新しいURLをファイルに追記する"""
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(url + "\n")

def smarter_patrol():
    print("🧠 記憶機能付き・巡回魔法、発動！")
    history = load_history()
    found_count = 0

    for site_name, url in SOURCES.items():
        try:
            response = requests.get(url, verify=False, timeout=10)
            feed = feedparser.parse(io.BytesIO(response.content))

            for entry in feed.entries:
                # 1. 既読チェック（すでに記憶にあるURLならスキップ）
                if entry.link in history:
                    continue
                
                # 2. キーワードチェック
                if any(word.lower() in entry.title.lower() for word in KEYWORDS):
                    print(f"   🆕 新着ヒット! [{site_name}]: {entry.title}")
                    
                    toast(f"【新着】{site_name}", entry.title, on_click=entry.link)
                    
                    # 3. 記憶に刻む
                    save_history(entry.link)
                    history.add(entry.link) # 今回の実行用にも追加
                    found_count += 1
                    break 

        except Exception as e:
            print(f"   ❌ {site_name} 失敗: {e}")

    if found_count == 0:
        print("☕ 新しいニュースはありませんでした。")

if __name__ == "__main__":
    smarter_patrol()