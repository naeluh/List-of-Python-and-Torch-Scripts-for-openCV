import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt


# Read image
# src = cv2.imread("black.jpg")

image = cv2.imread("c.jpg")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# Find Contours 
blurred = cv2.GaussianBlur(resized, (5, 5), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(resized, cv2.COLOR_BGR2LAB)
thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)[1]
imagem = cv2.bitwise_not(thresh)
th4 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,2)
cv2.imshow("Thresh", thresh)
cv2.imshow("adaptiveThreshold", th3)
cv2.imshow("THRESH_OTSU", th4)
#cv2.imshow("Lab", lab)
cv2.imshow("Imagem", imagem)
cv2.imshow("Blurred", blurred)
cv2.imshow("Gray", gray)
cnts = cv2.findContours(imagem.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]


# loop over the contours
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	if M["m00"] != 0:
	    cX = int(M["m10"] / M["m00"])
	    cY = int(M["m01"] / M["m00"])
	else:
	    cX, cY = 0, 0

	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape and labeled
	# color on the image
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.circle(image, (cX, cY), 50, (0, 255, 0), 3)

	cv2.drawContours(image, [c], 0, (0, 255, 0), 3)

	# show the output image
	cv2.imshow("Image", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
