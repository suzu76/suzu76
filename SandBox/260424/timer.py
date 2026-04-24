# 残り時間を教えてくれる「カウントダウンタイマー」

import time

seconds = int(input("何秒測りますか？："))

print("タイマー開始！")

while seconds > 0:
    print(f"残り {seconds} 秒...", end="\r") # 同じ行に上書き表示するテクニック
    time.sleep(1) # 1秒待つ
    seconds -= 1

print("\n時間です！ 終了！")
# Windowsの場合、これで「ピッ」という音が鳴ります
import winsound
winsound.Beep(1000, 500)