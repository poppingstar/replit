import cv2 as cv

Hello_world = cv.imread('Lenna.png')

cv2.putText(Hello_world, "20191469/t신민수", (0,0), cv2.FONT_HERSHEY_SIMPLEX ,1  (255,255,255), 3)
cv.imshow('image',Hello_world)