'''
1. 함수(function) : 특정 작업을 수행하는 코드 블록을 정의하는 방법

ex) '사진을 찍는다'라는 행위에 대해 생각하면
1) 주머니에서 폰을 꺼냄
2) 잠금을 품
3) 카메라를 킴
4) 사진을 찍고자 하는 대상에 폰을 조준
5) 셔터를 누름

하지만 컴퓨터는 시키는대로만 하기 때문에 사진을 찍기 위해서
1) ~ 5) 까지의 명령어를 입력해줘야함 함

하지만 '사진을 찍는다'라는 함수내에 1) ~ 5)의 명령어들을 미리 입력해두고 나서
'사진을 찍는다'라는 명령어를 실행시키기만 하면 1) ~ 5)까지의 명령들을 순서대로 수행하도록 하는것이 함수의 개념

함수 정의 형식:
def turn_right():
    turn_left()
    turn_left()

함수 호출 형식:
turn_right

2. 함수의 종류
  1) 파이썬 내장 함수
  2) 메서드
  3) 사용자 정의 함수

3. 함수 용어 정리
  1) 함수 정의 : 사용자 함수를 새로 만드는 것을 의미(def : define)
  2) 인수(argument) : 함수에 전달할 입력값(input)
  3) 매개변수(parameter) : 인수를 받아서 저장하는 변수
  4) 변환값 / 결과값 / 리턴값 : 함수의 출력값
  5) 함수 호출 : 함수를 실제로 하용하는 것을 의미

4. (사용자) 함수의 형식 :
def 함수_이름(매개변수):
    실행문

변수 = 함수_이름(argument)
'''

# # 함수 정의
# def write_name(name):   # 정의 할 때 소롸호 내에 있는걸 parameter라고 함.
#     print(f"당신의 이름은 {name}입니다.")
#
# # 함수 호출
# write_name("안근수")    # 호출할 때 소괄호 내에 있는 것을 argument라고 함.
#
# def write_name_age(name, age):   # parameter가 복수인 사례 및 함수 정의
#     print(f"당신의 이름은{name}이고, 나이는 {age}입니다.")
#
# write_name_age("안근수", 38)   # 매개변수가 두 개 이기때무네 argument도 두 개인 상황
# write_name_age(age = 10, name = "안근수")    # keyword argument라고 함.

'''
우리가 예를 들어 input("이름을 입력하세요 >>> ")을 이용해서 이것을 name이라는 변수에 담았다고 가정하면 
name = input("이름을 입력하세요 >>> ")이라고 작성해왔음

우리는 여태까지 함수의 결과값을 변수에 담아오고 있었음

파이썬 내장함수는 이미 함수가 정의돼있고, 개발자들은 함수 호출만 잘 하면 됨
사용자 함수는 개발자 자신이 함수를 정의하고, 그 후에 호출하는 것까지의 과정이라고 생각하면 됨.

내장함수 예시
print() / type() / int() / flat() / input()

2. 메서드(method) : 특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함돼있는 함수
사실 함수와 매서드는 동일한 개념. 호출 방식에 있엇어의 차이가 있음

함수는 독립적으로 사용가능 / 메서드는 특정 객체를 통해서만 호출 가능
'''

# eng_name = input("당신의 이름을 소문자로 입력하세요 >>> ").upper()
# # 이상의 코드에서 input()은 함수, .upper()은 메서드
# print(eng_name)     # 얘는 함수
# eng_name2 = input("당신의 이름을 소문자로 입력하세요 >>> ").title()
# print(eng_name2)
'''
함수(메서드)의 유형
'''
# # 매개변수 x / 리턴 x
# def call1():
#     print("[ x | x ]")
#
# #매개변수 o / 리턴 x
# def call2(str_type):
#     print("[ o | x ]")
#     print(f"{str_type}라고 입력하셨나보네요")
#
# # 매개변수 x / 리턴 o
# def call3():
#     print("[ x | o ]")
#     return 1
#
# # 매개변수 o / 리턴 o
# def call4(str_type):
#     print("[ x | o ]")
#     return f"제 이름은 {str_type}입니다"
#
# call1()
# call2("오늘 날씨 너무 추워요")
# call3()  # 이 경우 return이 출력되지 않습니다.
# print(call3())  # 이래야 return이 출력됨.    ->  그럼 길게 써야하니까 불편한거 아닌가?
# print(call3() + 1)
#
# new_element = (call3() + 3) * 10
# print(new_element)
#
# call4("이현민")
# print(call4("이현민"))

'''
 call3() / call4() 유형에서 함수 내에 print()를 집어넣어두면 main단계에서 (들여쓰기가 되어있지 않은 단계에서)
print() 함수를 입력할 필요가 없어 후러씬 편할것 같은데
왜 굳이 return 형태로 입력해서 main에서 일일이 print()함수를 적용해야하는가

함수형 프로그래밍 : 특정한 함수1의 결과값이 
    또 다른 함수2의 argument로 사용되는 것을 의미
    그리고 함수2의 겨로가값이 함수3의 argument로 사용되는 것이 반복된다면
'''
# # 사용자 함수르 ㄹ정의
# def introduce(name, address):           # call4() 유형으로 정의
#     return f"제 이름은 {name}이고, {address}에 삽니다"
#
# # 함수1 사용 : input() -> 파이썬 내장 함수
# name = input("이름을 입력하세요 >>> ")
# address = input("주소를 입력하세요 >>> ")
#
# # 함수1의 결과값을 함수2인 사용자 함수의 argument로 사용 -> 그 결과값을 함수3인 print()함수의 argument로 사용
# print(introduce(name,address))

'''
700원 짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지, 그리고 잔돈은 얼마인지
모든 경우의 수를 출력

함수 정의
- 반환값 : 없음
- 함수이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성

def vending_machine():
    #함수 구성

vending_machine(3000)

실행 예
음료수 = 0개, 잔돈 3000원
음료수 = 1개, 잔돈 2300원
'''

# # 나
# def vending_machine(money):
#     a = money // 700
#     for i in range(a):
#         print("음료수 = {}개, 잔돈 {}원".format(i, money-(i*700)))
#
# vending_machine(10000)
#
# # 선생님
# my_money = 3000
# drink_price = 700
# # for 반복문 돌려서 실행 예와 같이 나오도록 하려면 어떻게 작성해야할까
# charge = 3000 - (700*음료수 개수)
# # my_money기준으로 음료수를 살 수 있는 경우의 수
#
# #return타입 없으니까 print()로 마무리 / 매개변수 명이 통제돼있으므로 vending_machine(money)형태로 작성
# def vending_machine(money):
#     for i in range(my_money//drink_price + 1):                   #range()함수에 내에 들어가는 argument의 자료형은 int여야 합니다.  ->단순히 나눠서는 안됨
#         print(f"음료수 = {i}개, 잔돈 ={my_money-(drink_price*i)}")
#
# vending_machine(7500)

'''
예제 : 구구단 출력하기
함수 정의 :
함수 이름 :
매개변수 : 정수 n 
 
함수 호출 :
multiply(dan)

실행 예
몇 단능 출력하시겠습니까? >>> 3
3 x 1 = 3
3 x 2 = 6
'''

# # 나
# def multiply(dan):
#     for i in range(1, 10):
#         print("{} x {} = {}".format(dan, i, i * dan))
#
# dan = int(input("몇 단을 출력하시겠습니까? >>> "))
# multiply(dan)
#
# def multiply():
#     n = int(input("몇 단을 출력하시곘습니까? >>> "))
#     for i in range(1, 10):
#         print("{} x {} = {}".format(n, i, i * n))

# # 선생님
# # 함수 정의
# def multiply(n):
#     for i in range(1,10):
#         print(f"{n} x {i} = {n * i}")
#
# def multiply2():
#     dan = int(input("몇 단을 출력하시곘습니까? >>> "))
#     for i in range(1,10):
#         print(f"{n} x {i} = {n * i}")
#
# #call2 유형을 호출

# print(dan)           # 현재 상황에서 오류 발생 -> 함수를 정의만 하는 것은 상요하게 아니기 때문에 변수에 해당하지 않음
# dan = 3              # 그리고 structure를 확인한 결과 선언한 dan이 없음을 확인할 수 있음
# print(dan)