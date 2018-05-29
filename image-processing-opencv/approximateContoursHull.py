import cv2
import numpy as np

img = cv2.imread('house.jpg')
orig_img = img.copy()

cv2.imshow("Original Image", orig_img)
cv2.waitKey(0)

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(grayImg, 127, 255,cv2.THRESH_BINARY_INV)

#Find Contours
image, contours, hirearchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(orig_img, (x,y), (x+w, y+h), (0,0,255), 2)
    cv2.imshow("With Bounding Rect", orig_img)

cv2.waitKey(0)

for c in contours:
    # Calculate accuracy as a percent of the contour perimeter
    accuracy = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, accuracy, True)
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
    cv2.imshow('Approx Poly DP', img)
    
cv2.waitKey(0)   
cv2.destroyAllWindows()


