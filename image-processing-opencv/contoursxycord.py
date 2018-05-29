import cv2
import numpy as np

def x_cord_contours(contours):
    #Return x cordinate
    if cv2.contourArea(contours) > 10:
        M = cv2.moments(contours)
        return (int(M['m10']/M['m00']))

def label_contour_center(img, contours):
    M = cv2.moments(contours)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(img,(cx, cy), 10, (0,0,255),-1)
    return img


img = cv2.imread("bunchofshapes.jpg")
orginal_image = img.copy()
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(grayImg, 50, 200)

contours = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]

for (i, c)  in enumerate(contours):
     orig = label_contour_center(img, c)
 
cv2.imshow("4 - Contour Centers ", img)
cv2.waitKey(0)

# Sort by left to right using our x_cord_contour function
contours_left_to_right = sorted(contours, key = x_cord_contours, reverse = False)


# Labeling Contours left to right
for (i,c)  in enumerate(contours_left_to_right):
    cv2.drawContours(orginal_image, [c], -1, (0,0,255), 3)  
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.putText(orginal_image, str(i+1), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('6 - Left to Right Contour', orginal_image)
    cv2.waitKey(0)
    (x, y, w, h) = cv2.boundingRect(c)  
    
    # Let's now crop each contour and save these images
    cropped_contour = orginal_image[y:y + h, x:x + w]
    image_name = "output_shape_number_" + str(i+1) + ".jpg"
    print (image_name)
    cv2.imwrite(image_name, cropped_contour)


cv2.destroyAllWindows()

