import tkinter as tk
import pyperclip
import pyautogui
import time

def paste_phrase(phrase):
    # 1. クリップボードにコピー
    pyperclip.copy(phrase)
    
    # 2. ほんの少し待つ（ウィンドウが切り替わる余裕を作る）
    time.sleep(3)
    
    # 3. Ctrl + V を実行して貼り付け！
    pyautogui.hotkey('ctrl', 'v')

# 定型文のリスト（ここを自由に書き換えてください！）
PHRASES = {
    "出社": "出社しました",
    "在宅": "在宅勤務開始します。",
    "勤務終了": "勤務終了します。",
}

# --- GUI ---
root = tk.Tk()
root.title("爆速ランチャー")
root.geometry("200x300")
root.attributes("-topmost", True) # 常に最前面に表示

tk.Label(root, text="クリックして貼り付け", font=("MS Gothic", 10)).pack(pady=10)

for label, text in PHRASES.items():
    # ボタンを作るときに、lambdaを使って引数を渡すのがコツです
    btn = tk.Button(root, text=label, width=20, 
                    command=lambda t=text: paste_phrase(t))
    btn.pack(pady=5)

root.mainloop()