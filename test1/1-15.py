from skimage import data,io
from matplotlib import pyplot as plt
#读入图像
image=data.coffee()
#分别取出红、绿、蓝三个颜色通道
image_r=image[:,:,0]
image_g=image[:,:,1]
image_b=image[:,:,2]
#红色和蓝色互换
temp=image_r
image_r=image_b
image_b=temp
#将互换后的通道颜色重新赋值给图像
image[:,:,0]=image_r
image[:,:,2]=image_b
#图像显示
plt.imshow(image)
plt.show()
