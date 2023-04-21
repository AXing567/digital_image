from scipy import signal
from skimage import data
from matplotlib import pyplot as plt
import math
import numpy as np


def gauss(i, j, sigma):
    return 1 / (2 * math.pi * sigma ** 2) * math.exp(-(i ** 2 + j ** 2) / (2 * sigma ** 2))


def correl2d(img, window):
    s = signal.correlate2d(img, window, mode='same', boundary='fill')
    return s.astype(np.uint8)


def gauss_window(radius, sigma):
    window = np.zeros((radius * 2 + 1, radius * 2 + 1))
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            window[i + radius][j + radius] = gauss(i, j, sigma)
    return window / np.sum(window)


image = data.camera()

window1 = gauss_window(3, 1)

img_gaussFilter = correl2d(image, window1)

# 显示两张图片
plt.subplot(1, 2, 1)  # 1行2列，第1张图
plt.imshow(image, cmap='gray')
plt.title('Image 1')

plt.subplot(1, 2, 2)  # 1行2列，第2张图
plt.imshow(img_gaussFilter, cmap='gray')
plt.title('Image 2')

plt.show()
