"""
Basic Functions of OpenCV for handling images and Videos.
"""

import cv2
import numpy as np

img = cv2.imread('data/sammy.jpg')
kernel = np.ones((5, 5), np.uint8)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
img_canny = cv2.Canny(img_gray, 100, 100)
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)
img_erode = cv2.erode(img_canny, kernel, iterations=1)

cv2.imshow('Gray Image', img_gray)
cv2.imshow('Blur Image', img_blur)
cv2.imshow('Canny Image', img_canny)
cv2.imshow('Dilation Image', img_dilation)
cv2.imshow('Erode Image', img_erode)
cv2.waitKey(0)
