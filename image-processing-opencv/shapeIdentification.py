import cv2
import numpy as np

shapeImg = cv2.imread('someshapes.jpg')
gray = cv2.cvtColor(shapeImg, cv2.COLOR_BGR2GRAY)

cv2.imshow('Identifying Shapes',shapeImg)
cv2.waitKey(0)

ret, thresh = cv2.threshold(gray, 127, 255, 1)

# Extract Contours
img, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for c in contours:
    polyPoints = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c, True), True)

    numOfPoints = len(polyPoints)
    print(numOfPoints)
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    if numOfPoints == 3:
        shapeName="Triangle"
        cv2.drawContours(shapeImg,[c],0,(0,255,0),-1)
        # Find contour center to place text at the center
        cv2.putText(shapeImg, shapeName, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif numOfPoints == 4:
        x, y, w, h = cv2.boundingRect(c)
        if abs(w-h) <= 3:
            shapeName="Square"
            cv2.drawContours(shapeImg, [c], 0, (0, 125 ,255), -1)
            cv2.putText(shapeImg, shapeName, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        else:
            shapeName="Rectangle"
            cv2.drawContours(shapeImg, [c], 0, (0, 0 ,255), -1)
            cv2.putText(shapeImg, shapeName, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif numOfPoints == 10:
        shapeName="Star"
        cv2.drawContours(shapeImg, [c], 0, (255, 255, 0), -1)
        cv2.putText(shapeImg, shapeName, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif numOfPoints >=15:
        shapeName="Circle"
        cv2.drawContours(shapeImg, [c], 0, (0, 255, 255), -1)
        cv2.putText(shapeImg, shapeName, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        
    
    cv2.imshow('Identifying Shapes',shapeImg)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()

        
