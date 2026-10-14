import sys
import tkinter as tk
import cv2
from tkinter import *

from PIL import Image, ImageTk

import My_math as m

class GUI_img(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        sz=self.master.winfo_width()/3
        #############################################################img name1
        self.labelimg_X = Label(self,text = "img_X :")
        self.labelimg_X.grid(row =0, column =0, sticky=N+S+E+W)
        #############################################################img name2
        self.labelimg_Y = Label(self,text = "img_Y :")
        self.labelimg_Y.grid(row =0, column =1, sticky=N+S+E+W)
        #############################################################img name3
        self.labelimg_Z = Label(self,text = "img_Z :")
        self.labelimg_Z.grid(row =2, column =0, sticky=N+S+E+W)
        #############################################################img name4
        self.labelimg_Zr = Label(self,text = "img_Zr :")
        self.labelimg_Zr.grid(row =2, column =1, sticky=N+S+E+W)


        #############################################################img1
        self.grid(sticky=N+S+E+W)
        self.image1 = Image.open("./result_img/img_X.BMP")
        self.img_copy1= self.image1.copy()
        self.background_image1 = ImageTk.PhotoImage(self.image1)
        self.background1 = Label(self, image=self.background_image1)
        self.background1.grid(row =1, column =0,sticky="nsew")

        #############################################################img2
        self.image2 = Image.open("./result_img/img_Y.BMP")
        self.img_copy2= self.image2.copy()
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2 = Label(self, image=self.background_image2)
        self.background2.grid(row =1, column =1,sticky="nsew")


        #############################################################img3
        self.image3 = Image.open("./result_img/img_Z.BMP")
        self.img_copy3= self.image3.copy()
        self.background_image3 = ImageTk.PhotoImage(self.image3)
        self.background3 = Label(self, image=self.background_image3)
        self.background3.grid(row =3, column =0,sticky="nsew")

        #############################################################img4
        self.image4 = Image.open("./result_img/img_Zr.BMP")
        self.img_copy4= self.image4.copy()
        self.background_image4 = ImageTk.PhotoImage(self.image4)
        self.background4 = Label(self, image=self.background_image4)
        self.background4.grid(row =3, column =1,sticky="nsew")
        self.master.bind('<Configure>', self._resize_image)
    def _resize_image(self,event):
        new_width = int(self.master.winfo_width()/3)
        new_height = int(self.master.winfo_height()/2.2)


        #############################################################img1
        self.image1 = self.img_copy1.resize((new_width, new_height))
        self.background_image1 = ImageTk.PhotoImage(self.image1)
        self.background1.configure(image =  self.background_image1)

        #############################################################img2
        self.image2 = self.img_copy2.resize((new_width, new_height))
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2.configure(image =  self.background_image2)

        #############################################################img3
        self.image3 = self.img_copy3.resize((new_width, new_height))
        self.background_image3 = ImageTk.PhotoImage(self.image3)
        self.background3.configure(image =  self.background_image3)

        #############################################################img4
        self.image4 = self.img_copy4.resize((new_width, new_height))
        self.background_image4 = ImageTk.PhotoImage(self.image4)
        self.background4.configure(image =  self.background_image4)


class GUI_button(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        mx=cv2.imread("./result_img/img_X.BMP", 0)
        my=cv2.imread("./result_img/img_Y.BMP", 0)
        mz=cv2.imread("./result_img/img_Z.BMP", 0)
        mzr=cv2.imread("./result_img/img_Zr.BMP", 0)

        self.master = master
        
        self.e = Entry(self,width=40, font = (("Times New Roman"),15))
        self.e.grid(row =0, column =0, columnspan=2, padx=20, pady=10, sticky=N)

        self.b1 = Button(self,text="X_Z_psnr",command=lambda:self.set_text("psnr of  X to Z = "+str(m.psnr(mx,mz))), fg = 'red', bg = 'white', highlightbackground="blue" ,font = (("Times New Roman"),15))
        self.b1.grid(row =1, column =0, columnspan=2, padx=20, pady=10, sticky=N+S+E+W)
        

        self.b2 = Button(self,text="Y_Zr_psnr",command=lambda:self.set_text("psnr of  Y to Zr = "+str(m.psnr(my,mzr))), fg = 'blue', bg = 'white', highlightbackground="blue",font = (("Times New Roman"),15))
        self.b2.grid(row =2, column =0, columnspan=2, padx=20, pady=10, sticky=N+S+E+W)

        self.b3 = Button(self, text = "Reselect", command=self.reput)
        self.b3.grid(row =3, column =0, padx=10, pady=10, sticky=N+S+E+W)
        
        self.b4 = Button(self, text = "Exit", command=self.QQ)
        self.b4.grid(row =3, column =1, padx=10, pady=10, sticky=N+S+E+W)


    def reput(self):
        self.master.destroy()
    def QQ(self):
        self.master.destroy()
        sys.exit("exit !")
    def set_text(self,text):
        self.e.delete(0,tk.END)
        self.e.insert(0,text)
        return 
    

class error_GUI(Frame):
    def __init__(self, master,shape_x,shape_y):
        Frame.__init__(self)

        self.shape =shape_x
        self.shape =shape_y
        
        self.labelimg_x = Label(self,text = "img_X.shape = " + str(shape_x), font = (("Times New Roman"),30))
        self.labelimg_x.grid(column=0, row=0, sticky=N+S+E+W)

        self.labelimg_Y = Label(self,text = "img_Y.shape = " + str(shape_y), font = (("Times New Roman"),30))
        self.labelimg_Y.grid(column=0, row=1, sticky=N+S+E+W)

        self.labelimg_text = Label(self,text = "Please select two images of the same size !", font = (("Times New Roman"),30))
        self.labelimg_text.grid(column=0, row=2, sticky=N+S+E+W)

        self.b0 = Button(self, text = "Sure", command=self.reput, font = (("Times New Roman"),30))
        self.b0.grid(column=0, row=3, columnspan=1, padx=10, pady=10, sticky=N+S+E+W)

    def reput(self):
        self.master.destroy()
        
