'''
Created on 27/01/2016

@author: Jesus Gutierrez Barajas
'''

import cv2

taj = cv2.imread('taj_mahal.jpg')

erosion = cv2.erode(taj, (5,5 ), iterations = 9)
dilation = cv2.dilate(taj, (5, 5), iterations = 9)
opening = cv2.morphologyEx(taj, cv2.MORPH_OPEN, (5, 5), iterations = 9)
closing = cv2.morphologyEx(taj, cv2.MORPH_CLOSE, (5, 5), iterations = 9)

cv2.imshow('Original', taj)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)

cv2.waitKey()