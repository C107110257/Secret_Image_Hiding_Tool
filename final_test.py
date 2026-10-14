import cv2
import sys
import math
import glob
import numpy as np

N = 8

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
    img_X= cv2.imread("./data/LENA.BMP",0)
    img_Y= cv2.imread("./data/Jet.jpg",0)
    # img_Y= cv2.imread("./data/Jet.BMP",0)
    # img_Y= cv2.imread("./data/Jet_resize256.BMP",0)
    
    
    if img_X.shape != img_Y.shape:
        print("img_X.shape",img_X.shape)
        print("img_Y.shape",img_Y.shape)
        sys.exit("Size is not equal !")    
    
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
    X_Z_psnr = psnr(img_X,img_Z)
    Y_Zr_psnr = psnr(img_Y,img_Zr)
            
            
    print("X_Z_psnr",X_Z_psnr)
    print("Y_Zr_psnr",Y_Zr_psnr)
    
            
            
            
    cv2.imshow("img_X", img_X)
    cv2.imshow("img_Y", img_Y)
    cv2.imshow("img_Z", img_Z)
    cv2.imshow("img_Zr", img_Zr)
  
    cv2.waitKey(0)
    # X=int_to_binary(img_X[0,0])
    # Y=int_to_binary(img_Y[0,0])
    # X2=reverse(X)
    
    # print("img_X[0,0]: ",img_X[0,0])
    # print("img_Y[0,0]: ",img_Y[0,0])
    # print("X: ",X)
    # print("Y: ",Y)
    # print("Z: ",Z)
    # print("x2: ",X2)
     
if __name__ == "__main__":
    main()
        