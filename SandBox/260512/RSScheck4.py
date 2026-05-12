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

# --- 設定項目 ---
# 保存場所をここで一括管理します
SAVE_DIR = r"C:\Users\7004141\OneDrive - Panasonic\作業用\Git-Work\suzu76\SandBox\temp@"
HISTORY_JSON_PATH = os.path.join(SAVE_DIR, "news_history.json")

RETENTION_DAYS = 30  # 何日分の履歴を保持するか
SOURCES = {
    "Car Watch": "http://car.watch.impress.co.jp/docs/car.rdf",
}
KEYWORDS = ["AI", "車載", "自動車"]

def load_history(filepath):
    """指定されたパスのJSONファイルから履歴を読み込み、古いデータを掃除する"""
    if not os.path.exists(filepath):
        return {}

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            history = json.load(f)
    except Exception:
        return {}

    # ★掃除機能：指定日数より古いエントリを削除
    cutoff_date = datetime.now() - timedelta(days=RETENTION_DAYS)
    
    # ISO形式の文字列を比較してフィルタリング
    cleaned_history = {
        url: info for url, info in history.items()
        if datetime.fromisoformat(info['date']) > cutoff_date
    }
    
    return cleaned_history

def save_history(history, filepath):
    """履歴全体をJSONファイルに指定されたパスへ保存する"""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

def professional_patrol():
    # フォルダが存在しない場合に備えて作成
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR, exist_ok=True)

    print(f"🧹 履歴（{RETENTION_DAYS}日分）を整理して巡回開始...")
    
    # load_historyにパスを渡して呼び出し
    history = load_history(HISTORY_JSON_PATH)
    found_new = False

    for site_name, url in SOURCES.items():
        try:
            print(f"📡 {site_name} をチェック中...")
            response = requests.get(url, verify=False, timeout=10)
            feed = feedparser.parse(io.BytesIO(response.content))

            for entry in feed.entries:
                # 既読チェック
                if entry.link in history:
                    continue
                
                # キーワードチェック
                if any(word.lower() in entry.title.lower() for word in KEYWORDS):
                    print(f"   🆕 新着! [{site_name}]: {entry.title}")
                    toast(f"【{site_name}】", entry.title, on_click=entry.link)
                    
                    # 履歴に追加
                    history[entry.link] = {
                        "title": entry.title,
                        "site": site_name,
                        "date": datetime.now().isoformat()
                    }
                    found_new = True

        except Exception as e:
            print(f"   ❌ {site_name} 失敗: {e}")

    # 保存処理
    if found_new:
        # save_historyにパスを渡して呼び出し
        save_history(history, HISTORY_JSON_PATH)
        print(f"✨ 履歴を更新しました: {HISTORY_JSON_PATH}")
    else:
        print("☕ 新しいキーワードを含むニュースはありませんでした。")

if __name__ == "__main__":
    professional_patrol()