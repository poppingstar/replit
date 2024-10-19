""" 
tw=[[1,2,3,4,5,6,],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]

for list in tw:
  print(list)

print('----------------------------')
for q,w,e,r,t,y in tw:
  print(q,w,e,r,t,y)
"""
import cv2 as cv
import tensorflow as tf

print(tf.__version__)

a=cv.imread('child.png')
print(a)
cv.imshow('child.png', a)