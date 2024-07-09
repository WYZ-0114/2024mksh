# -*- coding: utf-8 -*-
import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    cv2.imshow('opencv08',img)
    #1000ms1秒
    #33ms對應1/30秒(每秒30張)
    if cv2.waitKey(33)==27:
        break#27對應ESC鍵
        
cv2.destoryAllWindow()
