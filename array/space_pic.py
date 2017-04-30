import cv2
from datetime import datetime

#t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cam0 = cv2.VideoCapture(1)
cam0.set(3, 1920.)
cam0.set(4, 1080.)
#cam0.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off
#cam0.set(CV_CAP_PROP_SETTINGS, 1);


#cam1 = cv2.VideoCapture(0)
#cam1.set(3, 1920.)
#cam1.set(4, 1080.)
#cam1.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off
##cam1.set(CV_CAP_PROP_SETTINGS, 1);



cv2.namedWindow("array0")
#cv2.namedWindow("array1")

img_counter = 0
img_counter1 = 0

while True:
    ret, frame = cam0.read()
    #ret1, frame1 = cam1.read()
    cv2.imshow("array0", frame)

    #cv2.imshow("array1", frame1)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        img_name = "042917/"+t+"_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1


cam0.release()

#cam1.release()

cv2.destroyAllWindows()