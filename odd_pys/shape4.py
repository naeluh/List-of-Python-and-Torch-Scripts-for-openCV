import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

def processImage(img):
   img = cv2.imread(img)
   resized = imutils.resize(image, width=300)
	
   return img


# Read image
# src = cv2.imread("black.jpg")

image = cv2.imread("c.jpg")

image2 = cv2.imread("c.jpg")

resized = imutils.resize(image, width=300)

ratio = image.shape[0] / float(resized.shape[0])

# Find Contours 
blurred = cv2.GaussianBlur(resized, (5, 5), 0)

gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

lab = cv2.cvtColor(resized, cv2.COLOR_BGR2LAB)

thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

imagem = cv2.bitwise_not(thresh)

th4 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

gray_2 = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)

thresh_2 = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 1)

kernel = np.ones((3, 3), np.uint8)

closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=4)




cv2.imshow("Thresh", thresh)

cv2.imshow("adaptiveThreshold", th3)

cv2.imshow("THRESH_OTSU", th4)

cv2.imshow("Lab", lab)

cv2.imshow("Blurred", blurred)

cv2.imshow("Gray", gray)

cv2.imshow("closing", closing)

cv2.imshow("thresh_2", thresh_2)

cv2.imshow("gray_blur", gray_blur)

cv2.imshow("gray_2", gray_2)

cv2.imshow("Imagem", imagem)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnts2 = cv2.findContours(closing.copy(), cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if imutils.is_cv2() else cnts[1]

cnts2 = cnts2[0] if imutils.is_cv2() else cnts2[1]

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

cv2.imshow("Image", image)

	# loop over the contours
for c2 in cnts2:
	# compute the center of the contour
	M2 = cv2.moments(c2)
	if M["m00"] != 0:
	    c2X = int(M2["m10"] / M2["m00"])
	    c2Y = int(M2["m01"] / M2["m00"])
	else:
	    c2X, c2Y = 0, 0

	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape and labeled
	# color on the image
	c2 = c2.astype("float")
	c2 *= ratio
	c2 = c2.astype("int")
	cv2.drawContours(closing, [c2], -1, (0, 255, 255), 1)

	# show the output image

cv2.imshow("Image2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
