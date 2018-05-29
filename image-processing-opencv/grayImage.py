import cv2
import numpy as np

image = cv2.imread("input_raj.jpg")
max_height = 600
max_width = 500
height, width = image.shape[:2] 

if max_height < height or max_width < width:
    #get scaling factor
    scale_factor = max_height/float(height)
    if max_width/float(width) < scale_factor:
        scale_factor = max_width/float(width)
    
    image = cv2.resize(image,None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
    
print(image.shape)
B, G, R = image[10, 50]
print(B, G, R)
cv2.imshow('Original', image)

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(grayImage.shape)
print(grayImage[0, 0])
#print(B, G, R)
cv2.imshow('Grayscale', grayImage)

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)

print(hsv_img[:, :, 1])
#HSV Image
cv2.imshow("HSV Image", hsv_img)
cv2.imshow("HSV Hue Channel", hsv_img[:, :, 0])
cv2.imshow("HSV Saturation Channel", hsv_img[:, :, 1])
cv2.imshow("HSV Value Channel", hsv_img[:, :, 2])

#RGB Image
B, G, R = cv2.split(image)
print (B.shape)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

# Let's merge the image
merged_img = cv2.merge([B, G, R])
#cv2.imshow("Merged Image", merged_img)

#Modify the image
mod_img = cv2.merge([B+100, G, R])
#cv2.imshow("Modified Image", mod_img)

zeros = np.zeros(image.shape[:2], dtype="uint8")

print(zeros.shape)

cv2.imshow("Red Merged", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green Merged", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue Merged", cv2.merge([B, zeros, zeros]))


k = cv2.waitKey(0)
if k == 27: #Esc Key
    cv2.destroyAllWindows()

if k == ord('s'):
    cv2.imwrite('DeepakGray.jpg', grayImage)
    cv2.destroyAllWindows()