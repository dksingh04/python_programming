import cv2
import numpy as np

img = cv2.imread('hand.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", img)
cv2.waitKey(0)
ret, thresh = cv2.threshold(gray, 176, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshhold Image", thresh)
cv2.waitKey(0)
image, contours, hirearchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("Conrours Image", image)
cv2.waitKey(0)

#sort Contours by areay
n = len(contours) - 1
contours = sorted(contours, key=cv2.contourArea, reverse=False)[:n]

for c in contours:
    hull = cv2.convexHull(c)
    cv2.drawContours(img, [hull], 0, (0, 255, 0), 2)
    cv2.imshow("Hull", img)

cv2.waitKey(0)
cv2.destroyAllWindows() 

