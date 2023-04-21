from matplotlib import pyplot as plt
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

plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False

L = 255
x = [0, 64, 127, 191, 255]
#绘制灰度图像到R通道的映射关系
plt.subplot(2,2,1)
R = []
for i in x:
    R.append(GetR(i))
plt.plot(x, R, 'r--', label = '红色变换')
plt.legend(loc = 'best')
#绘制灰度图像到G通道的映射关系
plt.subplot(2,2,2)
G = []
for i in x:
    G.append(GetG(i))
plt.plot(x, G, 'g', label = '绿色变换')
plt.legend(loc = 'best')
#绘制灰度图像到B通道的映射关系
plt.subplot(2,2,3)
B = []
for i in x:
    B.append(GetB(i))
plt.plot(x, B, 'b', marker = 'o', markersize = 5, label = '蓝色变换')
plt.legend(loc = 'best')
#绘制灰度图像到RGB的映射关系
plt.subplot(2,2,4)
plt.plot(x, R, 'r--')
plt.plot(x, G, 'g')
plt.plot(x, B, 'b', marker = 'o', markersize = 5)
plt.savefig('灰度到彩色的映射关系.tif')