"""
Resizing and Crapping images
"""

import cv2
import numpy as np

img = cv2.imread('data/dog_backpack.jpg')
print(img.shape)

img_cropped = img[0:200, 200:500]

img_resize = cv2.resize(img, (300, 200))
cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', img_resize)
cv2.imshow('Cropped Image', img_cropped)
cv2.waitKey(0)
