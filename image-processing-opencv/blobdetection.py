# Standard imports
import cv2
import numpy as np;
 
# Read image
image = cv2.imread("Sunflowers.jpg", 0)
 
# Set up the detector with default parameters.
#detector = None
 
# Detect blobs.
is_cv3 = cv2.__version__.startswith("3.")
detector = None
if is_cv3:
    detector = cv2.SimpleBlobDetector_create()
else:
    detector = cv2.SimpleBlobDetector()

keypoints = detector.detect(image)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of
# the circle corresponds to the size of blob
blank = np.zeros((1,1)) 
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,0,255),
                                      cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
 
# Show keypoints
cv2.imshow("Blobs", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()