import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt


# Read image
# src = cv2.imread("black.jpg")


cap = cv2.VideoCapture(1)

while(True):
# Capture frame-by-frame
	ret, image = cap.read()

#image = cv2.imread("c.jpg")
#resized = imutils.resize(image, width=300)
	#ratio = image.shape[0] / float(resized.shape[0])

	# Find Contours 
	blurred = cv2.GaussianBlur(image, (5, 5), 0)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
	imagem = cv2.bitwise_not(gray)
	thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
	#th4 = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
	th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("adaptiveThreshold", th3)
	#cv2.imshow("THRESH_OTSU", th4)
	cv2.imshow("Lab", lab)
	cv2.imshow("Imagem", imagem)
	cv2.imshow("Blurred", blurred)
	cv2.imshow("Gray", gray)
	# show the output image
	cv2.imshow("Image", image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]



cap.release()
cv2.destroyAllWindows()
