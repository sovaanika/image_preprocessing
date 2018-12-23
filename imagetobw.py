import cv2
#import numpy as np
color_image = cv2.imread("3.jpg")

color_image_b = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit= 3., tileGridSize=(8,8))
lab = cv2.cvtColor(color_image, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
l2 = clahe.apply(l)
lab = cv2.merge((l2,a,b))
img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('contrast', img2)
cv2.imshow('GRAY', color_image_b)
cv2.imwrite('conntrast.jpg', img2)
cv2.waitKey(0)