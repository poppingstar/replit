"""
1. 허프 변환이란 끊긴 엣지를 모아 직선 또는 원 등을 검출하는 방법으로

"""
""" 
2.
"""

import cv2 as cv    #

img=cv.imread('hough.jpg')  
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#입력 이미지와 동일한 해상도로, 감지된 원 사이의 최소 거리는 200,
apples=cv.HoughCircles(gray,cv.HOUGH_GRADIENT, 1, 200, param1=150,param2=20,minRadius=50,maxRadius=120) 

for i in apples[0]:
    cv.circle(img,int(i[0]),int(i[1]),int(i[2]),(255,0,0),2)    
    
cv.imshow("Apple detection",img)  #detection된 이미지 출력

cv.waitKey()    #입력 대기
cv.destroyAllWindows()  #모든 윈도우 닫기

""" 
4.NMS
"""
