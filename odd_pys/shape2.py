import cv2

# Read image
src = cv2.imread("c.jpg")

imgray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

# Set threshold and maxValue
thresh = 200
maxValue = 255

# Basic threshold example
th, dst = cv2.threshold(imgray, thresh, maxValue, cv2.THRESH_BINARY);

# Find Contours 
_,countours,hierarchy=cv2.findContours(dst,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# Draw Contour
cv2.drawContours(dst,countours,-1,(255,255,255),3)

cv2.imshow("Contour",dst)
cv2.waitKey(0)

