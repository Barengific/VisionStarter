# -*- coding: utf-8 -*-
"""

@author: barengific
"""
#testing class list

import numpy as np
import cv2


img = cv2.imread(r'D:\Python\land.jpg')
#print(type(img))
#print(img)
#print(img.shape)

rows = open(r'D:\Python\words.txt').read().strip().split("\n")

clas = [r[r.find(' ') + 1: ] for r in rows]

for(i,c) in enumerate(clas):
    if i==4:
        break
    print(i,c)


cv2.imshow('Image', img)
cv2.waitKey(0)

