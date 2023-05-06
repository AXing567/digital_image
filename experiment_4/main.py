from skimage import io, filters
from matplotlib import pyplot as plt
import numpy as np


# 图像空间滤波函数
def correl2d(img, window):
    m = window.shape[0]
    n = window.shape[1]
    # 边界通过 0 灰度值填充扩展

    img1 = np.zeros((img.shape[0] + m - 1, img.shape[1] + n - 1))
    img1[(m - 1) // 2: (img.shape[0] + (m - 1) // 2), (n - 1) // 2: (img.shape[1] + (n - 1) // 2)] = img
    img2 = np.zeros(img.shape)
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            temp = img1[i: i + m, j: j + n]
            img2[i, j] = np.sum(np.multiply(temp, window))
    return img2


# img 为原始图像
img = io.imread('I3.jpg', as_gray=True)
# img_laplace 为原始图像经过拉普拉斯变换后的结果
window = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
img_laplace = correl2d(img, window)
img_laplace = 255 * (img_laplace - img_laplace.min()) / (img_laplace.max() - img_laplace.min())
# 将 img 和 img_laplace 相加得到锐化增强图像 img_laplace
img_laplace_enhance = img + img_laplace
# img_sobel 为对原始图像 img 进行 sobel 处理的结果
img_sobel = filters.sobel(img)
# 使用 5×5 均值滤波器平滑后的 sobel 图像
window_mean = np.ones((5, 5)) / (5 ** 2)
img_sobel_mean = correl2d(img_sobel, window_mean)
# 将 img_laplace_enhance 与 img_sobel_mean 相乘得到锐化结果
img_mask = img_laplace_enhance * img_sobel_mean
# 将原始图像 img 与锐化图像 img_sharp 相加得到锐化增强图像
img_sharp_enhance = img + img_mask
# 对 img_sharp_enhance 进行灰度幂律变换得到最终结果
img_enhance = img_sharp_enhance ** 0.5
# 显示图像
imgList = [img, img_laplace, img_laplace_enhance, img_sobel, img_sobel_mean, img_mask, img_sharp_enhance, img_enhance]

i = 0
for grayImg in imgList:
    i += 1
    plt.subplot(2, 4, i)
    plt.axis('off')
    plt.imshow(grayImg, cmap='gray')

plt.show()
