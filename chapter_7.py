"""
Chapter 7: Color detection
"""

import cv2
import numpy as np


def empty(a):
    pass


def stack_images(scale, img_array):
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(img_array[x][y], (0, 0), None, scale, scale)
                else:
                    img_array[x][y] = cv2.resize(img_array[x][y], (img_array[0][0].shape[1], img_array[0][0].shape[0]),
                                                 None, scale, scale)
                if len(img_array[x][y].shape) == 2: img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank] * rows
        hor_con = [image_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv2.resize(img_array[x], (img_array[0].shape[1], img_array[0].shape[0]), None, scale,
                                          scale)
            if len(img_array[x].shape) == 2: img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver


path = 'data/sammy_face.jpg'
cv2.namedWindow('Track Bars')
cv2.resizeWindow('Track Bars', 640, 240)
cv2.createTrackbar('Hue Min', 'Track Bars', 85, 179, empty)
cv2.createTrackbar('Hue Max', 'Track Bars', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'Track Bars', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'Track Bars', 255, 255, empty)
cv2.createTrackbar('Val Min', 'Track Bars', 60, 255, empty)
cv2.createTrackbar('Val Max', 'Track Bars', 255, 255, empty)

while True:
    img = cv2.imread(path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'Track Bars')
    h_max = cv2.getTrackbarPos('Hue Max', 'Track Bars')
    s_min = cv2.getTrackbarPos('Sat Min', 'Track Bars')
    s_max = cv2.getTrackbarPos('Sat Max', 'Track Bars')
    v_min = cv2.getTrackbarPos('Val Min', 'Track Bars')
    v_max = cv2.getTrackbarPos('Val Max', 'Track Bars')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_hsv, lower, upper)
    img_result = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow('Original', img)
    # cv2.imshow('HSV image', img_hsv)
    # cv2.imshow('Mask', mask)
    # cv2.imshow('Dog mask', img_result)

    stack_img = stack_images(0.7, [[img, img_hsv], [mask, img_result]])
    cv2.imshow('Images', stack_img)
    cv2.waitKey(1)
