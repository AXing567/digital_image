from skimage import data,io,exposure
from matplotlib import pyplot as plt
#读入图像
image=data.coffee()
#分别计算gamma=0.2,0.67,25时的图像
image_1=exposure.adjust_gamma(image,0.1)
image_2=exposure.adjust_gamma(image,0.67)
image_3=exposure.adjust_gamma(image,25)
#分别展示原图及结果图像
plt.subplot(2,2,1)
plt.title('gamma=1')
io.imshow(image)
plt.subplot(2,2,2)
plt.title('gamma=0.2')
io.imshow(image_1)
plt.subplot(2,2,3)
plt.title('gamma=0.67')
io.imshow(image_2)
plt.subplot(2,2,4)
plt.title('gamma=25')
io.imshow(image_3)
plt.show()
