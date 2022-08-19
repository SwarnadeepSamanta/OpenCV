import cv2
import numpy as np

img = cv2.imread('img_vid\cartoon.jpg')
size = 30
kernel = np.zeros((size, size))
kernel[int((size - 1) / 2), :] = np.ones(size)
kernel = kernel / size

out = cv2.filter2D(img, -1, kernel)
cv2.imshow('original', img)
cv2.imshow('Motion blurr', out)
cv2.waitKey(0)
