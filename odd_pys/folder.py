import glob
import cv2

from resize import process

for (i,image_file) in enumerate(glob.iglob('84 photos/*.jpg')):
        process(image_file, i)  