from skimage import data,io
import math
import numpy as np
import sys
from scipy import signal
from skimage import data
from matplotlib import pyplot as plt


def rgb2hsi(r, g, b):
    r = r / 255
    g = g / 255
    b = b / 255
    num = 0.5 * ((r - g) + (r - b))
    den = ((r - g) * (r - g) + (r - b) * (g - b))**0.5
    if b<=g:
        if den == 0:
            den = sys.float_info.min
        h = math.acos(num/den)
    elif b>g:
        if den == 0:
            den = sys.float_info.min
        h = (2*math.pi)-math.acos(num/den)
    s = 1 - (3 * min(r, g, b) / (r + g + b))
    i = (r + g + b)/3
    return int(h),int(s*100),int(i*255)

image = io.imread(r'C:\Users\PC78\PycharmProjects\pythonProject\flower.jpg')
hsi_image = np.zeros(image.shape, dtype='uint8')
for ii in range(image.shape[0]):
    for jj in range(image.shape[1]):
        r, g, b = image[ii, jj, :]
        h, s, i = rgb2hsi(r, g, b)
        hsi_image[ii, jj, :] = (h, s, i)
H = hsi_image[:, :, 0]
S = hsi_image[:, :, 1]
I = hsi_image[:, :, 2]
#生成二值饱和度模板
S_template = np.zeros(S.shape, dtype='uint8')
for i in range(S.shape[0]):
    for j in range(S.shape[1]):
        if S[i, j] > 0.3 * S.max():
            S_template[i, j] = 1
#色调图像与二值饱和度模板相乘可得到分割结果F
F = np.zeros(H.shape, dtype='uint8')
for i in range(F.shape[0]):
    for j in range(F.shape[1]):
        F[i, j] = H[i, j] * S_template[i, j]
plt.imshow(F, cmap = 'gray')
#显示结果
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(2,3,1)
plt.axis('off')
plt.imshow(image)
plt.title('原始RGB图像')
plt.subplot(2,3,2)
plt.axis('off')
plt.imshow(H, cmap='gray')
plt.title('H分量')
plt.subplot(2,3,3)
plt.axis('off')
plt.imshow(S, cmap='gray')
plt.title('S分量')
plt.subplot(2,3,4)
plt.axis('off')
plt.imshow(I, cmap='gray')
plt.title('I分量')
plt.subplot(2,3,5)
plt.axis('off')
plt.imshow(S_template, cmap='gray')
plt.title('二值饱和度模板')
plt.subplot(2,3,6)
plt.axis('off')
plt.imshow(F, cmap='gray')
plt.title('分割结果')
plt.savefig('HSI彩色分割.tif')
plt.show()

image = io.imread(r'C:\Users\PC78\PycharmProjects\pythonProject\flower.jpg')
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
