from cv2 import cv2 
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('qr.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
    success, img = cap.read()
    for code in decode(img):
        myData = code.data.decode('utf-8')
        print(myData)
    cv2.imshow('Result',img)
    cv2.waitKey(1)