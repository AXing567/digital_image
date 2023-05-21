from matplotlib import pyplot as plt
from skimage import exposure, data

image = data.coffee()
hist_r = exposure.histogram(image[:, :, 0], nbins=256)
hist_g = exposure.histogram(image[:, :, 1], nbins=256)
hist_b = exposure.histogram(image[:, :, 2], nbins=256)

fig, ax = plt.subplots(2, 2, figsize=(10, 10))

ax[0, 0].imshow(image)
ax[0, 0].set_title('原始图像')
ax[0, 0].set_xlabel('x 坐标')
ax[0, 0].set_ylabel('y 坐标')

ax[0, 1].bar(hist_r[1], hist_r[0], width=1, color='red')
ax[0, 1].set_title('红色通道直方图')
ax[0, 1].set_xlim([0, 256])
ax[0, 1].set_xlabel('像素值')
ax[0, 1].set_ylabel('像素数量')

ax[1, 0].bar(hist_g[1], hist_g[0], width=1, color='green')
ax[1, 0].set_title('绿色通道直方图')
ax[1, 0].set_xlim([0, 256])
ax[1, 0].set_xlabel('像素值')
ax[1, 0].set_ylabel('像素数量')

ax[1, 1].bar(hist_b[1], hist_b[0], width=1, color='blue')
ax[1, 1].set_title('蓝色通道直方图')
ax[1, 1].set_xlim([0, 256])
ax[1, 1].set_xlabel('像素值')
ax[1, 1].set_ylabel('像素数量')

plt.tight_layout()
plt.show()