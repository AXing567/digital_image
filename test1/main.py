from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
from skimage import data, io, exposure
from matplotlib import pyplot as plt

# 步骤1-4
# 读入图像
image = data.coffee()
# 分别取出红、绿、蓝三个颜色通道
image_r = image[:, :, 0]
image_g = image[:, :, 1]
image_b = image[:, :, 2]
# 分别展示三个通道
plt.subplot(2, 2, 1)
io.imshow(image)
plt.subplot(2, 2, 2)
io.imshow(image_r)
plt.subplot(2, 2, 3)
io.imshow(image_g)
plt.subplot(2, 2, 4)
io.imshow(image_b)
plt.show()

# 步骤5
# 红色和蓝色互换
temp = image_r
image_r = image_b
image_b = temp
# 将互换后的通道颜色重新赋值给图像
image[:, :, 0] = image_r
image[:, :, 2] = image_b
# 图像显示
plt.imshow(image)
plt.show()

# 步骤6 设定gama值分别为0.67，1，0.2，50 图像变化结果
# 读入图像
image = io.imread("flower.jpg")
# 分别计算gamma=0.2,0.67,25时的图像
image_1 = exposure.adjust_gamma(image, 0.2)
image_2 = exposure.adjust_gamma(image, 0.67)
image_3 = exposure.adjust_gamma(image, 50)
# 分别展示原图及结果图像
plt.subplot(2, 2, 1)
plt.title('gamma=1')
io.imshow(image)
plt.subplot(2, 2, 2)
plt.title('gamma=0.2')
io.imshow(image_1)
plt.subplot(2, 2, 3)
plt.title('gamma=0.67')
io.imshow(image_2)
plt.subplot(2, 2, 4)
plt.title('gamma=50')
io.imshow(image_3)
plt.show()



# 步骤八 对moon图片直方图均衡化的结果展示
img = data.moon()
plt.figure("hist", figsize=(8, 8))
arr = img.flatten()
plt.subplot(221)
plt.imshow(img, plt.cm.gray)  # 原始图像
plt.subplot(222)
plt.hist(arr, bins=256, density=True, edgecolor='None', facecolor='red')  # 原始图像直方图
img1 = exposure.equalize_hist(img)
arr1 = img1.flatten()
plt.subplot(223)
plt.imshow(img1, plt.cm.gray)  # 均衡化图像
plt.subplot(224)
plt.hist(arr1, bins=256, density=True, edgecolor='None', facecolor='red')  # 均衡化直方图
plt.show()


# 步骤九 月亮加减
moon = data.moon()
camera = data.camera()
image_minus = moon - camera
image_plus = moon + camera
plt.set_cmap(cmap='gray')
plt.subplot(2, 2, 1)
plt.title('月亮图像', fontproperties=font_set)
plt.imshow(moon)
plt.subplot(2, 2, 2)
plt.title('摄影师图像', fontproperties=font_set)
plt.imshow(camera)
plt.subplot(2, 2, 3)
plt.title('月亮加摄影师图像', fontproperties=font_set)
plt.imshow(image_plus)
plt.subplot(2, 2, 4)
plt.title('月亮减摄影师图像', fontproperties=font_set)
plt.imshow(image_minus)
plt.show()

