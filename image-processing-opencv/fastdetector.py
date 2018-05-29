import cv2 
import numpy as np

img = cv2.imread('input1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create()

kps = fast.detect(gray, None)
blank = np.zeros((1, 1))
print('No. of keypoint Detected: ', len(kps))

img = cv2.drawKeypoints(img, kps, blank, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()