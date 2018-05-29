import cv2
import numpy as np 

img = cv2.imread("bunchofshapes.jpg")
#create a blank image
blank_image = np.zeros((img.shape[0], img.shape[1], 3))
gr_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

orig_img = img

#Find Canny Img
edge = cv2.Canny(gr_img, 50, 200)
cv2.imshow('1 - Canny Edges', edge)
cv2.waitKey(0)

contours = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]

print("contours: "+str(len(contours)))

#Draw all contours
cv2.drawContours(blank_image, contours, -1, (0,255,0), 3)
cv2.imshow('2 - All Contours over blank image', blank_image)
cv2.waitKey(0)

# Draw all contours over blank image
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow('3 - All Contours', img)
cv2.waitKey(0)

def getAllContoursArea(contours):
    all_area = []
    for cntr in contours:
        all_area.append(cv2.contourArea(cntr))
    
    return all_area

print ("Contor Areas before sorting") 
areas = getAllContoursArea(contours)
print (areas)

sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

img = cv2.imread("bunchofshapes.jpg")
orig_img = img
for c in sorted_contours:
    cv2.drawContours(orig_img,[c], -1, (0,255,0), 3)
    cv2.waitKey(0)
    cv2.imshow('Contours by area', orig_img)

cv2.waitKey(0)   
cv2.destroyAllWindows()
