from skimage import data,io
from matplotlib import pyplot as plt
import numpy as np
import math

image = io.imread('flower.jpg')
r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]
#RGB颜色空间中的分割
#选择要分割的区域
r1 = r[128:255, 85:169]
#计算该区域中的彩色点的平均向量a的红色分量
r1_u = np.mean(r1)
#计算样本点红色分量的标准差
r1_d = 0.0
for i in range(r1.shape[0]):
    for j in range(r1.shape[1]):
        r1_d = r1_d + (r1[i, j] - r1_u) * (r1[i, j] - r1_u)
r1_d = math.sqrt(r1_d/r1.shape[0]/r1.shape[1])
#寻找符合条件的点，r2为红色分割图像
r2 = np.zeros(r.shape, dtype = 'uint8')
for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        if r[i, j] >= (r1_u - 1.25 * r1_d) and r[i, j] <= (r1_u + 1.25 * r1_d):
            r2[i, j] = 1
#image2为根据红色分割后的RGB图像，
image2 = np.zeros(image.shape, dtype = 'uint8')
for i in range(r.shape[0]):
    for j in range(r.shape[1]):
        if r2[i, j] == 1:
            image2[i, j, :] = image[i, j, :]
#显示结果
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(2,3,1)
plt.axis('off') 
plt.imshow(image)
plt.title('原始RGB图像') 
plt.subplot(2,3,2)
plt.axis('off') 
plt.imshow(r, cmap='gray')
plt.title('R分量') 
plt.subplot(2,3,3)
plt.axis('off') 
plt.imshow(g, cmap='gray')
plt.title('G分量') 
plt.subplot(2,3,4)
plt.axis('off') 
plt.imshow(b, cmap='gray')
plt.title('B分量') 
plt.subplot(2,3,5)
plt.axis('off') 
plt.imshow(r2, cmap='gray')
plt.title('红色分割图像') 
plt.subplot(2,3,6)
plt.axis('off') 
plt.imshow(image2)
plt.title('分割后的RGB图像') 
plt.savefig('RGB彩色分割.tif')
plt.show()