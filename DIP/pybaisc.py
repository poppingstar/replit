def add(*operands):     #가변인자를 받아 더하는 함수 선언
  sum=operands[0]       #첫번째 요소를 초기값으로 설정
  for _ in operands[1:]:      #가변 인자 투플을 순회하며 각 요소 더하기
    sum+=_
  return sum              #결과 반환

def subtract(*operands):  #가변인자를 받아 빼는 함수 선언
  sum=operands[0]         #첫번째 요소를 초기값으로 설정
  for _ in operands[1:]:      #가변 인자 투플을 순회하며 각 요소 빼기
    sum-= _
  return sum              #결과 반환

def multiply(*operands):  #가변인자를 받아 곱하는 함수 선언
  sum=operands[0]         #첫번째 요소를 초기값으로 설정
  for _ in operands[1:]:      #가변 인자 투플을 순회하며 각 요소 곱하기
    sum*= _
  return sum          #결과 반환

def main():          #main함수 선언
  list = [3,2,10,27,0,10,100,75,28]    #list 선언
  list.append(300)      #300을 추가
  list.remove(10)        #10 삭제

  for _ in list:        #리스트 범위 기반 for문
    print(_,end=',')            #리스트의 요소 출력
  print()
  
  nums=10,5,4,2
  ad=add(*nums)
  sub=subtract(*nums)
  mul=multiply(*nums)
  print(ad, sub, mul)

if __name__ == "__main__":
  main()