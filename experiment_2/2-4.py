from skimage import data, color
from matplotlib import pyplot as plt
import numpy as np
#定义灰度级到彩色变换    
L = 255    
def GetR(gray):
    if gray < L / 2:
        return 0
    elif gray > L / 4 * 3:
        return L
    else:
        return 4 * gray - 2 * L
       
def GetG(gray):
    if gray < L / 4:
        return 4 * gray
    elif gray > L / 4 * 3:
        return 4 * L - 4 * gray
    else:
        return L
        
def GetB(gray):
    if gray < L / 4:
        return L
    elif gray > L / 2:
        return 0
    else:
        return 2 * L - 4 * gray

img = data.coffee()
grayimg = color.rgb2gray(img) * 255 #将彩色图像转化为灰度图像
colorimg = np.zeros(img.shape,dtype='uint8')
for ii in range(img.shape[0]):
    for jj in range(img.shape[1]):
        r,g,b = GetR(grayimg[ii, jj]), GetG(grayimg[ii, jj]), GetB(grayimg[ii, jj])
        colorimg[ii,jj,:]=(r, g, b)

plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False    
plt.subplot(1,2,1)
plt.axis('off') 
plt.imshow(grayimg, cmap='gray')
plt.title('灰度图像')
plt.subplot(1,2,2)
plt.axis('off') 
plt.imshow(colorimg)
plt.title('伪彩色图像')
plt.savefig('Intensity2Color.tif')