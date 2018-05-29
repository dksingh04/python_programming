import cv2
import numpy as np
#import cv2 as cv

image = cv2.imread('bottlecaps.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray, 100, 170)
blur = cv2.medianBlur(gray, 5)
#cimage = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.imshow("Blur Image", blur)
cv2.waitKey(0)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.5, 20)
print(circles)
#circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1, 10)
#print(np.around(circles))
circles = np.uint64(np.around(circles))
#print(circles)
for i in circles[0,:]:
    # draw the outer circle
    #print(i)
    cv2.circle(image,(i[0], i[1]), i[2], (255, 255, 0), 2)
    
    # draw the center of the circle
    cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 3)

cv2.imshow('detected circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()