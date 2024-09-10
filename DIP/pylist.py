def main():          #main함수 선언
  list = [3,2,10,27,0,10,100,75,28]    #list 선언
  list.append(300)      #300을 추가
  list.remove(10)        #10 삭제

  for _ in list:        #리스트 범위 기반 for문
    print(_,end=' ')            #리스트의 요소 출력
  print()       #줄바꿈

if __name__ == "__main__":    #모듈로 사용시 실행 방지
  main()      #main함수 호출