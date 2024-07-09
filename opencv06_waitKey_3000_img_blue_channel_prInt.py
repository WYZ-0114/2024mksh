# -*- coding: utf-8 -*-
import cv2
#先把圖檔放在同一個目錄
#小心副檔名
img=cv2.imread('01.jpg')
b=img[:,:,0]#藍色channel
print(b)
cv2.imshow('opencv06',img)
cv2.waitKey(3000)#等按空白鍵
#等3秒後，都沒按鍵，就離開
cv2.destroyAllWindows()#再關閉視窗