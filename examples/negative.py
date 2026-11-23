import cv2
import numpy as np

img = cv2.imread('_HLW0388.png')
resized_img = cv2.resize(img, (1068, 600))

negative_img = 255 - resized_img

cv2.imshow('Original Image', resized_img)
cv2.imshow('Negative Image', negative_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
