def add(*operands):     #가변인자를 받아 더하는 함수 선언
  sum=operands[0]       #첫번째 요소를 초기값으로 설정
  for _ in operands[1:]:      #가변 인자 tuple을 순회하며 각 요소 더하기
    sum+=_
  return sum              #결과 반환

def subtract(*operands):  #가변인자를 받아 빼는 함수 선언
  sum=operands[0]         #첫번째 요소를 초기값으로 설정
  for _ in operands[1:]:      #가변 인자 tuple을 순회하며 각 요소 빼기
    sum-= _
  return sum              #결과 반환

def multiply(*operands):  #가변인자를 받아 곱하는 함수 선언
  sum=operands[0]         #첫번째 요소를 초기값으로 설정
  for _ in operands[1:]:      #가변 인자 tuple을 순회하며 각 요소 곱하기
    sum*= _
  return sum          #결과 반환

def main():             #main함수 선언
  nums=10,5,4,2         #인자 리스트 선언
  ad=add(*nums)         #add 함수 호출, 인자로 언패킹한 tuple 전달
  sub=subtract(*nums)   #subtract 함수 호출
  mul=multiply(*nums)   #multiply 함수 호출
  print(ad, sub, mul)   #결과 출력

if __name__ == "__main__":  #모듈로 사용시 실행 방지
  main()        #main함수 호출
