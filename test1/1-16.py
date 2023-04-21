from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
from skimage import data
from matplotlib import pyplot as plt
moon=data.moon()
camera=data.camera()
image_minus=moon-camera
image_plus=moon+camera
plt.set_cmap(cmap='gray')
plt.subplot(2,2,1)
plt.title('月亮图像',fontproperties=font_set)
plt.imshow(moon)
plt.subplot(2,2,2)
plt.title('摄影师图像',fontproperties=font_set)
plt.imshow(camera)
plt.subplot(2,2,3)
plt.title('月亮加摄影师图像',fontproperties=font_set)
plt.imshow(image_plus)
plt.subplot(2,2,4)
plt.title('月亮减摄影师图像',fontproperties=font_set)
plt.imshow(image_minus)
plt.show()
