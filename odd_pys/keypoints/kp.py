import cv2
import numpy as np

img = cv2.imread('imageresized_0.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
detector = sift.detect(gray, None)

kpts, des = sift.compute(gray, detector)
# kpts,des=descriptor.compute(gray,kpts)
im_with_keypoints = cv2.drawKeypoints(gray, kpts, np.array([]), color=255, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey()