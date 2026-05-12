import feedparser
from win11toast import toast
import time

# 1. 取得したいニュースのRSS URL（Yahoo!ニュース IT・科学）
# RSS_URL = "https://news.yahoo.co.jp/rss/categories/it.xml"
RSS_URL = "http://car.watch.impress.co.jp/docs/car.rdf"

def check_news():
    print("ニュースをチェック中...")
    
    # RSSを読み込む
    feed = feedparser.parse(RSS_URL)
    
    # 最新の1件を取得
    if feed.entries:
        latest_entry = feed.entries[0]
        title = latest_entry.title
        link = latest_entry.link
        summary = latest_entry.summary

        # 2. Windowsのデスクトップ通知を出す
        # クリックするとブラウザで記事が開く設定にします
        toast(
            "最新ニュースが届きました！", 
            title,
            on_click=link  # 通知をクリックすると記事へ飛ぶ
        )
        print(f"通知を送信しました: {title}")

if __name__ == "__main__":
    # まずは1回実行
    check_news()
    
    # マニアの自動化：10分（600秒）ごとにチェックするループ
    # print("\n10分おきに自動チェックを開始します。停止するには Ctrl+C を押してください。")
    # while True:
    #     time.sleep(600)
    #     check_news()