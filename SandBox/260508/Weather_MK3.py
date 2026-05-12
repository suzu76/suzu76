import requests
import webbrowser
import os
import urllib3
from datetime import datetime

# セキュリティチェック回避の設定
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_colorful_weather():
    location_name = input("天気を知りたい地名を入力してください: ")

    # 1. 地名を座標に変換
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location_name}&count=1&language=ja&format=json"
    geo_res = requests.get(geo_url, verify=False).json()

    if not geo_res.get('results'):
        print("場所が見つかりませんでした。")
        return

    result = geo_res['results'][0]
    lat = result['latitude']
    lon = result['longitude']
    display_name = result.get('name', location_name)

    # 2. 天気を取得
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code&timezone=Asia%2FTokyo"
    w_res = requests.get(weather_url, verify=False).json()
    temp = w_res['current']['temperature_2m']
    code = w_res['current']['weather_code']

    # ★マニアのこだわり：天気コードから「アイコン」と「色」のセットを決める
    # (Font Awesomeのクラス名と、CSSの色を指定)
    icon_map = {
        0:  ("fa-sun", "#FFD700", "快晴"),          # 金色
        1:  ("fa-cloud-sun", "#FFA500", "晴れ"),     # オレンジ
        2:  ("fa-cloud", "#BDC3C7", "曇り"),        # シルバーグレー
        3:  ("fa-cloud", "#7F8C8D", "どんより"),     # 濃いグレー
        45: ("fa-smog", "#95A5A6", "霧"),           # 霧色
        51: ("fa-cloud-showers-heavy", "#3498DB", "小雨"), # 青
        61: ("fa-cloud-primary-showers", "#2980B9", "雨"), # 濃い青
    }
    
    # マップになければデフォルト（虹色）
    icon_class, icon_color, weather_text = icon_map.get(code, ("fa-rainbow", "#9B59B6", "不明"))

    # 3. HTMLを生成（Font Awesomeを読み込む）
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #ecf0f1; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .weather-card {{ background: white; padding: 50px; border-radius: 25px; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.1); width: 350px; transition: all 0.3s; }}
            .weather-card:hover {{ transform: scale(1.02); }}
            
            /* ★アイコンのスタイル（ここが本番！） */
            .main-icon {{ 
                font-size: 120px;          /* ★サイズをめちゃくちゃ大きく */
                color: {icon_color};       /* ★Pythonから渡された色を適用 */
                margin-bottom: 20px;
                filter: drop-shadow(0 5px 10px rgba(0,0,0,0.1)); /* 少し影をつけて高級感を */
            }}
            
            .temp {{ font-size: 4em; font-weight: bold; color: #333; margin: 10px 0; }}
            .location {{ color: #7f8c8d; font-size: 1.2em; }}
            .text {{ font-size: 1.5em; color: {icon_color}; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="weather-card">
            <div class="location"><i class="fa-solid fa-location-dot"></i> {display_name}</div>
            
            <i class="fa-solid {icon_class} main-icon"></i>
            
            <div class="text">{weather_text}</div>
            <div class="temp">{temp}<span style="font-size: 0.5em;">°C</span></div>
        </div>
    </body>
    </html>
    """

    SAVE_DIR = r"C:\Users\7004141\OneDrive - Panasonic\作業用\Git-Work\suzu76\SandBox\temp@"
    file_path = os.path.join(SAVE_DIR, "colorful_weather.html")

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

if __name__ == "__main__":
    get_colorful_weather()