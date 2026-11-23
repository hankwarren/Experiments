import exifread
import math

def get_dng_exif(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)

        for tag, value in tags.items():
            if "Thumbnail" not in tag:
                print(f"{tag}: {value}")
    return tags

#tags = get_dng_exif('../images2/20260711_0001.dng')
#tags = get_dng_exif('../images2/DSC_3311.dng')
tags = get_dng_exif('/Volumes/ExternalSSD/Pictures/Projects/Timelapse/LimpusLane_Sunset_2026_07_15/DSC_3176.png')

exposure_time = tags["EXIF ExposureTime"].values[0].decimal()
print(f"ExposureTime: {exposure_time}")

f_number = tags["EXIF FNumber"].values[0]
print(f"FNumber: {f_number}")

print(f"ISO: {tags["EXIF ISOSpeedRatings"]}")
print(f"DateTime: {tags["EXIF DateTimeOriginal"]}")
print(f"FocalLength: {tags["EXIF FocalLength"]}")

# really need to look at the exposure value (EV) for the image
ev = 2 * math.log2(f_number) - math.log2(exposure_time)
print(f"EV: {ev}")