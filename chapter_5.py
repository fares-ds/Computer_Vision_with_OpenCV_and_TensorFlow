"""
Chapter 5: Wrap perspective
"""

import cv2
import numpy as np

img = cv2.imread('data/many_cereals.jpg')
width, height = 250, 350

pts1 = np.float32([[370, 150], [450, 160], [370, 275], [450, 275]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Wrapped Image", img_output)
cv2.waitKey(0)
