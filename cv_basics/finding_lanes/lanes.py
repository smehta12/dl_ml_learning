# learning of the opencv basics from the https://www.youtube.com/watch?v=eLTLtUVuuy4

import cv2

# returns the np array
image  = cv2.imread('test_image.jpg')

cv2.imshow('result', image)
cv2.waitKey(0) # if 0 display window infinitly until an key pressed else add milliseconds in arg
