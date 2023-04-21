from skimage import data
from matplotlib import pyplot as plt
image=data.coffee()  #载入测试图像
ratio=128                #设置量化比率
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        for k in range(image.shape[2]):
            image[i][j][k]=int(image[i][j][k]/ratio)*ratio
            #对图像每个像素进行量化
plt.imshow(image)#打印采样后图像图像
plt.show()
