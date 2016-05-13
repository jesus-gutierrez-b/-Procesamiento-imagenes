'''
Created on 18/01/2016

@author: Jesus Gutierrez Barajas
'''

import cv2
import numpy as np

img1 = cv2.imread('joven.jpg')
img2 = cv2.imread('mar.jpeg')

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY, 3)
bw = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                           cv2.THRESH_BINARY, 11, 0)
notbw = cv2.bitwise_not(bw)
anda = img1 & img2 # tambien se puede usar cv2.bitwise_and(img1, img2)
oro = img1 | img2 # tambien se puede usar cv2.bitwise_or(img1, img2)

res = np.hstack((img1, img2))
res2 = np.hstack((anda, oro))
res3 = np.hstack((bw, notbw))

cv2.imshow('Originals', res)
cv2.imshow('AND/OR', res2)
cv2.imshow('BW/NOT BW', res3)

cv2.waitKey()