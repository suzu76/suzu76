# ヒエログリフを変数に入れてみる
hieroglyphs = "\U00013000 \U00013080 \U00013193" # 鷲、ひよこ、目

print(f"古代エジプトの文字: {hieroglyphs}")

# 1文字ずつコードポイントを確認
for char in hieroglyphs.split():
    print(f"文字: {char}  Unicode番号: {hex(ord(char))}")