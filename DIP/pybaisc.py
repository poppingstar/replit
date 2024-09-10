def add(*operands):   #가변인자를 받아 더하는 함수 선언
  for _ in operands:      #가변 인자 투플을 순회하며 각 요소 더하기
    result+=_
  return result            #결과 반환

def subtract(*operands):  #가변인자를 받아 빼는 함수 선언
  for _ in operands:      #가변 인자 투플을 순회하며 각 요소 빼기
    result-= _
  return result            #결과 반환

def multiply(*operands):  #가변인자를 받아 곱하는 함수 선언
  for _ in operands:      #가변 인자 투플을 순회하며 각 요소 곱하기
    result*= _
  return result          #결과 반환

def main():          #main함수 선언
  list = [3,2,10,27,0,10,100,75,28]    #list 선언
  list.append(300)      #300을 추가
  list.remove(10)        #10 삭제

  for _ in list:        #리스트 범위 기반 for문
    print(_)            #리스트의 요소 출력
  
  nums=10,5,4,2
  add(nums)
  subtract(nums)
  multiply(nums)

if __name__ == "__main__":
  main()