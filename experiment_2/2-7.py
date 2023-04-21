from skimage import data
from matplotlib import pyplot as plt
import numpy as np 
image = data.coffee()  #载入测试图像
#初始化灰度图像
max_gray = np.zeros(image.shape[0:2],dtype='uint8')
ave_gray = np.zeros(image.shape[0:2],dtype='uint8')
weight_gray = np.zeros(image.shape[0:2],dtype='uint8')
for ii in range(image.shape[0]):
    for jj in range(image.shape[1]):
        r, g, b = image[ii, jj, :]
        #最大值法
        max_gray[ii, jj] = max(r, g, b) 
        #平均值法
        ave_gray[ii, jj] = (r + g + b)/3
        #加权平均法
        weight_gray[ii, jj] = 0.30 * r + 0.59 * g + 0.11 * b

plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(2,2,1)
plt.axis('off') 
plt.imshow(image)
plt.title('彩色图像')
plt.subplot(2,2,2)
plt.axis('off') 
plt.imshow(max_gray, cmap='gray')
plt.title('最大值法')
plt.subplot(2,2,3)
plt.axis('off')
plt.imshow(ave_gray, cmap='gray')
plt.title('平均值法')
plt.subplot(2,2,4)
plt.axis('off') 
plt.imshow(weight_gray, cmap='gray')
plt.title('加权平均法')
plt.savefig('彩色图像灰度化.tif')