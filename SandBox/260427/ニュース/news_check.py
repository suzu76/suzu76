import requests
from bs4 import BeautifulSoup
import urllib3

# SSL警告を非表示にする（これを書かないと画面が警告だらけになります）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. サイトのデータを取ってくる（verify=False を追加！）
url = "https://www.yahoo.co.jp/"
response = requests.get(url, verify=False)

# 2. 解析の準備（HTMLのスープを作るイメージ）
soup = BeautifulSoup(response.text, "html.parser")

# 3. 特定の場所（ニュースの見出し）を探す
# Yahooのトップページの見出しは <a> タグの中に隠れています
print("--- 本日の主要ニュース ---")
articles = soup.find_all("a")

count = 0
for article in articles:
    # ニュースのリンクっぽいテキストだけを抽出（マニアックな判別）
    title = article.text
    # 長さや特定の条件で見出しを絞り込む
    if 10 < len(title) < 40:
        print(f"{count+1}: {title}")
        count += 1
    if count >= 13: # 13件取れたら終了
        break