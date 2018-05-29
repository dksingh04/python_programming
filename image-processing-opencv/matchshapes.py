import cv2
import numpy as np

#load shape template
template = cv2.imread('4star.jpg')
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
cv2.imshow("Template", template)
cv2.waitKey(0)

targetImg = cv2.imread('shapestomatch.jpg')
target_gray = cv2.cvtColor(targetImg, cv2.COLOR_BGR2GRAY)

# Threshold both images first before using cv2.findContours
ret, thresh1 = cv2.threshold(template_gray, 127, 255, 0)
ret, thresh2 = cv2.threshold(target_gray, 127, 255, 0)

#find the contours in template image
img, contours, hirearchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

#sort contours
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

template_contour=contours[1]

#find the contours in template image
img2, contours, hirearchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    match = cv2.matchShapes(template_contour, c, 3, 0.0)
    print (match)
    if match < 0.15:
        closest_contour = c
    else:
        closest_contour = []
    

cv2.drawContours(targetImg, [closest_contour], -1, (0,255,0), 3)
cv2.imshow('Output', targetImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

