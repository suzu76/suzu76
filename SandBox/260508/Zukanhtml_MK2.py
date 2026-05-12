import webbrowser
import os

# 表示したい古代文字のリスト
chars = ["\U00013000", "\U00013080", "\U0001202D", "\U00012157", "\U0001F40D"]
labels = ["鷲", "ひよこ", "神/空", "口", "蛇"]

html_parts = []

# Pythonで各文字の情報を「計算」してHTMLを生成
for char, label in zip(chars, labels):
    code_hex = hex(ord(char)).upper()  # 16進数に変換 (例: 0x13000)
    code_dec = ord(char)               # 10進数（コンピュータ内の生データ）
    
    html_parts.append(f"""
        <div class="card">
            <div class="char">{char}</div>
            <div class="info">
                <h3>{label}</h3>
                <hr>
                <p><strong>Unicode:</strong> {code_hex}</p>
                <p><strong>Decimal:</strong> {code_dec}</p>
                <div class="status-bar">
                    <div class="fill" style="width: {code_dec % 100}%"></div>
                </div>
            </div>
        </div>
    """)

cards_html = "".join(html_parts)

# HTMLテンプレート（少しデザインを「ダッシュボード風」に強化）
full_html = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>古代文字データセンター</title>
    <style>
        body {{ font-family: 'Consolas', 'Courier New', monospace; background-color: #1a1a1a; color: #e0e0e0; padding: 20px; }}
        h1 {{ text-align: center; color: #00d4ff; border-bottom: 2px solid #00d4ff; padding-bottom: 10px; }}
        .container {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; }}
        .card {{ background: #2d2d2d; border: 1px solid #444; border-radius: 8px; width: 220px; padding: 15px; }}
        .char {{ font-size: 70px; background: #3d3d3d; border-radius: 5px; margin-bottom: 10px; }}
        .info h3 {{ color: #00d4ff; margin: 5px 0; }}
        .info p {{ font-size: 12px; margin: 5px 0; color: #bbb; }}
        hr {{ border: 0.5px solid #444; }}
        .status-bar {{ background: #111; height: 5px; border-radius: 10px; margin-top: 10px; }}
        .fill {{ background: #00d4ff; height: 100%; border-radius: 10px; }}
    </style>
</head>
<body>
    <h1>ANCIENT CHAR DATA ANALYSIS</h1>
    <div class="container">
        {cards_html}
    </div>
</body>
</html>
"""

# --- 保存場所の設定 ---
# フォルダパスを r"..." で囲むことで、バックスラッシュ（\）をそのまま扱えます
SAVE_DIR = r"C:\Users\7004141\OneDrive - Panasonic\作業用\Git-Work\suzu76\SandBox\temp@"
file_path = os.path.join(SAVE_DIR, "data_zukan.html")

# フォルダが存在しない場合に備えて作成（念のため）
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# ファイル保存
with open(file_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"✨ ファイルを保存しました: {file_path}")

# ブラウザ起動
# ブラウザで開く際はパスを絶対パス（realpath）に変換して渡します
webbrowser.open('file://' + os.path.realpath(file_path))