import cv2
import numpy as np
import imutils

# Read image
src = cv2.imread("c.jpg")

image = cv2.imread("c.jpg")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# Find Contours 
blurred = cv2.GaussianBlur(resized, (5, 5), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
imagem = cv2.bitwise_not(gray)
thresh = cv2.threshold(gray, 171, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Thresh", thresh)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
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
	cv2.drawContours(image, [c], -1, (0, 255, 0), 3)

	# show the output image
	cv2.imshow("Image", image)
	cv2.waitKey(0)
