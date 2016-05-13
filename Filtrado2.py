'''
Created on 26/01/2016

@author: JesusAlberto
'''

import cv2

taj = cv2.imread('taj_mahal.jpg')
text = cv2.imread('taj_mahal_texto.jpg')
back = cv2.imread('taj_mahal_fondo.jpg')

taj_text= (taj & cv2.bitwise_not(back)) | (text & back)
suma = cv2.GaussianBlur(taj + taj, (5, 5), 0)
resta = cv2.GaussianBlur(taj - taj, (5, 5), 0)
multi = cv2.GaussianBlur(taj * taj, (5, 5), 0)
divi = cv2.GaussianBlur(taj / taj, (5, 5), 0)
comb = cv2.GaussianBlur((taj / taj)/2 + 128, (5, 5), 0)

cv2.imshow('Texto', taj_text)
cv2.imshow('Original', taj)
cv2.imshow('Suma', suma)
cv2.imshow('Resta', resta)
cv2.imshow('Multiplicacion', multi)
cv2.imshow('Division', divi)
cv2.imshow('Combinacion', comb)

cv2.waitKey()