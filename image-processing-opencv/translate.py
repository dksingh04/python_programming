import cv2
import numpy as np

img = cv2.imread("input1.jpg")

height, width = img.shape[:2]
qheight, qwidth = height/4, width/4

#T = {1, 0, Tx
#     0, 1, Ty}

# T is translated Matrix
T = np.array([[1, 0, qwidth], [0, 1, qheight]])
print (T)
translated_img = cv2.warpAffine(img,T, (width, height))
cv2.imshow("Translated Image", translated_img)
cv2.waitKey()
cv2.destroyAllWindows()