import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

def process(filename, key):
    image = cv2.imread(filename)

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

    print image.shape

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
        # use cropped mask image (roi) to get rid of all small pieces
        QR_final = QR_crop * (roi/255)
    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    resized = imutils.resize(QR_final, width=600)
    ratio = QR_final.shape[0] / float(resized.shape[0])
    blurred = cv2.GaussianBlur(resized, (5, 5), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    lab = cv2.cvtColor(resized, cv2.COLOR_BGR2LAB)
    thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)[1]
    imagem = cv2.bitwise_not(thresh)
    th4 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    gray_2 = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
    thresh_2 = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 1)
    kernel = np.ones((1, 1), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=500)
    cnts = cv2.findContours(closing.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
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
          cX *= ratio
          cY *= ratio
          cv2.drawContours(QR_final, [c], -1, (0, 255, 0), 5)
          cv2.circle(QR_final, (int(cX),int(cY)),5,300,3)  

    #r = 100.0 / image.shape[1]
    #dim = (100, int(image.shape[0] *r))

    #imageresized = cv2.resize(image,(2048,2048),dim,interpolation = cv2.INTER_AREA)
    cv2.imwrite( 'i/image_{}.jpg'.format(key) ,QR_final )
    print 'image_{}.jpg'.format(key) 