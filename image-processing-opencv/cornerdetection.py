import cv2 
import numpy as np

image = cv2.imread("scan.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


'''gray = np.float32(gray)

harris_corner = cv2.cornerHarris(gray, 27, 27, 0.05)
kernal = np.ones((7,7), np.uint8)
harris_corner = cv2.dilate(harris_corner, kernal, iterations=1)

print(harris_corner)
# Threshold for an optimal value, it may vary depending on the image.
image[harris_corner > 0.025 * harris_corner.max() ] = [255, 127, 127]

cv2.imshow('Harris Corners', image)
'''

# We specific the top 50 corners
corners = cv2.goodFeaturesToTrack(gray, 10, 0.01, 150)

for corner in corners:
    x, y = corner[0]
    x = int(x)
    y = int(y)
    cv2.rectangle(image,(x-10,y-10),(x+10,y+10),(0,255,0), 2)
    
cv2.imshow("Corners Found", image)

cv2.waitKey(0)
cv2.destroyAllWindows()