import cv2
import numpy as np

def sketch(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #clean up image using Guassian blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    #Extarct Edge
    canny_img = cv2.Canny(img_gray_blur, 10, 70)

    # Do an invert binarize
    ret, mask = cv2.threshold(canny_img, 70, 200, cv2.THRESH_BINARY_INV)

    return mask

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("Live Sketch", sketch(frame))
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()

