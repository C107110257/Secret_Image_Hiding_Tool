import tkinter as tk
from tkinter import N, S, E, W

from PIL import Image, ImageTk

import My_math as m

FONT = ("Microsoft JhengHei", 12)
FONT_BIG = ("Microsoft JhengHei", 24)

# 顯示名稱集中放這裡,要改名只改這一處
LABELS = {
    "X":  "載體圖 (X)",
    "Y":  "秘密圖 (Y)",
    "Z":  "藏密後影像 (Z)",
    "Zr": "還原影像 (Zr)",
}

# 每張圖在 grid 的位置: (標籤 row, column);圖片放在標籤下一列
LAYOUT = {
    "X":  (0, 0),
    "Y":  (0, 1),
    "Z":  (2, 0),
    "Zr": (2, 1),
}


class GUI_img(tk.Frame):
    """images: dict,key 為 X/Y/Z/Zr,value 為 numpy 灰階陣列"""

    def __init__(self, master, images):
        super().__init__(master)
        self.master = master
        self.grid(sticky=N + S + E + W)

        self.pil = {}      # 原始 PIL 圖
        self.tkimg = {}    # PhotoImage(要留著參考,否則會被回收)
        self.panels = {}   # 顯示圖片的 Label
        self._after_id = None

        for key, (row, col) in LAYOUT.items():
            tk.Label(self, text=LABELS[key], font=FONT).grid(
                row=row, column=col, sticky=N + S + E + W)

            self.pil[key] = Image.fromarray(images[key])
            self.tkimg[key] = ImageTk.PhotoImage(self.pil[key])
            panel = tk.Label(self, image=self.tkimg[key])
            panel.grid(row=row + 1, column=col, sticky="nsew")
            self.panels[key] = panel

        self.master.bind("<Configure>", self._on_configure)

    def _on_configure(self, event):
        # 子元件的 Configure 也會冒泡上來,只處理視窗本身
        if event.widget is not self.master:
            return
        # debounce:停止拖曳 100ms 後才重畫
        if self._after_id is not None:
            self.after_cancel(self._after_id)
        self._after_id = self.after(100, self._resize_images)

    def _resize_images(self):
        self._after_id = None
        w = max(int(self.master.winfo_width() / 3), 1)
        h = max(int(self.master.winfo_height() / 2.2), 1)
        for key, panel in self.panels.items():
            self.tkimg[key] = ImageTk.PhotoImage(self.pil[key].resize((w, h)))
            panel.configure(image=self.tkimg[key])


class GUI_button(tk.Frame):
    """用原始陣列計算 PSNR(不是 resize 後的圖)"""

    def __init__(self, master, images):
        super().__init__(master)
        self.master = master
        self.images = images
        self.quit_app = False

        self.e = tk.Entry(self, width=40, font=FONT)
        self.e.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky=N)

        self.b1 = tk.Button(
            self, text="PSNR:載體圖 vs 藏密後影像",
            command=lambda: self.show_psnr("X", "Z"),
            fg="red", bg="white", font=FONT)
        self.b1.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky=N + S + E + W)

        self.b2 = tk.Button(
            self, text="PSNR:秘密圖 vs 還原影像",
            command=lambda: self.show_psnr("Y", "Zr"),
            fg="blue", bg="white", font=FONT)
        self.b2.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky=N + S + E + W)

        self.b3 = tk.Button(self, text="重新選擇圖片", command=self.reselect, font=FONT)
        self.b3.grid(row=3, column=0, padx=10, pady=10, sticky=N + S + E + W)

        self.b4 = tk.Button(self, text="離開", command=self.exit_app, font=FONT)
        self.b4.grid(row=3, column=1, padx=10, pady=10, sticky=N + S + E + W)

    def show_psnr(self, a, b):
        value = m.psnr(self.images[a], self.images[b])
        self.set_text(f"PSNR({LABELS[a]} vs {LABELS[b]}) = {value:.2f} dB")

    def set_text(self, text):
        self.e.delete(0, tk.END)
        self.e.insert(0, text)

    def reselect(self):
        self.master.destroy()

    def exit_app(self):
        self.quit_app = True
        self.master.destroy()


class error_GUI(tk.Frame):
    def __init__(self, master, shape_x, shape_y):
        super().__init__(master)
        self.master = master

        msg = [
            f"載體圖 (X) 尺寸:{shape_x}",
            f"秘密圖 (Y) 尺寸:{shape_y}",
            "兩張圖尺寸不同,請重新選擇",
        ]
        for i, text in enumerate(msg):
            tk.Label(self, text=text, font=FONT_BIG).grid(
                row=i, column=0, sticky=N + S + E + W)

        tk.Button(self, text="確定", command=self.master.destroy, font=FONT_BIG).grid(
            row=3, column=0, padx=10, pady=10, sticky=N + S + E + W)