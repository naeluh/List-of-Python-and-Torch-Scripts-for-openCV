import glob
import cv2

from add_contours import process

for (i,image_file) in enumerate(glob.iglob('images/*.png')):
        process(image_file, i)   