import numpy as np
import cv2

def process(filename, key):
	gwash = cv2.imread(filename)# Read in your image	
	#blur = cv2.bilateralFilter(img,9,75,75)
	gwashBW = cv2.cvtColor(gwash, cv2.COLOR_BGR2GRAY) #change to grayscale

	ret,thresh1 = cv2.threshold(gwashBW,179,255,cv2.THRESH_BINARY) #the value of 15 is chosen by trial-and-error to produce the best outline of the skull
	kernel = np.ones((1,1),np.uint8) #square image kernel used for erosion
	erosion = cv2.erode(thresh1, kernel,iterations = 1) #refines all edges in the binary image
	opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel) #this is for further removing small noises and holes in the image
	_, contours ,_ = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find contours with simple approximation


	# Find the index of the largest contour
	areas = [cv2.contourArea(c) for c in contours]
	idx = np.argmax(areas)
	#idx = 0
	cnt = contours[idx]


	mask = np.zeros_like(gwash) # Create mask where white is what we want, black otherwise
	cv2.drawContours(mask, contours, idx, (255,255,255), -1) # Draw filled contour in mask
	out = np.zeros_like(gwash) # Extract out the object and place into output image
	out[mask == 255] = gwash[mask == 255]

	# Show the output image
	cv2.imwrite('img/out{}.jpg'.format(key),opening)
	print idx
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()