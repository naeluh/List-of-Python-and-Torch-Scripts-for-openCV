import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

# Callback Function for Trackbar (but do not any work)
def nothing(*arg):
    pass

# Code here
def SimpleTrackbar(Image, WindowName):
 # Generate trackbar Window Name
 TrackbarName = WindowName + "Trackbar"
 TrackbarNameBlur = WindowName + 'TrackbarBlur'
 # Make Window and Trackbar
 cv2.namedWindow(WindowName)
 cv2.createTrackbar(TrackbarName, WindowName, 0, 255, nothing)
 cv2.createTrackbar(TrackbarNameBlur, WindowName, 1, 55, nothing)
 hh = 'Hue High'
 hl = 'Hue Low'
 sh = 'Saturation High'
 sl = 'Saturation Low'
 vh = 'Value High'
 vl = 'Value Low'
 cv2.createTrackbar(hl, WindowName, 0, 179, nothing)
 cv2.createTrackbar(hh, WindowName, 0, 179, nothing)
 cv2.createTrackbar(sl, WindowName, 0, 255, nothing)
 cv2.createTrackbar(sh, WindowName, 0, 255, nothing)
 cv2.createTrackbar(vl, WindowName, 0, 255, nothing)
 cv2.createTrackbar(vh, WindowName, 0, 255, nothing)
 # Allocate destination image
 Threshold = np.zeros(Image.shape, np.uint8)

 # Loop for get trackbar pos and process it
 while True:
  # Get position in trackbar
  TrackbarPos = cv2.getTrackbarPos(TrackbarName, WindowName)
  hsv = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
  TrackbarPosBlur = cv2.getTrackbarPos(TrackbarNameBlur, WindowName)
  hul = cv2.getTrackbarPos(hl, WindowName)
  huh = cv2.getTrackbarPos(hh, WindowName)
  sal = cv2.getTrackbarPos(sl, WindowName)
  sah = cv2.getTrackbarPos(sh, WindowName)
  val = cv2.getTrackbarPos(vl, WindowName)
  vah = cv2.getTrackbarPos(vh, WindowName)
  #make array for final values
  HSVLOW=np.array([hul,sal,val])
  HSVHIGH=np.array([huh,sah,vah])
  #create a mask for that range
  mask = cv2.inRange(hsv,HSVLOW, HSVHIGH)
  # Apply threshold
  if TrackbarPosBlur % 2 == 1:
    cv2.GaussianBlur(Image, (TrackbarPosBlur, TrackbarPosBlur), 0 , Threshold)
  cv2.threshold(Image, TrackbarPos, 255, cv2.THRESH_BINARY, Threshold)
  # Show in window
  res = cv2.bitwise_and(Image, Image, mask = mask)
  #cv2.imshow(WindowName, res)
  cv2.imshow(WindowName, Threshold)

  # If you press "ESC", it will return value
  ch = cv2.waitKey(5)
  if ch == 27:
      break

 cv2.destroyAllWindows()
 return Threshold

WindowName = 'Thresh1'
Image = cv2.imread('c.jpg')

SimpleTrackbar(Image, WindowName)