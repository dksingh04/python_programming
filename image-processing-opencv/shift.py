import cv2
import numpy as np

img = cv2.imread('input1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#create SIFT feature detection
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)
blank = np.zeros((1,1))
img = cv2.drawKeypoints(img, kp, blank, (0,0,255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Orginal Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
