import glob
import cv2

from crop_contour_func import process

for (i,image_file) in enumerate(glob.iglob('images/*.jpg')):
        process(image_file, i)   