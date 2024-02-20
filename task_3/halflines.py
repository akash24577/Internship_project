import cv2
import numpy as np
img=cv2.imread("D:/Intern/task_3/sudoku.jpg")
# img = cv2.resize(img, None, fx=0.7, fy=0.7)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow('edges', edges)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imshow('image', gray)
# cv2.waitKey(0)