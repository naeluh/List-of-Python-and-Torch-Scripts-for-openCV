import cv2

def process(filename, key):

    image = cv2.imread(filename)

    print image.shape

    r = 1024.0 / image.shape[1]
    dim = (1024, int(image.shape[0] *r))

    imageresized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)

    cv2.imwrite( 'imageresized_{}.jpg'.format(key) ,imageresized )
    print 'imageresized_{}.jpg'.format(key) 