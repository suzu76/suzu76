import feedparser
from win11toast import toast

# 1. 取得したいニュースのRSS
RSS_URL = "https://news.yahoo.co.jp/rss/categories/it.xml"

# 2. 魔法のフィルターリスト（ここに興味のある言葉を入れる）
KEYWORDS = ["AI", "車載", "自動車"]

def check_news_with_filter():
    feed = feedparser.parse(RSS_URL)
    
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        
        # 3. フィルタリング魔法！
        # タイトルの中にキーワードがどれか1つでも含まれているか？
        if any(word in title for word in KEYWORDS):
            print(f"★ヒットしました！: {title}")
            
            toast(
                "気になるニュースを発見！",
                title,
                on_click=link
            )
            # 1件見つかったら今回は終了（通知の乱舞を防ぐため）
            return 
    
    print("条件に合うニュースはありませんでした。")

if __name__ == "__main__":
    check_news_with_filter()