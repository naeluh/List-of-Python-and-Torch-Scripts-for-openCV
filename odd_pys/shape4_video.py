import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt


# Read image
# src = cv2.imread("black.jpg")


cap = cv2.VideoCapture(1)

width = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
height = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)



while(True):

# Capture frame-by-frame
	ret, image = cap.read()

#image = cv2.imread("c.jpg")
#resized = imutils.resize(image, width=300)
	ratio = 640/480

	# Find Contours 
	blurred = cv2.GaussianBlur(image, (5, 5), 0)
	gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
	lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
	imagem = cv2.bitwise_not(gray)
	thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
	th4 = thr = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)[1]
	th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
	add = cv2.add(lab , image)
	cv2.line(lab,(0,0),(150,150),(255,255,255),15)
	cv2.moveWindow("add", 0, 0)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("add", add)
	cv2.imshow("adaptiveThreshold", th3)
	cv2.imshow("THRESH_OTSU", th4)
	cv2.imshow("Lab", lab)
	cv2.imshow("Imagem", imagem)
	cv2.imshow("Blurred", blurred)
	cv2.imshow("Gray", gray)
	# show the output image

	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

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
	cv2.drawContours(image, [c], 0, (0, 255, 0), 3)


	cv2.imshow("Image", image)










cap.release()
cv2.destroyAllWindows()
