import pyautogui
import sys

print("Ctrl+C で終了します。マウスの現在の座標を表示し続けます。")

try:
    while True:
        # 現在の座標を取得
        x, y = pyautogui.position()
        # 画面を書き換えて表示（末尾に '\r' をつけるのがコツ）
        print(f"X: {str(x).rjust(4)} Y: {str(y).rjust(4)}", end="\r")
except KeyboardInterrupt:
    print("\n終了しました。")