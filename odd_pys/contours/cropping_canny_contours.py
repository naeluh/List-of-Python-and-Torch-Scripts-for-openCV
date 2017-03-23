import cv2 
import numpy
import imutils
image = cv2.imread("imageresized_0.jpg")
resized = imutils.resize(image, width=600)
ratio = image.shape[0] / float(resized.shape[0])
blurred = cv2.GaussianBlur(resized, (7, 7), 0)
gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 180 , 255, cv2.THRESH_BINARY)[1]
kernel = numpy.ones((1, 1), numpy.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=500)
edged = cv2.Canny(closing, 100, 250)
cv2.imshow("closing", closing)
cv2.imshow("edged",edged)
cv2.imshow("image",image)
cnts = cv2.findContours(closing.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
idx = 0
for c in cnts:
	x,y,w,h = cv2.boundingRect(c)
	if w>50 and h>50:
		idx+=1
		new_img=image[y:y+h,x:x+w]
		#cv2.imwrite(str(idx) + '.png', new_img)
cv2.imshow("im",new_img)
cv2.waitKey(0)