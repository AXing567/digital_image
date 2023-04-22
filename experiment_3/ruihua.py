from skimage import data,filters
from matplotlib import pyplot as plt
img = data.camera()
img_laplace = filters.laplace(img, ksize = 3,mask = None)
img_enhance = img + img_laplace
plt.rcParams['font.sans-serif']=['simHei']
plt.subplot(1,3,1)
plt.title('原始图像')
plt.imshow(img,cmap='gray')
plt.subplot(1,3,2)
plt.title('拉普拉斯图像')
plt.imshow(img_laplace,cmap='gray')
plt.subplot(1,3,3)
plt.title('拉普拉斯锐化增强图像')
plt.imshow(img_enhance,cmap='gray')
plt.show()