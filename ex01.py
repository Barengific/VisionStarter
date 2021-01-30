# -*- coding: utf-8 -*-
"""

@author: barengific
"""
#image view and differnt channel views

import numpy as np
import cv2

img = cv2.imread(r'D:\Python\Nature.jpg')
print(type(img))
#print(img)
print(img.shape)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
print(b)

cv2.imshow('Image', img)
cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)
cv2.waitKey(0)

