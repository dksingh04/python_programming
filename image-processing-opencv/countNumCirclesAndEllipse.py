import cv2
import numpy as np

image = cv2.imread('blobs.jpg')
cv2.imshow('Original Image',image)
cv2.waitKey(0)
is_cv3 = cv2.__version__.startswith('3.')

detector = None

if is_cv3:
    detector = cv2.SimpleBlobDetector_create()
else:
    detector = cv2.SimpleBlobDetector()

keypoints = detector.detect(image)

blank = np.zeros((1,1)) 
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,120,255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

num_of_blobs = len(keypoints)

text = "Total Number of Blobs: "+str(num_of_blobs)
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 125, 255), 2)

cv2.imshow("Blobs Image", blobs)
cv2.waitKey(0)

params = cv2.SimpleBlobDetector_Params()

#filter by Area
params.filterByArea=True
params.minArea=100

#filter by parameter 
params.filterByCircularity=True
params.minCircularity=0.6
#params.maxCircularity=0.8 if you want to filter ellipse

# Set Convexity filtering parameters
params.filterByConvexity = False
params.minConvexity = 0.2
    
# Set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.01

if is_cv3:
    detector = cv2.SimpleBlobDetector_create(params)
else:
    detector = cv2.SimpleBlobDetector(params)

keypoints = detector.detect(image)

blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 145, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

num_of_blobs = len(keypoints)

text = "Number of Circular Blobs: " + str(num_of_blobs)

cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey(0)


cv2.destroyAllWindows()