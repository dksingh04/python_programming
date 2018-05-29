import cv2
import numpy as np

beachImage = cv2.imread('WaldoBeach.jpg')

cv2.imshow("Where is Waldo?", beachImage)
gray = cv2.cvtColor(beachImage, cv2.COLOR_BGR2GRAY)

cv2.waitKey(0)

templateImg = cv2.imread('waldo.jpg', 0)

result = cv2.matchTemplate(gray, templateImg,cv2.TM_CCOEFF)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv2.rectangle(beachImage, top_left, bottom_right, (0,0,255), 2)

cv2.imshow('Where is Waldo?', beachImage)

cv2.waitKey(0)

cv2.destroyAllWindows()

