import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/imageresized_0.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create(threshold=50)

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None,color=(255,0,0))

print("Threshold: ", fast.getThreshold())
print("nonmaxSuppression: ", fast.getNonmaxSuppression())
print("neighborhood: ", fast.getType())
print("Total Keypoints with nonmaxSuppression: ", len(kp))

plt.imshow(img2),plt.show()

# Disable nonmaxSuppression
fast.setNonmaxSuppression(1)
kp = fast.detect(img,None)

print "Total Keypoints without nonmaxSuppression: ", len(kp)

img3 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))

plt.imshow(img3),plt.show()