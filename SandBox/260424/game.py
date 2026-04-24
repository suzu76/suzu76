# 数字当てゲーム（数当てクイズ）

import random

# 1から10の間でランダムな数字を決める
answer = random.randint(1, 10)

print("1から10の中で、僕が考えた数字は何かな？")

# 正解するまで繰り返す
while True:
    guess = int(input("予想を入力してね："))
    
    if guess == answer:
        print("大正解！おめでとう！")
        break # ループを終了
    elif guess < answer:
        print("もっと大きい数字だよ。")
    else:
        print("もっと小さい数字だよ。")