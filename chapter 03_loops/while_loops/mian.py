'''
wheil 반복문
    while 다음에 나오는 조건문이 참이라면 이하의 실행문이 실생됨(조건문이 Flase가 될때까지

형식:
while 조건문:
 실행문
'''

# # 무한 루프의 개념
# num1 = 1
# while num1 > 0:
#     print(num1)

'''
그래서 while 반복문을 작성할 때 고려할 점:
  특정한 상황에서 조건식이 Flase가 될 수 있도록 사전에 미리 지정해줘야 함
    ->아닐 경우 무한 루프에 빠지게 될 수 있음
'''
# #특정 조건에서 반ㅂ고문이 종료될 수 있도록 하는 예시
# num2 = 1
# while num2 < 11:
#     print(num2)
#     num2 += 1      #특정 조건하에서 조건문이 False가 될 수 있도록 하는 부분
# #최종 num2는 11임.

'''
if문과의 비교:
  if문의 경우 조건식이 참일 때 실행문이 한번 실행되지만 
  while문의 경우 조건식이 참일 때 실행문이 '반복' 실행되기 때문에 
  특정 조건이 맞을 경우와 아닐 경우에 대한 고민이 필요
  
기본예제
10부터 1까지의 모든 정수를 출력하는 while문을 작성하시오
'''

# num3 = 10
# while num3 > 0:
#     print(num3)
#     num3 -= 1

'''
중첩 while문 : while문 내부에 while문이 나타나는 것

ex)
총 5일 동안 매일 3시간씩 수업을 진행. 매일 '1일차 1교시 입니다.'와 같은 메세지 출력
1일차 부터 5일차 까지 반복되는 수
'''

# day = 1
# while day < 6:   # 5일까지만 출력해야함
#     hour = 1
#     while hour < 4:  # 3일차 까지 출력
#         print(f"{day}일차 {hour}교시 입니다.")
#         hour += 1
#     day += 1

'''
기본 예제 
구구단 2단 부터 9단까지 출력하는 프로그램. (while문 사용)
변수명은 dan / number
'''

# dan = 2
# while dan < 10:
#     number = 1
#     while number < 10:
#         result = dan * number
#         print(f"{dan} x {number} = {result}")
#         number += 1
#     dan += 1

# 나
n = 1
while n < 11:
    while n < 101:
        print(n, end=" ")
        n += 1
    n += 1

# 선생님
n = 1
while n < 101:
    print(f"{n} {n+1} {n+2} {n+3} {n+4} {n+5} {n+6} {n+7} {n+8} {n+9}")
    n += 10

'''
이상의 코드의 경우에는 반복을 10번 돌리는 경우였음
모든 편견을 가지고 코드를 작성하게 되면 반복을 100번 돌ㄹ리게 됐을 경우에 사용 가능한 방식
'''

n2 = 1
while n2 < 101:
    print(n2, end = " ")
    if n2 % 10 == 0:
        print()
    n2 += 1