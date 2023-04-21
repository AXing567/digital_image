'''
高斯平滑滤波是一种应用比较广泛的平滑滤波器
可以使用3*3，5*5，7*7等高斯平滑滤波器实现对图像的平滑滤波
'''
import numpy as np
from scipy import signal
from skimage import data
from matplotlib import pyplot as plt
import math


def correl2d(img, window):
    s = signal.correlate2d(img, window, mode='same', boundary='fill')
    return s.astype(np.unint8)


# 定义二维高斯函数
def gauss(i, j, sigma):
    return 1 / (2 * math.pi * sigma ** 2) * math.exp(-(i ** 2 + j ** 2) / (2 * sigma ** 2))


# 定义radius*radius的高斯平滑滤波模板
def gauss_window(radius, sigma):
    window = np.zeros((radius * 2 + 1, radius * 2 + 1))
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            window[i + radius][j + radius] = gauss(i, j, sigma)
    return window / np.sum(window)
