from skimage import data
from matplotlib import pyplot as plt
import numpy as np 
image = data.coffee()  #载入测试图像
fig = plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False
#两行两列的第一个子图
axis = fig.add_subplot(221) 
plt.axis('off') # 不显示坐标轴
plt.imshow(image)#显示RGB彩色图像
plt.title('RGB图像')
#第二个子图
axis = fig.add_subplot(222) 
imageR = image[:, :, 0]
plt.axis('off') 
plt.imshow(imageR, cmap='gray')#显示R通道图像
plt.title('R通道图像')
#第三个子图
axis = fig.add_subplot(223) 
imageG = image[:, :, 1]
plt.axis('off') 
plt.imshow(imageG, cmap='gray')#显示G通道图像
plt.title('G通道图像')
#第四个子图
axis = fig.add_subplot(224) 
imageB = image[:, :, 2]
plt.axis('off') 
plt.imshow(imageB, cmap='gray')#显示B通道图像
plt.title('B通道图像')
plt.savefig('RGBimage.tif')