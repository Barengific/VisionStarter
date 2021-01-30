# -*- coding: utf-8 -*-
"""

@author: barengific
"""

import numpy as np
import cv2

#classification test for video

cap = cv2.VideoCapture(r'D:\Python\JJ.mp4')

rows = open(r'D:\Python\words.txt').read().strip().split("\n")

clas = [r[r.find(' ') + 1: ] for r in rows]

net = cv2.dnn.readNetFromCaffe(r'D:\Python\googlenet.prototxt',r'D:\Python\googlenet.caffemodel')

if cap.isOpened() == False:
    print('cannot proceed')
    
while True:
    ret, frame = cap.read()
    
    blob = cv2.dnn.blobFromImage(frame,1,(224,224))

    net.setInput(blob)

    out = net.forward()
    
    r=1
    for i in np.argsort(out[0])[::-1][:5]:
        txt = ' "%s" probability "%.3f" ' % (clas[i], out[0][i] * 100)
        cv2.putText(frame, txt, (0, 25 + 40*r), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        r+=1
        
    if ret == True:
        cv2.imshow('Frame', frame)
        
        if cv2.waitKey(25) & 0xFF == 27:
            break
    else:
        break
    

cap.release()
cv2.destroyAllWindows()      