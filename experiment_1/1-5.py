from skimage import data, io
from matplotlib import pyplot as plt
import numpy as np  # 导入所需类包

image = io.imread("flower.jpg")  # 载入测试图像
print(image.shape)  # 显示图像原始大小
print(type(image))  # 显示图像类型
ratio = 20  # 设置采样比率
image1 = np.zeros((int(image.shape[0] / ratio),
                   int(image.shape[1] / ratio), image.shape[2]), dtype='int32')  # 设置采样后图像大小

for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        for k in range(image1.shape[2]):  # 对图像进行遍历
            delta = image[i * ratio:(i + 1) * ratio, j * ratio:(j + 1) * ratio, k]  # 获取需要采样图像块
            image1[i, j, k] = np.mean(delta)  # 计算均值，并存入结果图像
plt.imshow(image1)  # 打印采样后图像图像
plt.show()
