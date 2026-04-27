# ウィンドウ付き！QRコード作成アプリ (Tkinter版)

import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk # 準備で入れた[pil]を使います

def generate_qr():
    link = entry.get()
    if not link:
        messagebox.showwarning("注意", "URLを入力してください")
        return

    # QRコード作成
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)
   # fill_colorでドットの色、back_colorで背景色を変えられます
   # img = qr.make_image(fill_color="darkblue", back_color="lightyellow")
    img = qr.make_image(fill_color="black", back_color="white")


    # 保存
    img.save("generated_qr.png")
    
    # 画面に表示するために変換
    img_tk = ImageTk.PhotoImage(img.resize((200, 200)))
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    messagebox.showinfo("完了", "QRコードを作成・保存しました！")

# GUI設定
root = tk.Tk()
root.title("爆速QRメーカー")
root.geometry("300x400")

tk.Label(root, text="URLを入力してください:").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
entry.insert(0, "https://")

btn = tk.Button(root, text="QRコード生成", command=generate_qr, bg="lightgray")
btn.pack(pady=20)

# QRコード表示用ラベル
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()