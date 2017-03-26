import numpy as np
import cv2 #this is the main openCV class, the python binding file should be in /pythonXX/Lib/site-packages
from matplotlib import pyplot as plt

gwash = cv2.imread("imageresized_6.jpg") #import image
#blurred = cv2.GaussianBlur(gwash, (5, 5), 0)
gwashBW = cv2.cvtColor(gwash, cv2.COLOR_BGR2GRAY) #change to grayscale

#plt.imshow(gwashBW, 'gray') #this is matplotlib solution (Figure 1)
#plt.xticks([]), plt.yticks([])
#plt.show()

#cv2.imshow('gwash', gwashBW) #this is for native openCV display
#cv2.waitKey(0) 

ret,thresh1 = cv2.threshold(gwashBW,179,255,cv2.THRESH_BINARY) #the value of 15 is chosen by trial-and-error to produce the best outline of the skull
kernel = np.ones((5,5),np.uint8) #square image kernel used for erosion
erosion = cv2.erode(thresh1, kernel,iterations = 1) #refines all edges in the binary image
#dialate = cv2.dialate(thresh1, kernel,iterations = 1) #refines all edges in the binary image

opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel) #this is for further removing small noises and holes in the image

#plt.imshow(closing, 'gray') #Figure 2
#plt.xticks([]), plt.yticks([])
#plt.show() 

_ , contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find contours with simple approximation
#cv2.imshow('cleaner', closing) #Figure 3
cv2.drawContours(closing, contours, -1, (255, 255, 255), 4)
#cv2.waitKey(0)

areas = [] #list to hold all areas

for contour in contours:
  ar = cv2.contourArea(contour)
  areas.append(ar)

max_area = max(areas)
max_area_index = areas.index(max_area) #index of the list element with largest area

cnt = contours[max_area_index] #largest area contour
gray = np.float32(closing)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
gwash[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',gwash)
cv2.imwrite('dst.png',gwash)
cv2.drawContours(closing, [cnt], 0, (255, 255, 255), 3, maxLevel = 0)
cv2.imshow('cleaner2.png', closing)
cv2.imwrite('cleaner2.png', closing)
#cv2.imwrite('cleaner2.png', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
