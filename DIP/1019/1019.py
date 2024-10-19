""" 
1.	비전에이전트의 개념을 작성하시오
    비전 프로그램에서 환경과 상황적 요소에 맞게 더 복잡한 상황에서 더 똑똑하게 판단을 내릴 수 있는 것이다.
    기존 비전 프로그램에 처리를 위한 다양한 조건들이 많이 들어가야 하는 경우 비전 에이전트로 확장된다
    나방만 찾아서 방제하는 드론 등이 비전 에이전트의 예시이다.
"""
""" 
2.  PyQt에 대해 설명하시오.
    PyQt란 Qt의 레이아웃에 파이썬 코드를 연결하여 GUI 프로그램을 만들 수 있게 해주는 프레임워크이다.
    시각적으로 괜찮으면서도, 프로그램을 쉽게 설계할 수 있다는 특징이 있다.
"""
"""
 4. 기계학습의 네 단계를 이야기하고 각 단계에 대해 설명하시오.
    1. 데이터셋 수집
    2. 모델 선택 or 구축
    3. 학습
    4. 추론
"""

""" 
3. 강의교안의 프로그램 6-4와 6-7을 실습하시오
 - 주석 달 것
 - 프로그램 소스코드와 실행결과 첨부할 것
 - 6-4는 traffic1.jpg, traffic2.jpg, traffic3.jpg에 대해서 실습 진행할 것
  (6-4에서 도로 이미지가 출력되지 않고 프로그램이 종료되면 경로에 한글이 포함되지 않은 곳으로 이동하여 진행할 것)
"""
import cv2 as cv
import numpy as np
from PyQt5.QtWidgets import *
import sys
import winsound

class TrafficWeak(QMainWindow): #GUI 애플리케이션 메인 윈도우 클래스 상속
    def __init__(self): 
        super().__init__()
        self.setWindowTitle('교통 약자 보호')   #윈도우 제목을  '교통약자 보호'로 설정
        self.setGeometry(200,200,700,200)       #좌표와 너비, 높이 설정
        
        #버튼 생성(표시할 텍스트, 부모 윈도우)
        signButton = QPushButton('표지판 등록', self)
        roadButton = QPushButton('도로 영상 불러옴', self)
        recognitionButton = QPushButton('인식',self)
        quitbutton = QPushButton('나가기',self)

        #레이블 생성(표시할 텍스트, 부모 윈도우)
        self.label=QLabel('환영합니다',self)
        
        #위치, 크기, 높이 설정
        signButton.setGeometry(10,10,100,30)
        roadButton.setGeometry(110,10,100,30)
        recognitionButton.setGeometry(210,10,100,30)
        quitbutton.setGeometry(510,10,100,30)
        self.label.setGeometry(10,40,600,170)
        
        #버튼이 클릭되었을때 호출될 함수 바인드
        signButton.clicked.connect(self.signFunction)
        roadButton.clicked.connect(self.roadFunction)
        recognitionButton.clicked.connect(self.recognitionFunction)
        quitbutton.clicked.connect(self.quitFunction)

        self.signFiles=[['child.png', '어린이'], ['elder.png', '노인'], ['disabled.png', '장애인']] #표지판 모델 영상
        self.signImgs=[]    #표지만 모델 영상 저장

    def signFunction(self): #표지판 등록 버튼이 눌렸을때 실행될 함수
        self.label.clear() #레이블에 표시된 텍스트 지우기
        self.label.setText('교통 약자표지판을 등록합니다.') #레이블에 표시될 텍스트 설정
        
        #signFiles의 하위 배열의 각 요소를 fname, _로 받아옴, _는 일반적으로 사용되지 않는 변수를 의미.
        for fname,_ in self.signFiles:      
            self.signImgs.append(cv.imread(fname))  #signImgs에 이미지 파일을 읽어서 추가
            cv.imshow(fname, self.signImgs[-1])    #마지막으로 추가된 이미지를 표시, 타이틀은 fname으로 설정
    
    def roadFunction(self): #도로 영상 불러오기 버튼이 눌렸을때 실행될 함수
        if self.signImgs==[]:   #signImgs가 비어있으면
            self.label.setText('먼저 표지판을 등록하세요.') #레이블에 '표지판을 등록하세요' 표시
        else:                                                  #signImgs가 비어있지 않으면
            fname=QFileDialog.getOpenFileName(self, '파일 읽기', './')  #현재 윈도우를 부모로, 대화 상자의 제목을 파일 읽기로, 초기 경로는 현재 위치
            self.roadImg=cv.imread(fname[0])    #반환된 파일 경로의 이미지를 읽어옴
            if self.roadImg is None: sys.exit('파일을 찾을 수 없습니다')    #이미지가 없을 시 예외처리

            cv.imshow('Road scene', self.roadImg)   #타이틀을 'Road scene'으로 설정하여 불러온 이미지 표시

    def recognitionFunction(self):  #인식 버튼이 눌렸을때 실행될 함수
        if self.roadImg is None:    #roadImg가 비어있으면
            self.label.setText('먼저 도로 영상을 불러오세요.')  #레이블에 '먼저 도로 영상을 불러오세요' 표시
        else:
            sift=cv.SIFT_create()   #특징점을 검출하고 디스크립터를 계산하는 SIFT 객체 생성

            KD=[]  #빈 리스트 생성
            for img in self.signImgs:   #signImgs의 각 요소를 img로 받아옴
                gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)    #img를 그레이스케일로 변환
                KD.append(sift.detectAndCompute(gray, None))   #그레이스케일로 변환된 이미지의 전체에서 특징점 검출 및 디스크립터 계산하여 KD에 추가
            grayRoad=cv.cvtColor(self.roadImg, cv.COLOR_BGR2GRAY)   #roadImg를 그레이스케일로 변환
            road_kp, road_des=sift.detectAndCompuute(grayRoad, None)    #그레이스케일로 변환된 이미지의 전체에서 특징점 검출 및 디스크립터 계산하여 각각 변수에 할당

            matcher=cv.DescriptorMatcher_create(cv.DESCRIPTOR_MATCHER_FLANNBASED)   #특징점 디스크립터를 매칭하는 객체 생성, FLANN 기반 매칭 알고리즘 사용
            GM=[]   #빈 리스트 생성
            for sign_kp, sign_des in KD:    #KD의 특징점과 디스크립터를 각각 sign_kp, sign_des로 받아옴
                knn_match=matcher.knnMatch(sign_des, road_des, 2)   #sign_des와 road_des의 매칭 결과를 knn_match에 저장, 2개의 가장 가까운 이웃을 찾음
                T=0.7   #임계값
                good_match=[]   #빈 리스트 생성
                for nearest1, nearest2 in knn_match:    #knn_match의 각 요소를 nearest1, nearest2로 받아옴
                    if (nearest1.distance/nearest2.distance)<T:  #nearest1과 nearest2의 거리 비율이 T보다 작으면
                        good_match.append(nearest1)   #good_match에 nearest1 추가
                GM.append(good_match)   #good_match를 GM에 추가
                
                best=GM.index(max(GM,key=len))  #GM의 요소 중 가장 긴 요소의 인덱스를 best에 저장
                
                if len(GM[best])<4:  #GM의 best번째 요소의 길이가 4보다 작으면
                    self.label.setText('표지판이 없습니다') #레이블에 '표지판이 없습니다' 표시
                else:
                    sign_kp=KD[best][0]   #KD의 best번째 요소의 0번째 요소를 sign_kp에 저장
                    good_match=GM[best]   #GM의 best번째 요소를 good_match에 저장

                    poinsts1=np.float32([sign_kp[gm.queryIdx].pt for gm in good_match]) #
                    poinsts2=np.float32([road_kp[gm.trainIdx].pt for gm in good_match]) 

                    H, _=cv.findHomography(poinsts1, poinsts2, cv.RANSAC)   
                    h1,w1=self.signImgs[best].shape[0],self.roadImg.shape[1]    
                    h2,w2=self.roadImg.shape[0],self.roadImg.shape[1]

                    box1=np.float32([[0,0],[0,h1-1],[w1-1,h1-1],[w1-1,0]]).reshape(4,1,2)
                    box2=cv.perspectiveTransform(box1,H)

                    self.roadImg=cv.polylines(self.roadImg, [np.int32(box2)], True, (0,255,0), 5)

                    img_match=np.empty((max(h1,h2),w1+w2,3), dtype=np.uint8)
                    cv.drawMatrches(self.signImgs[best], sign_kp, self.roadImg, road_kp,
                                    good_match, img_match, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
                    cv.imshow('Matches and Homography', img_match)
                    self.label.setText(self.signFiles[best][1]+'보호구역입니다. 30km로 서행하세요.')
                    winsound.Beep(3000,500)

    def quitFunction(self): #나가기 버튼이 눌렸을때 실행될 함수
        cv.destroyAllWindows()
        self.close()

app=QApplication(sys.argv)
win=TrafficWeak()
win.show()
app.exec_() 

""" 
5. 강의교안의 프로그램 7-1를 실습하시오.
 - 주석 달 것
 - 프로그램 소스코드와 실행결과 첨부할 것
"""
""" 
import tensorflow as tf
import tensorflow.keras.datasets as ds
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test)=ds.mnist.load_data()  #mnist 데이터셋을 불러옴
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)    #불러온 데이터셋의 형태 출력
plt.figure(figsize=(24,3))
plt.suptitle('MNIST', fontsize=30)

for i in range(10):
    plt.subplot(1,10,i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.xticks([]); plt.yticks([])
    plt.title(str(y_train[i]), fontsize=30)
(x_train, y_train), (x_test,y_test)=ds.cifar10.load_data()
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
class_names=[]
plt.figure(figsize=(24,3))
plt.suptitle('CIFAR-10', fontsize=30)
for i in range(10):
    plt.subplot(1,10,i+1)
    plt.imshow(x_train[i])
    plt.xticks([]); plt.yticks([])
    plt.title(class_names[y_train[i,0]],fontsize=30)
 """