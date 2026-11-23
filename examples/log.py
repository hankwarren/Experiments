import cv2
import numpy as np

img = cv2.imread('_HLW0388.png')
resized_img = cv2.resize(img, (1068, 600))

negative_img = 255 - resized_img

c = 255 / (np.log(1 + np.max(resized_img)))
log_transformed = c * np.log(1 + resized_img)
log_transformed = np.array(log_transformed, dtype=np.uint8)

cv2.imshow('Original Image', resized_img)
cv2.imshow('Negative Image', negative_img)
cv2.imshow('Log Transformed Image', log_transformed)

for gamma in [0.1, 0.5, 1.2, 2.2]:
    gamma_corrected = np.array(255*(resized_img / 255) ** gamma, dtype='uint8')
    cv2.imshow('gamma transformed' + str(gamma), gamma_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()
