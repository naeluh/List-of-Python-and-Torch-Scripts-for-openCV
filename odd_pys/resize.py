import cv2

def process(filename, key):

    image = cv2.imread(filename)

    print image.shape

    r = 100.0 / image.shape[1]
    dim = (100, int(image.shape[0] *r))

    imageresized = cv2.resize(image,(300,300),dim,interpolation = cv2.INTER_AREA)

    cv2.imwrite( 'imageresized_{}.jpg'.format(key) ,imageresized )
    print 'imageresized_{}.jpg'.format(key)