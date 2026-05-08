import webbrowser
import os

# 表示したいデータのリスト（文字, 名前, 意味）
data = [
    ("\U00013000", "ヒエログリフ: 鷲", "エジプトのAの音"),
    ("\U00013080", "ヒエログリフ: ひよこ", "エジプトのWの音"),
    ("\U0001202D", "楔形文字: AN", "シュメールの『神・空』"),
    ("\U00012157", "楔形文字: KA", "シュメールの『口』"),
    ("\U0001F40D", "絵文字: 蛇", "現代のUnicode文字")
]

# HTMLの組み立て（Pythonのf文字列を使うと楽！）
html_parts = []
for char, name, meaning in data:
    html_parts.append(f"""
        <div class="card">
            <div class="char">{char}</div>
            <div class="info">
                <h3>{name}</h3>
                <p>{meaning}</p>
            </div>
        </div>
    """)

cards_html = "".join(html_parts)

# 全体のテンプレート
full_html = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>古代文字図鑑</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; padding: 20px; }}
        h1 {{ text-align: center; color: #2c3e50; }}
        .container {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; }}
        .card {{ background: white; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 250px; padding: 20px; text-align: center; transition: transform 0.2s; }}
        .card:hover {{ transform: translateY(-5px); }}
        .char {{ font-size: 80px; margin-bottom: 10px; color: #2980b9; }}
        .info h3 {{ margin: 0; color: #34495e; }}
        .info p {{ color: #7f8c8d; font-size: 0.9em; }}
    </style>
</head>
<body>
    <h1>Python生成：古代文字デジタル図鑑</h1>
    <div class="container">
        {cards_html}
    </div>
</body>
</html>
"""

# ファイル書き出し
file_path = "zukan.html"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(full_html)

# ブラウザで表示
webbrowser.open('file://' + os.path.realpath(file_path))