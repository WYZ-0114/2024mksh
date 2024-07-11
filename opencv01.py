# -*- coding: utf-8 -*-
import cv2#使用Opencv的cv2外掛
#匯入cv2
img=cv2.imread('onepiece.jpg')
#讀入opencv.png這張圖，小心副檔名
cv2.imshow('opencv01',img)#要在'opencv01'視窗裡秀圖
cv2.imshow('Hollo',img)#要在'one'秀圖
cv2.imshow('mksh',img)#要在'one'秀圖
cv2.waitKey(0)#等待任意鍵，卡住，不要結束
#File-New Ctrl-N 開新檔
#File-Save as 另存新檔
#Win+E 開啟檔案總管
#存在桌面上的opencv01
#先寫好，不要執行，因為沒有圖，執行會當機
#圖也要放在同個桌面目錄