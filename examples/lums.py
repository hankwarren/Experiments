import cv2
import numpy as np
import rawpy
from pathlib import Path
import exifread

#file = "../images/20260711_0001.dng"
#with rawpy.imread(file) as raw:
    # default demosaicing
    # default auto-exposure
    # default auto-white-balance
#    raw = raw.postprocess()

# define the standard sRGB BT.709 coefficients: R, G, B
#   numpy arrays are RGB, opencv arrays are BGR
weights = np.array([0.21126, 0.7152, 0.0722]) # 2d array
#weights = np.array([0.0722, 0.7152, 0.21126]) # simple array

print('weights', weights)
print('weights: ', weights.reshape(1, 3))

files = [f for f in Path('../images2').iterdir() if f.is_file()]
#print(type(files))
#print(files)
for posix_item in sorted(files):
    #print(posix_item)
    #print(type(posix_item))
    if posix_item.suffix == '.dng':
        with rawpy.imread(str(posix_item)) as raw:
        # default demosaicing
        # default auto-exposure
        # default auto-white-balance
            raw = raw.postprocess()

        #lum_map_709 = cv2.transform(raw, weights.reshape(1,3))
        #avg_lum_709 = np.mean(lum_map_709)

        # quick and dirty?
        avg_lum_709 = np.mean(raw)
        # get exif info
# FNumber
# ISOSpeedRatings
# DateTimeOriginal        
#        if "ExposureTime" in tag:
#            exposure_time 
        with open(posix_item, 'rb') as f:
            tags = exifread.process_file(f)
        exposure_time = tags["EXIF ExposureTime"]
        fnumber = tags["EXIF FNumber"]
        iso = tags["EXIF ISOSpeedRatings"]
        print(f"{posix_item} Avg Lum {avg_lum_709:6.2f} \
              {exposure_time} sec \
              {fnumber} \
              {iso}", flush=True)

# should also look at resize and cropped image to understand changes in lum
#resized = cv2.resize(cv2.cvtColor(raw, cv2.COLOR_RGB2BGR), (400, 300))
#cv2.imshow('raw image', cv2.cvtColor(raw, cv2.COLOR_RGB2BGR))
#cv2.imshow('resized: ', resized)
#cv2.waitKey(0)