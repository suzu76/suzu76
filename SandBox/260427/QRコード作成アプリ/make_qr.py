import qrcode

# QRコードにしたい情報（URLやテキスト）
data = "https://github.com/suzu76"

# QRコードの作成
img = qrcode.make(data)

# 画像ファイルとして保存
img.save("my_github_qr.png")

print("QRコードを作成しました！フォルダを確認してください。")