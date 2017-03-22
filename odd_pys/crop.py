import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

image = cv2.imread("84 photos/2013-01-01 00.00.00-213.jpg")

init_resized = imutils.resize(image, width=600)
init_ratio = image.shape[0] / float(init_resized.shape[0])
init_blurred = cv2.GaussianBlur(init_resized, (5, 5), 0)
init_gray = cv2.cvtColor(init_blurred, cv2.COLOR_BGR2GRAY)
init_thresh = cv2.threshold(init_gray, 180, 255, cv2.THRESH_BINARY)[1]

QR_orig = image
QR = init_gray 
mask = np.zeros(QR.shape,np.uint8) 

init_kernel = np.ones((1, 1), np.uint8)
init_closing = cv2.morphologyEx(init_thresh, cv2.MORPH_CLOSE, init_kernel, iterations=500)
contours = cv2.findContours(init_closing.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[1]



# Choose largest contour
best = 0
maxsize = 0
count = 0
for cnts in contours:
    if cv2.contourArea(cnts) > maxsize :
        maxsize = cv2.contourArea(cnts)
        best = count

    count = count + 1
    
    x,y,w,h = cv2.boundingRect(cnts[best])
    roi=mask[y:y+h,x:x+w]
        # crop the original QR based on the ROI
    QR_crop = QR_orig[y:y+h,x:x+w]
    print QR_crop
        # use cropped mask image (roi) to get rid of all small pieces
    QR_final = QR_crop * (roi/255)

cv2.imshow( 'i/image_{}.jpg'.format(int(x)) ,QR_crop )
print 'image_{}.jpg'.format(int(x)) 

cv2.waitKey(0)
cv2.destroyAllWindows()