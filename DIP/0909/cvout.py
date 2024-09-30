import cv2 as cv    #cv2모듈을 cv로 import

def main(): #main 함수 선언
  Hello_world = cv.imread('Lenna.png') #이미지 파일을 읽어 Hello_world에 저장

  cv.putText(Hello_world, "20191469 MinsuShin", (20,40), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0)) 
  #이미지에 텍스트 추가, 좌상단 기준 좌표(20,40), 폰트 cv.FONT_HERSHEY_SIMPLEX, 크기 1, 검은색
  cv.imshow('image',Hello_world) #이미지 출력
  cv.waitKey(0) #입력이 들어올때까지 이미지 출력 유지

if __name__ == "__main__":  #모듈로 사용시 실행 방지
  main()  #main함수 호출
