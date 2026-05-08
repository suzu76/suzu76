import requests
import webbrowser
import os
import urllib3
from datetime import datetime

# セキュリティチェック回避の設定
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_weather_by_location():
    location_name = input("天気を知りたい地名を入力してください（例：横浜）: ")

    # 1. 地名を座標（緯度・経度）に変換するAPI
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location_name}&count=1&language=ja&format=json"
    geo_res = requests.get(geo_url, verify=False).json()

    if not geo_res.get('results'):
        print("場所が見つかりませんでした。")
        return

    # 座標を取得
    result = geo_res['results'][0]
    lat = result['latitude']
    lon = result['longitude']
    display_name = result.get('name', location_name)

    # 2. その座標の天気を取得
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,weather_code&timezone=Asia%2FTokyo"
    w_res = requests.get(weather_url, verify=False).json()

    temp = w_res['current']['temperature_2m']
    humidity = w_res['current']['relative_humidity_2m']
    code = w_res['current']['weather_code']
    time_str = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    weather_map = {0: "☀️ 快晴", 1: "🌤 晴れ", 2: "⛅ 曇り", 3: "☁️ どんより", 45: "🌫 霧", 51: "🌧 小雨", 61: "☔ 雨"}
    weather_text = weather_map.get(code, "🌈 不明")

    # 3. HTMLを生成して表示
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: sans-serif; background: #2c3e50; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .card {{ background: #34495e; padding: 30px; border-radius: 15px; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.3); }}
            .temp {{ font-size: 3em; font-weight: bold; color: #3498db; }}
            .info {{ margin-top: 10px; font-size: 1.2em; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>{display_name} の現在の天気</h2>
            <div class="temp">{temp}°C</div>
            <div class="info">{weather_text}</div>
            <p>湿度: {humidity}%</p>
            <p style="font-size: 0.7em; color: #95a5a6;">更新: {time_str}</p>
        </div>
    </body>
    </html>
    """

    file_path = "dynamic_weather.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    webbrowser.open('file://' + os.path.realpath(file_path))

if __name__ == "__main__":
    get_weather_by_location()