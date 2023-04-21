from skimage import data
from matplotlib import pyplot as plt
import math
import numpy as np
import sys
#定义RGB转HSI
def rgb2hsi(r,g,b):
    r=r/255
    g=g/255
    b=b/255

    num=0.5*((r-g)+(r-b))
    den=((r-g)*(r-g)+(r-b)*(g-b))**0.5

    if b<=g:
        if den == 0:
            den = sys.float_info.min
        h=math.acos(num/den)
    elif b>g:
        if den == 0:
            den = sys.float_info.min
        h=(2*math.pi)-math.acos(num/den)

    s=1-(3*min(r,g,b)/(r+g+b))
    i=(r+g+b)/3

    return int(h),int(s*100),int(i*255)

image = data.imread('flower.jpg')
hsi_image=np.zeros(image.shape,dtype='uint8')
for ii in range(image.shape[0]):
    for jj in range(image.shape[1]):
        r,g,b=image[ii,jj,:]
        h,s,i=rgb2hsi(r,g,b)
        hsi_image[ii,jj,:]=(h,s,i)
        
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.subplot(2,3,1)
plt.axis('off') 
plt.imshow(image)
plt.title('RGB原图像')
plt.subplot(2,3,2)
plt.axis('off') 
plt.imshow(image[:, :, 0], cmap='gray')
plt.title('R分量')
plt.subplot(2,3,3)
plt.axis('off') 
plt.imshow(hsi_image)
plt.title('HSI图像')
plt.subplot(2,3,4)
plt.axis('off') 
plt.imshow(hsi_image[:,:,0], cmap='gray')
plt.title('H分量')
plt.subplot(2,3,5)
plt.axis('off')
plt.imshow(hsi_image[:,:,1], cmap='gray')
plt.title('S分量')
plt.subplot(2,3,6)
plt.axis('off') 
plt.imshow(hsi_image[:,:,2],cmap='gray')
plt.title('I分量')
plt.savefig('HSIimage.tif')