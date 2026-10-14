import os
import cv2
import sys
import math
import glob
import numpy as np
import Gpy

from tkinter import filedialog
from PIL import Image,ImageTk

import My_math as m
from Gpy import * 

def main():
    
    def reput():
        root.destroy()
    def QQ():
        root.destroy()
        sys.exit("exit !")
    
    while(1):
        root = Tk()
        root.title("Final_project")
        root.geometry('100x100')
        

        img_X_text = filedialog.askopenfilename(title=u'選擇圖檔1',initialdir=(os.path.expanduser('./data/')))
        if not img_X_text:
            sys.exit("cancel !")
        img_Y_text = filedialog.askopenfilename(title=u'選擇圖檔2',initialdir=(os.path.expanduser('./data/')))

        #Path names need to used English
        print("img_X_text",img_X_text)
        print("img_Y_text",img_Y_text)
        img_X= cv2.imread(img_X_text,0)
        
        img_Y= cv2.imread(img_Y_text,0)       
        
        if img_X.shape != img_Y.shape:
            print("img_X.shape",img_X.shape)
            print("img_Y.shape",img_Y.shape)
            

            root.geometry('700x300')
            G = error_GUI(root,img_X.shape,img_Y.shape)
            G.grid(row =0, column =0,sticky="nsew")
            root.mainloop()

            continue

            
        img_Z= np.zeros(img_X.shape, np.uint8)
        img_Zr= np.zeros(img_X.shape, np.uint8)
        
        for r in range(len(img_Z[0])):
            for c in range(len(img_Z[1])):
                X=m.int_to_binary(img_X[r,c])
                Y=m.int_to_binary(img_Y[r,c])
                Z=m.combine(X,Y)
                img_Z[r][c]= m.binary_to_int(Z)
                img_Zr[r][c]= m.binary_to_int(m.reverse(Z))
                # print(Z)
                # print(img_Z[r][c])
        
        set_psize=(512,512) 
        cv2.imwrite("./result_img/img_X.BMP", cv2.resize(img_X,set_psize,interpolation=cv2.INTER_AREA))
        cv2.imwrite("./result_img/img_Y.BMP", cv2.resize(img_Y,set_psize,interpolation=cv2.INTER_AREA))
        cv2.imwrite("./result_img/img_Z.BMP", cv2.resize(img_Z,set_psize,interpolation=cv2.INTER_AREA))
        cv2.imwrite("./result_img/img_Zr.BMP", cv2.resize(img_Zr,set_psize,interpolation=cv2.INTER_AREA))
        

        root.geometry('1500x900')
        Gm = GUI_img(root)
        Gm.grid(row =0, column =0,sticky="nsew")
        Gb = GUI_button(root)
        Gb.grid(row =0, column =1,sticky="nsew")

        root.mainloop()


if __name__ == "__main__":
    main()
        