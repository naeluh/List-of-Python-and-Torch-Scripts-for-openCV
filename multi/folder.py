import glob
import cv2

from resize import process

for (i,image_file) in enumerate(glob.iglob('/home/winowa/Desktop/Intern101/fisherFace/test/*.jpg')):
        process(image_file, i)