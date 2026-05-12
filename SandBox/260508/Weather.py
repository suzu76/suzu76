import requests
import webbrowser
import os
from datetime import datetime

# 1. 気象データをAPIから取得（東京・千代田区付近の座標）
url = "https://api.open-meteo.com/v1/forecast?latitude=35.4437&longitude=139.6380&current=temperature_2m,relative_humidity_2m,weather_code&timezone=Asia%2FTokyo"

# verify=False を追加して、セキュリティチェックをスキップします
# 同時に警告が出ないように設定を追加します
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ここを修正
response = requests.get(url, verify=False)

data = response.json()

# 現在の数値を取得
temp = data['current']['temperature_2m']
humidity = data['current']['relative_humidity_2m']
code = data['current']['weather_code']
time_str = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

# 天気コードを文字とアイコンに変換（簡易版）
weather_map = {0: "☀️ 快晴", 1: "🌤 晴れ", 2: "⛅ 曇り", 3: "☁️ どんより曇り", 45: "🌫 霧", 51: "🌧 小雨", 61: "☔ 雨"}
weather_text = weather_map.get(code, "🌈 不明/その他")

# 2. HTMLの組み立て
html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>お天気ダッシュボード</title>
    <style>
        body {{ font-family: 'Helvetica Neue', Arial, sans-serif; background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%); display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
        .weather-card {{ background: rgba(255, 255, 255, 0.9); padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center; width: 300px; }}
        .city {{ font-size: 1.2em; color: #666; }}
        .weather-icon {{ font-size: 80px; margin: 20px 0; }}
        .temp {{ font-size: 48px; font-weight: bold; color: #333; }}
        .unit {{ font-size: 20px; }}
        .detail {{ margin-top: 20px; color: #888; font-size: 0.9em; }}
        .update {{ font-size: 0.7em; color: #bbb; margin-top: 10px; }}
    </style>
</head>
<body>
    <div class="weather-card">
        <div class="city">Yokohama</div>
        <div class="weather-icon">{weather_text.split()[0]}</div>
        <div class="weather-text" style="font-size: 20px; color: #444;">{weather_text.split()[1]}</div>
        <div class="temp">{temp}<span class="unit">°C</span></div>
        <div class="detail">湿度: {humidity}%</div>
        <div class="update">最終更新: {time_str}</div>
    </div>
</body>
</html>
"""

# --- 保存場所の設定 ---
# フォルダパスを r"..." で囲むことで、バックスラッシュ（\）をそのまま扱えます
SAVE_DIR = r"C:\Users\7004141\OneDrive - Panasonic\作業用\Git-Work\suzu76\SandBox\temp@"
file_path = os.path.join(SAVE_DIR, "weather.html")

# フォルダが存在しない場合に備えて作成（念のため）
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# ファイル保存
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✨ ファイルを保存しました: {file_path}")

# ブラウザ起動
# ブラウザで開く際はパスを絶対パス（realpath）に変換して渡します
webbrowser.open('file://' + os.path.realpath(file_path))
