from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Title")
root.geometry("800x600")

class Example(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid(sticky=N+S+E+W)

        #############################################################img1
        self.image1 = Image.open("./result_img/img_X.BMP")
        self.img_copy1= self.image1.copy()
        self.background_image1 = ImageTk.PhotoImage(self.image1)
        self.background1 = Label(self, image=self.background_image1)
        self.background1.grid(row =10, column =0,sticky="nsew")

        #############################################################img2
        self.image2 = Image.open("./result_img/img_Y.BMP")
        self.img_copy2= self.image2.copy()
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2 = Label(self, image=self.background_image2)
        self.background2.grid(row =10, column =50,sticky="nsew")


        #############################################################img3
        self.image3 = Image.open("./result_img/img_Z.BMP")
        self.img_copy3= self.image3.copy()
        self.background_image3 = ImageTk.PhotoImage(self.image3)
        self.background3 = Label(self, image=self.background_image3)
        self.background3.grid(row =11, column =0,sticky="nsew")

        #############################################################img4
        self.image4 = Image.open("./result_img/img_Zr.BMP")
        self.img_copy4= self.image4.copy()
        self.background_image4 = ImageTk.PhotoImage(self.image4)
        self.background4 = Label(self, image=self.background_image4)
        self.background4.grid(row =11, column =50,sticky="nsew")


        
        # self.background.grid_rowconfigure(0, weight=1)
        # self.background.grid_columnconfigure(0, weight=1)

        # self.background.bind('<Configure>', self._resize_image)
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

        
e = Example(root)
e.grid(row =0, column =0,sticky="nsew")
# e.grid_rowconfigure(0, weight=1)
# e.grid_columnconfigure(0, weight=1)

root.mainloop()