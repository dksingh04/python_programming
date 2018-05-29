import cv2
import numpy as np

img = cv2.imread('input1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create(500)
#surf.hessianThreshold = 500

kps, descriptors = surf.detectAndCompute(gray, None)

print('No. of keypoint Detected: ', len(kps))
blank = np.zeros((1, 1))
print(blank)
img = cv2.drawKeypoints(img, kps, blank, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
