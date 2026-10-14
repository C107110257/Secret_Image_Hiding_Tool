import os
import cv2
import sys
import math
import glob
import numpy as np
import tkinter as tk

from tkinter import filedialog
from PIL import Image,ImageTk

N = 8
p_resize=(512,512)

def psnr(img1, img2):
   mse = np.mean( (img1/255. - img2/255.) ** 2 )
   if mse < 1.0e-10:
      return 100
   PIXEL_MAX = 1
   return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


def reverse(x):
    b= np.zeros((N,), dtype=int)
    for i in range(N):
        b[i]=x[N-i-1]
    return b

def combine(x,y):
    z= np.zeros((N,), dtype=int)
    for i in range(int(N/2)):
        z[i]=x[i]
        z[i+4]=y[3-i]
    return z
def int_to_binary(num):
    b= np.zeros((N,), dtype=int) 
    for i in range(N):          
        b[N-i-1]= num%2
        # b[i]= num%2
        num = num/2
    return b
def binary_to_int(b):
    n = 0
    for i in range(N):          
        n += b[i]*pow(2,N-i-1)
    return n
def main():
    def set_text(text):
        e.delete(0,tk.END)
        e.insert(0,text)
        return
    def reput():
        GUI.destroy()
    def QQ():
        GUI.destroy()
        sys.exit("exit !")
    
    while(1):
        GUI = tk.Tk()
        GUI.title("Final_project")
        GUI.geometry('1920x1080')
        img_X_text = filedialog.askopenfilename(title=u'選擇圖檔1',initialdir=(os.path.expanduser('./data/')))
        img_Y_text = filedialog.askopenfilename(title=u'選擇圖檔2',initialdir=(os.path.expanduser('./data/')))

        #Path names need to used English
        print("img_X_text",img_X_text)
        print("img_Y_text",img_Y_text)
        img_X= cv2.imread(img_X_text,0)
        
        img_Y= cv2.imread(img_Y_text,0)
        
        
        # img_Y= cv2.imread("./data/Jet.BMP",0)
        # img_Y= cv2.imread("./data/Jet_resize256.BMP",0)
        
        
        if img_X.shape != img_Y.shape:
            print("img_X.shape",img_X.shape)
            print("img_Y.shape",img_Y.shape)

            labelimg_x = tk.Label(GUI,text = "img_X.shape = " + str(img_X.shape), font = (("Times New Roman"),15))
            labelimg_x.grid(column=0, row=0, sticky=tk.W+tk.E+tk.N+tk.S)

            labelimg_Y = tk.Label(GUI,text = "img_Y.shape = " + str(img_Y.shape), font = (("Times New Roman"),15))
            labelimg_Y.grid(column=0, row=1, sticky=tk.W+tk.E+tk.N+tk.S)

            labelimg_text = tk.Label(GUI,text = "Please select two images of the same size !", font = (("Times New Roman"),15))
            labelimg_text.grid(column=0, row=2, sticky=tk.W+tk.E+tk.N+tk.S)

            b0 = tk.Button(GUI, text = "Sure", command=reput, font = (("Times New Roman"),15))
            b0.grid(column=0, row=3, columnspan=1, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

            GUI.mainloop()

            continue

            
        img_Z= np.zeros(img_X.shape, np.uint8)
        img_Zr= np.zeros(img_X.shape, np.uint8)
        
        for r in range(len(img_Z[0])):
            for c in range(len(img_Z[1])):
                X=int_to_binary(img_X[r,c])
                Y=int_to_binary(img_Y[r,c])
                Z=combine(X,Y)
                img_Z[r][c]= binary_to_int(Z)
                img_Zr[r][c]= binary_to_int(reverse(Z))
                # print(Z)
                # print(img_Z[r][c])
        
                
        cv2.imwrite("./result_img/img_X.BMP", cv2.resize(img_X,p_resize,interpolation=cv2.INTER_AREA))
        cv2.imwrite("./result_img/img_Y.BMP", cv2.resize(img_Y,p_resize,interpolation=cv2.INTER_AREA))
        cv2.imwrite("./result_img/img_Z.BMP", cv2.resize(img_Z,p_resize,interpolation=cv2.INTER_AREA))
        cv2.imwrite("./result_img/img_Zr.BMP", cv2.resize(img_Zr,p_resize,interpolation=cv2.INTER_AREA))
        
        
        
        labelimg_X = tk.Label(GUI,text = "img_X :")

        labelimg_X.grid(column=0, row=0, sticky=tk.W+tk.S)

        labelimg_Y = tk.Label(GUI,text = "img_Y :")

        labelimg_Y.grid(column=11, row=0, sticky=tk.W+tk.S)

        labelimg_Z = tk.Label(GUI,text = "img_Z :")

        labelimg_Z.grid(column=0, row=21, sticky=tk.W+tk.S)

        labelimg_Zr = tk.Label(GUI,text = "img_Zr :")

        labelimg_Zr.grid(column=11, row=21, sticky=tk.W+tk.S)

        
        img1 = ImageTk.PhotoImage(Image.open("./result_img/img_X.BMP"))
        labelimg1 = tk.Label(GUI, image=img1)
        labelimg1.grid(row=11, column=0, columnspan=10, rowspan=10,sticky=tk.W+tk.E+tk.N+tk.S)

        img2 = ImageTk.PhotoImage(Image.open("./result_img/img_Y.BMP"))
        labelimg2 = tk.Label(GUI, image=img2)
        labelimg2.grid(row=11, column=11, columnspan=10, rowspan=10,sticky=tk.W+tk.E+tk.N+tk.S)

        img3 = ImageTk.PhotoImage(Image.open("./result_img/img_Z.BMP"))
        labelimg3 = tk.Label(GUI, image=img3)
        labelimg3.grid(row=31, column=0, columnspan=10, rowspan=10,sticky=tk.W+tk.E+tk.N+tk.S)

        img4 = ImageTk.PhotoImage(Image.open("./result_img/img_Zr.BMP"))
        labelimg4 = tk.Label(GUI, image=img4)
        labelimg4.grid(row=31, column=11, columnspan=10, rowspan=10,sticky=tk.W+tk.E+tk.N+tk.S)

        e = tk.Entry(GUI,width=40, font = (("Times New Roman"),15))
        e.grid(column=21, row=13, columnspan=2, padx=20, pady=10, sticky=tk.N)
        

        b1 = tk.Button(GUI,text="X_Z_psnr",command=lambda:set_text("psnr of  X to Z = "+str(psnr(img_X,img_Z))), fg = 'red', bg = 'white', highlightbackground="blue" ,font = (("Times New Roman"),15))
        b1.grid(column=21, row=11, columnspan=2, padx=20, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)
        

        b2 = tk.Button(GUI,text="Y_Zr_psnr",command=lambda:set_text("psnr of  Y to Zr = "+str(psnr(img_Y,img_Zr))), fg = 'blue', bg = 'white', highlightbackground="blue",font = (("Times New Roman"),15))
        b2.grid(column=21, row=12, columnspan=2, padx=20, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

        b3 = tk.Button(GUI, text = "Reselect", command=reput)
        b3.grid(column=21, row=21, columnspan=1, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)
        
        b4 = tk.Button(GUI, text = "Exit", command=QQ)
        b4.grid(column=31, row=21, columnspan=1, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)

        GUI.mainloop()
        break

if __name__ == "__main__":
    main()
        