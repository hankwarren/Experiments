import cv2
import numpy as np
import rawpy
import imageio

def change_exposure(img, exposure_factor):
    if img is None:
        print("Error: Image not found ")
        return None
    return cv2.convertScaleAbs(img, alpha=exposure_factor, beta=0)

with rawpy.imread("../images/20260711_0303.dng") as raw:
    raw = raw.postprocess()
#cv2.imshow('Original', raw)
#cv2.waitKey(0)

#imageio.imwrite("input_image.jpg", raw)
#imageio.imwrite("input_image.png", raw)
# this is the essential step!
original = cv2.cvtColor(raw, cv2.COLOR_RGB2BGR)

#h, w = original.shape[:2]
#ratio = (int(h * 800 / w), 800) # cv2.resize expects (w, h) instead of (h, w)

resized = cv2.resize(original, (400, 300))
cv2.imshow('Resized', resized)
cv2.waitKey(0)

brighter = change_exposure(resized, 1.3)
dimmer = change_exposure(resized, 0.7)
cv2.imshow('Resized Original Exposure', resized)
cv2.imshow('Brighter Exposure', brighter)
cv2.imshow('Dimmer Exposure', dimmer)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Question to stackoverflow:
# How to fast change image brightness with python + OpenCV?
#   and this was one of the answers
def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
