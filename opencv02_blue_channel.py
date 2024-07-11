# -*- coding: utf-8 -*-
import cv2

img=cv2.imread('onepiece.jpg')
b=img[:,:,0]#冒號，冒號，0 藍色
cv2.imshow('blue',b)
cv2.waitKey(0)#K是大寫