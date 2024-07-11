# -*- coding: utf-8 -*-
import cv2

img=cv2.imread('onepiece.jpg')
b=img[:,:,0]#冒號，冒號，0 藍色
g=img[:,:,1]#冒號，冒號，0 綠色
r=img[:,:,2]#冒號，冒號，0 紅色

img_rbb=cv2.merge([r,b,b])
cv2.imwrite('rbb.jpg',img_rbb)
cv2.imshow('RBB',img_rbb)
cv2.imshow('opencv04',img)


cv2.waitKey(0)#K是大寫
#如果按下任意鍵，要把全部的視窗關閉
cv2.destroyAllWindows()#會把全部視窗關閉