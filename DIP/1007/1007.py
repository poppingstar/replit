import cv2

if __name__ == "__main__":
  cam=cv2.VideoCapture(0)   # 기본 카메라 연결
  if cam.isOpened() == False: #카메라 연결 실패 시 메시지 출력 및 종료
    print('카메라를 열 수 없습니다.')
    exit
  
  cam.set(cv2.CAP_PROP_FRAME_WIDTH, 720)  # 카메라 영상의 너비와 높이 설정
  cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  
  while cv2.waitKey(1)>0: #키보드 입력이 있을 때까지 반복
    ret, frame = cam.read()
    cv2.imshow('webcam', frame)