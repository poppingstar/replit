"""
1. 허프 변환이란 끊긴 엣지를 모아 직선 또는 원 등을 검출하는 방법으로 (b,a)공간을 이산화하고 누적 배열을 만든다. 이후 이후 각 점에 대한 직선이
지나는 길을 투표로 누적 배열에 기록하고, 다수의 표를 얻은 점을 결정할 때 비최대 억제를 적용하여 지역 최대점을 찾는다
"""
""" 
2. RANSAC은 전체 데이터에서 일부 샘플을 선택한 뒤, 이를 inliner로 가정하여 모델을 예측하고
 이렇게 예측된 파라미터에 임계값을 일부 첨가하여 임계값 범위 이내에 있는 데이터들을 inlier로 판단한다.
 데이터 셋에서 inliner의 수를 센 후 최대값일때마다 파라미터를 새로 저장하는것을 정해진 횟수까지 반복한다.
 이러한 방식으로 작동하기에, outlier가 모델을 이루는 경우 잘못된 결과를 출력할 수 있고, 항상 같은 결과를 보장하지도 않는다
"""

import cv2 as cv    # cv라는 별명으로 opencv 사용

img=cv.imread('hough.jpg')  #이미지 불러오기
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #  grayscale로 변환

#허프 변환을 사용하여 이미지에서 원을 검출, 입력 이미지와 동일한 해상도로, 감지된 원 사이의 최소 거리는 200, 엣지 검출 상한은 150
#허프 변환 임계값은 40, 원의 최소 반지름은 50, 최대 반지름은 120
apples=cv.HoughCircles(gray,cv.HOUGH_GRADIENT, 1, 1, param1=150,param2=40,minRadius=50,maxRadius=120) 

# 원의 중심, 반지름, 색상, 두께를 입력 받아 이미지에 원을 그림
for i in apples[0]:
    cv.circle(img,(int(i[0]),int(i[1])),int(i[2]),(255,0,0),2)    
"""
i=apples[0][0]
for _ in range(10):
    cv.circle(img,(int(i[0]),int(i[1])),int(i[2]),(255,0,0),2)
"""
    
cv.imshow("Apple detection",img)  #detection된 이미지 출력

cv.waitKey()    #입력 대기
cv.destroyAllWindows()  #모든 윈도우 닫기

""" 
4.input image가 object detection 모델을 통과하면, 각 object에 여러 개의 bounding box가 생성되는데,
각 object의 bouning box들 중 가장 스코어가 높은 박스만 남기고 나머지를 제거하는 방법이 NMS다.
Bounding box list에서 가장 점수가 높은 박스를 선택하고 최종 제안 목록에 추가한 후, IOU가 임계값보다 높은 경우 list에서 제거하는 것을 list가 빌때까지 반복한다.
"""
