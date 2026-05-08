# 楔形文字（メソポタミア文明）のサンプル
# 1. AN（神・空）：最も有名な文字の一つ
# 2. KA（口）
# 3. MUSH（蛇）

an = "\U0001202D"
ka = "\U00012157"
mush = "\U00012232"

print("--- メソポタミアの文字 ---")
print(f"神/空 (AN): {an}")
print(f"口 (KA)   : {ka}")
print(f"蛇 (MUSH) : {mush}")

# 文章のように並べてみる
phrase = f"{an}{ka}{mush}"
print(f"\n並べたもの: {phrase}")

# Unicode番号を調べる（逆引き）
for char in phrase:
    print(f"文字: {char} -> Unicode: {hex(ord(char))}")