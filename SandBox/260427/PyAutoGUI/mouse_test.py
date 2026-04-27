import pyautogui
import time

# 5秒間の猶予（この間に、クリックしたい場所を準備します）
print("5秒後にマウスが動きます。準備してください！")
time.sleep(5)

# 1. マウスを特定の座標（x, y）に移動させる
# 座標は画面の左上が (0, 0) です
pyautogui.moveTo(500, 500, duration=1) # 1秒かけて (500, 500) へ

# 2. 右クリック
pyautogui.click(button='left')

# 3. メッセージ入力（キーボード操作）
pyautogui.write("Hello, I am a Robot!", interval=0.1)