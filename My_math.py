# My_math.py
import numpy as np

_REV8 = np.array([int(f"{i:08b}"[::-1], 2) for i in range(256)], dtype=np.uint8)

def combine(x, y):
    # 保留 x 高 4 bit；y 高 4 bit 反轉後放到低 4 bit
    return (x & 0xF0) | (_REV8[y >> 4] >> 4)

def reverse(z):
    return _REV8[z]

def psnr(a, b):
    mse = np.mean((a.astype(np.float64) - b.astype(np.float64)) ** 2)
    if mse < 1e-10:
        return 100
    return 20 * np.log10(255 / np.sqrt(mse))