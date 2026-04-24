# 強力なパスワードを自動で作る「パスワード生成器」

import random
import string

print("--- ランダムパスワード生成器 ---")

# 使いたい文字の種類をまとめる（英字＋数字＋記号）
chars = string.ascii_letters + string.digits + string.punctuation

# 12桁のパスワードを作る
length = 12
password = "".join(random.sample(chars, length))

print(f"生成されたパスワード： {password}")
print("※安全な場所にメモしておきましょう！")