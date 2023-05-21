from skimage import io,data

# 从文件中读取图像数据
image = io.imread('flower.jpg')
image = data.hubble_deep_field()

# 显示图像
io.imshow(image)
io.show()