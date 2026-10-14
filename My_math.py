import numpy as np
import math

N = 8

def psnr(img1, img2): #計算PSNR
   mse = np.mean( (img1/255. - img2/255.) ** 2 )
   if mse < 1.0e-10:
      return 100
   PIXEL_MAX = 1
   return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


def reverse(x): #位元陣列反轉
    return x[::-1]

def combine(x,y): #合併
    y=y[::-1] #先反轉
    return np.concatenate((x[0:4],y[4:8]),axis=0) #取位元合併

def int_to_binary(num):
    b= np.zeros((N,), dtype=int) 
    for i in range(N):          
        b[N-i-1]= num%2
        num = num/2
    return b

def binary_to_int(b):
    n = 0
    for i in range(N):          
        n += b[i]*pow(2,N-i-1)
    return n