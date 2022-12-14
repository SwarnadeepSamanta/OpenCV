# importing the modules
import cv2
import numpy as np

# import the image
img = cv2.imread('img_vid\lake.jpg')

# form the filters
kernel_identity = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
kernel_3 = np.ones((3, 3), dtype=np.float64)/9.0
kernel_11 = np.ones((11, 11), dtype=np.float64)/121.0

# apply the filters
output1 = cv2.filter2D(img, -1, kernel_identity)
output2 = cv2.filter2D(img, -1, kernel_3)
output3 = cv2.filter2D(img, -1, kernel_11)
# Show the images
cv2.imshow('Original image', output1)
cv2.imshow('Blurr 3', output2)
cv2.imshow('Blurr 11', output3)

cv2.waitKey()
