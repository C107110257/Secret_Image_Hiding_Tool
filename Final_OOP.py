import sys
import tkinter as tk
from tkinter import filedialog

import cv2

import My_math as m
from Gpy import GUI_img, GUI_button, error_GUI


def pick_image(title):
    path = filedialog.askopenfilename(title=title, initialdir="./data/")
    if not path:
        sys.exit("cancel !")
    img = cv2.imread(path, 0)
    if img is None:
        sys.exit(f"無法讀取圖片:{path}(路徑請避免中文)")
    return img


def main():
    while True:
        root = tk.Tk()
        root.title("影像藏密與還原")
        root.geometry("100x100")

        img_X = pick_image("選擇載體圖 (X)")
        img_Y = pick_image("選擇秘密圖 (Y)")

        if img_X.shape != img_Y.shape:
            root.geometry("900x350")
            error_GUI(root, img_X.shape, img_Y.shape).grid(row=0, column=0, sticky="nsew")
            root.mainloop()
            continue

        img_Z = m.combine(img_X, img_Y)
        img_Zr = m.reverse(img_Z)
        images = {"X": img_X, "Y": img_Y, "Z": img_Z, "Zr": img_Zr}

        root.geometry("1500x900")
        GUI_img(root, images).grid(row=0, column=0, sticky="nsew")
        Gb = GUI_button(root, images)
        Gb.grid(row=0, column=1, sticky="nsew")
        root.mainloop()

        if Gb.quit_app:
            break


if __name__ == "__main__":
    main()