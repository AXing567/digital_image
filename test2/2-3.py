from skimage import data,color
from matplotlib import pyplot as plt
import numpy as np
img = data.coffee()
grayimg = color.rgb2gray(img) #将彩色图像转化为灰度图像
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(1, 2, 1)
plt.imshow(grayimg, cmap = 'gray')
plt.title('灰度图像')
rows, cols = grayimg.shape
labels = np.zeros([rows, cols])
for i in range(rows):
    for j in range(cols):
        if(grayimg[i, j] < 0.4):
            labels[i, j] = 0
        elif(grayimg[i, j] < 0.8):
            labels[i, j] = 1
        else:
            labels[i, j] = 2
psdimg = color.label2rgb(labels)#不同的label采用不同的颜色
plt.subplot(1, 2, 2)
plt.imshow(psdimg)
plt.title('强度分层图像')
plt.savefig('灰度分层.tif')