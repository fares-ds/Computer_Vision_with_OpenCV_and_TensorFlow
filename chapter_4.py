"""
Shapes and Texts, How to draw shapes on images?
"""

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img[:] = 100, 150, 120

cv2.line(img, (0, 0), (512, 512), color=(0, 255, 0), thickness=5)
cv2.rectangle(img, (200, 200), (300, 300), (255, 0, 0), thickness=-1)
cv2.circle(img, (100, 400), 30, (255, 155, 0), thickness=5)
cv2.putText(img, "OPENCV", (375, 505), cv2.FONT_HERSHEY_COMPLEX, 1, (155, 40, 40), thickness=2)

print(img.shape)
cv2.imshow('Image', img)

cv2.waitKey()
