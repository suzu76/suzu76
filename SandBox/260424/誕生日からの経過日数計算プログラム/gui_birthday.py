# ウィンドウ版：誕生日計算プログラム

import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate():
    try:
        # 入力欄から数字を取得
        y = int(entry_y.get())
        m = int(entry_m.get())
        d = int(entry_d.get())
        
        # 計算ロジック
        birthday = date(y, m, d)
        today = date.today()
        delta = today - birthday
        
        # メッセージボックスで結果を表示
        messagebox.showinfo("結果", f"今日は：{today}\nあなたは生まれてから今日で\n【 {delta.days} 日目 】です！")
    except ValueError:
        messagebox.showerror("エラー", "数字を正しく入力してください。")

# --- 画面の作成 ---
root = tk.Tk()
root.title("誕生日カウンター🎂")
root.geometry("300x250")

# ラベルと入力欄（年）
tk.Label(root, text="生まれた年 (西暦):").pack(pady=5)
entry_y = tk.Entry(root)
entry_y.pack()

# ラベルと入力欄（月）
tk.Label(root, text="生まれた月:").pack(pady=5)
entry_m = tk.Entry(root)
entry_m.pack()

# ラベルと入力欄（日）
tk.Label(root, text="生まれた日:").pack(pady=5)
entry_d = tk.Entry(root)
entry_d.pack()

# 計算ボタン
btn = tk.Button(root, text="計算する", command=calculate, bg="lightblue")
btn.pack(pady=20)

root.mainloop()