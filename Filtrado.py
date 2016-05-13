'''
Created on 25/01/2016

@author: Jesus Gutierrez Barajas
'''

import cv2

taj = cv2.imread('taj_mahal.jpg')

sobelx = cv2.Sobel(taj, cv2.CV_64F, 0, 1, ksize = 1)
sobely = cv2.Sobel(taj, cv2.CV_64F, 1, 0, ksize = 1)
laplacian = cv2.Laplacian(taj, cv2.CV_64F)
gaussian = cv2.GaussianBlur(taj, (7,7), 0)
mediana = cv2.medianBlur(taj, 5)
canny = cv2.Canny(taj, 1, 5)

cv2.imshow('Original', taj)
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Laplacian', laplacian)
cv2.imshow('Gaussian', gaussian)
cv2.imshow('Median', mediana)
cv2.imshow('Canny', canny)

cv2.waitKey()