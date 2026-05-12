import feedparser
from win11toast import toast
import urllib3
import requests
import io
import os
import json
from datetime import datetime, timedelta

# セキュリティ回避
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HISTORY_JSON = "history.json"
RETENTION_DAYS = 30  # ★何日分の履歴を保持するか
SOURCES = {
    "Car Watch": "http://car.watch.impress.co.jp/docs/car.rdf",
}
KEYWORDS = ["AI", "車載", "自動車"]

def load_history():
    """JSONファイルから履歴を読み込み、古いデータを掃除する"""
    if not os.path.exists(HISTORY_JSON):
        return {}

    with open(HISTORY_JSON, "r", encoding="utf-8") as f:
        history = json.load(f)

    # ★掃除機能：指定日数より古いエントリを削除
    cutoff_date = datetime.now() - timedelta(days=RETENTION_DAYS)
    # 辞書の中身をフィルタリング
    cleaned_history = {
        url: info for url, info in history.items()
        if datetime.fromisoformat(info['date']) > cutoff_date
    }
    
    return cleaned_history

def save_history(history):
    """履歴全体をJSONファイルに保存する"""
    with open(HISTORY_JSON, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

def professional_patrol():
    print(f"🧹 履歴（{RETENTION_DAYS}日分）を整理して巡回開始...")
    history = load_history()
    found_new = False

    for site_name, url in SOURCES.items():
        try:
            response = requests.get(url, verify=False, timeout=10)
            feed = feedparser.parse(io.BytesIO(response.content))

            for entry in feed.entries:
                if entry.link in history:
                    continue
                
                if any(word.lower() in entry.title.lower() for word in KEYWORDS):
                    print(f"   🆕 新着! [{site_name}]: {entry.title}")
                    toast(f"【{site_name}】", entry.title, on_click=entry.link)
                    
                    # ★情報の構造化保存
                    history[entry.link] = {
                        "title": entry.title,
                        "site": site_name,
                        "date": datetime.now().isoformat() # ISO形式で日付を保存
                    }
                    found_new = True
                    break 

        except Exception as e:
            print(f"   ❌ {site_name} 失敗: {e}")

    if found_new:
        save_history(history)
    else:
        print("☕ 新しいニュースはありません。")

if __name__ == "__main__":
    professional_patrol()