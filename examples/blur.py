import cv2
from matplotlib import pyplot as plt

image_path = '_HLW0388.png'
image = cv2.imread(image_path)
resized_image = cv2.resize(image, (1068, 600))
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

#plt.imshow(resized_image_rgb)
#plt.title('Original Image')

gaussian = cv2.GaussianBlur(resized_image, (15, 15), 0)
gaussian_rgb = cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB)

plt.imshow(gaussian_rgb)
plt.title('Gaussian Blurred Image')

plt.axis('on')
plt.show()