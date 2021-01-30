# -*- coding: utf-8 -*-
"""

@author: barengific
"""

import numpy as np
import cv2

#classification test for image

img = cv2.imread(r'D:\Python\Mountain.jpeg')
#print(type(img))
#print(img)
#print(img.shape)

rows = open(r'D:\Python\words.txt').read().strip().split("\n")

clas = [r[r.find(' ') + 1: ] for r in rows]

net = cv2.dnn.readNetFromCaffe(r'D:\Python\googlenet.prototxt',r'D:\Python\googlenet.caffemodel')

blob = cv2.dnn.blobFromImage(img,1,(224,224))

net.setInput(blob)

out = net.forward()

#print(out)

idx = np.argsort(out[0])[::-1][:5]

for(i,id) in enumerate(idx):
    print('{}. {} ({}): Probability {:.3}%'.format(i+1, clas[id], id, out[0][id]*100))

#cv2.imshow('Image', img)
#cv2.waitKey(0)

