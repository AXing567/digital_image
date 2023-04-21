'''
高斯平滑滤波是一种应用比较广泛的平滑滤波器
可以使用3*3，5*5，7*7等高斯平滑滤波器实现对图像的平滑滤波
'''
import numpy as np
from scipy import signal
from skimage import data
from matplotlib import pyplot as plt
import math

def correl2d(img,window):
    s=signal.correlate2d(img,window,mode='same',boundary='fill')#信号的互相关运算，img和window做卷积运算，mode=‘same’表示输出数组与img相同以window为中心，最后一个参数表示边界值填充
    return s.astype(np.uint8) #数值类型转换
# 定义二维高斯函数
def gauss(i,j,sigma):
    return 1/(2*math.pi*sigma**2)*math.exp(-(i**2+j**2)/(2*sigma**2))
#定义radius*radius的高斯平滑滤波模板
def guass_window(radius,sigma):
    window=np.zeros((radius*2+1,radius*2+1))
    for i in range(-radius,radius+1):
        for j in range(-radius,radius+1):
            window[i+radius][j+radius]=gauss(i,j,sigma)
    return window/np.sum(window)
#img为原始图像
img=data.camera()
#高斯平滑滤波模板
window1=guass_window(3,1.0)
#生成高斯滤波结果
img_gaussFilter=correl2d(img,window1)
#显示结果
plt.rcParams['font.sans-serif']=['simHei']
plt.subplot(1,2,1)
plt.title('原始图像')
plt.imshow(img,cmap='gray')
plt.subplot(1,2,2)
plt.title('滤波图像')
plt.imshow(img_gaussFilter,cmap='gray')
plt.show()