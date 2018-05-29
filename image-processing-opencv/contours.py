import cv2
import numpy as np

img = cv2.imread("scan.jpg")
cv2.imshow('Input Image', img)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Find canny Edge
canny = cv2.Canny(img_gray, 30, 200)
cv2.imshow('Canny Image', canny)
cv2.waitKey(0)

#Find contours
contours = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
cv2.imshow('Canny Edges After Contouring', canny)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))
print(contours)
# Draw all contours
# Use '-1' as the 3rd parameter to draw all
#ctr = np.array(contours).reshape((contours.shape(0),1,3)).astype(np.int32)
cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
