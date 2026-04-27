# 誕生日からの経過日数計算プログラム

from datetime import date

print("--- 生きた日数を数えるプログラム ---")

# 1. 誕生日を入力してもらう
year = int(input("生まれた年（西暦）を入力してください（例: 2000）："))
month = int(input("生まれた月を入力してください（例: 4）："))
day = int(input("生まれた日を入力してください（例: 24）："))

# 2. 日付オブジェクトを作成
birthday = date(year, month, day)
today = date.today() # 今日の日付を取得

# 3. 引き算をする（今日 - 誕生日）
delta = today - birthday

# 4. 結果を表示
print("-" * 30)
print(f"今日は：{today}")
print(f"あなたは生まれてから今日で【 {delta.days} 日目 】です！")
print("-" * 30)

if delta.days % 1000 == 0:
    print("おおっ！今日はちょうど1000日ごとの記念日ですね！")

# これを最後に追加！
input("エンターキーを押すと終了します...")