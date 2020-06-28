"""
Chapter 9: Face Detection
"""

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
img = cv2.imread('data/solvay_conference.jpg')
img_gray = cv2.imread('data/solvay_conference.jpg', 0)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)
