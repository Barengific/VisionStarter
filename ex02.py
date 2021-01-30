# -*- coding: utf-8 -*-
"""

@author: barengific
"""
#read and view video files

import numpy as np
import cv2

cap = cv2.VideoCapture(r'D:\Python\JJ.mp4')

if cap.isOpened() == False:
    print('cannot proceed')
    
while True:
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow('Frame', frame)
        
        if cv2.waitKey(25) & 0xFF == 27:
            break
    else:
        break
    

cap.release()
cv2.destroyAllWindows()      