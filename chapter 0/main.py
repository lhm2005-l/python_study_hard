print("Hello, Python!😊")

#주석(comment): 컴퓨터가 읽는 부분이 아니라 사람이 읽을 수 있도록
# 정보를 제공하는 방법으로 주석처리가 되어있는 부분은 인터프리터가 코드로 인지하지 않음.
# 미리 작성해 놓고 후에 주석처리를 하는 방법: ctrl + /

# '''
# 다중 주석 처리
#
# 앞으로 우리가 필기를 하게 되는 내용이 여러 줄에 걸쳐 있을 경우에는 미리
# 작은 따옴표 세 개(누르면 자동으로 세개 더 나옴)를 눌러주고 타이핑을 진행하게 됨.
# ->엔터쳤을 때 자동으로 나머지 세개의 작은 따옴표가 내려가게 되면서 ctrl+/를 할 필요가 없다는 장점이 있음.
# '''
#
# print("1")
# print(1)
# # print(Hello, Python!😊) -> 오류 발생 : 주석처리를 하니까 읽지 않음.
#
# '''
# 15-16번 라인의 출력 결과가 동일하기 때문에 큰 따옴표의 필요성에 대해 인지하지 못할 수 있지만,
# 17번 라인이 오류가 발생하는 점에서 차이를 발견할 수 있음)
# '''
# print(type("1"))   # <class 'str'>
# print(type(1))     # <class 'int'>
# # type의 차이에 따른 검증
# print("1" + "2")   # 결과값 : 12
# print(1+2)         # 결과값 : 3
#
# print("2" + "1")   # 결과값 : 21  / 문자열이라서 순자가 중요
# print(2+1)         # 결과값 : 3   / 정수라서 1+2 = 2+1
# '''
# print() : 컴퓨터한테 출력해달라고 요청하는 명령어
# type() : 소괄호 내에 들어가있는 데이터가 어떤 자료형인지 표시하는 명령어
#   -> 주로 print() 함수와 합쳐져서 사용됨.
# str : string의 축약어로 '문자열'을 의미.
# int : integer의 축약어로 '정수'를 의미.
#
# 여러분들이 자기 소개를 한다고 가정했을 때, 그것이 콘솔에 축력되려면
# ""내에 작성을 해야함.
# '''
# print("제 이름은 이현민 입니다. 나이는 21이고, 부산광역시 남구에 삽니다.")
# print("MBTI는 INFP입니다."
#       "엔터를 치니까 추가가 된다.")
# print('''
# 이런 경우에는 엔터를 치게 됐을 경우에
# 콘솔에서 엔터키가 적용이 된 상태로
# 작성이 가능합니다.
# ''')
'''
콘솔창에 찍히는 문자 개수보다 우리가 타이핑하는게 훨씬 더 많음.
콘솔창에서는 print("")만큼은 출력을 해주지 않음.
'''
# print("제 이름은 이현민입니다. 나이는 21이고, 부산시 남구에 삽니다.")
intro = "제 이름은 이현민입니다. 나이는 21이고, 부산시 남구에 삽니다."
print(intro)
'''
변수(variable) : 데이터를 저장하는 바구니 -> 이름을 어떻게 붙이는지는 자유로움.

변수 명명 규칙(python 버전)
 1. 변수의 경우 소문자로만 입력.
 2. 여러 단어가 합쳐진 변수의 경우 _로 연결. ex) school_name -> 이런걸 snake case라고 함
'''
# name 이라는 변수에 이름을 대입, age 라는 변수에 나이를 대입해서 콘솔창에 내림차순으로 출력

name = "이현민"
age = 21
print(name)
print(age+1)  # 변수에 정수가 담겨있다면 수학적 연산이 가능

a = 1
print(a)  # 결과값 : 1
a = a + 1
print(a)  # 결과값 : 2
'''
대입 연산자
1. = : = 오른쪽에 있는 데이터를  = 왼쪽에 있는 변수에 대입한다는 의미
 즉, 70번 라인의 a = 1는 1이라는 정수 데이터를 a라는 변수에 대입하고
 72번 라인에서 a + 1라는 데이터를 다시 b라는 변수에 대입했다는 의미
 그 결과 73번 라인에서 2가 출력이 됨
 
변수는 처음에 변수 이름을 정하고 "=" 표시 뒤에 넣고자 하는 데이터를 집어넣으면
print()를 통해서 출력하거나 혹은 수학적 연산이 가능하고, 동일한 변수명에 새로운 데이터를 
다시 집어넣는 것도 가능.
'''

'''
f-string : formatted string의 축약어로 str 내에 변수를 불러올 수 있음.
""내에 변수를 불러오기 위해서는 중괄호를 삽입하고, 불러오고자 하는 변수를 기입함.
'''
print(f"제 이름은 {name}이고, 나이는 {age+1}살이 됩니다")

'''
지금까지 수업한 방식으로는 미리 데이터를 준비 해놓고, 거기에 변수르 대입.
즉 실시간으로 데이터를 입력할 수가 없음.

이름이 "김일"이었다가 "김이"로 바꾸기 위새서는 
name = "김일"
print(name)
name = "김이"
print(name)
과 같은 방식으로 코드를 작성해야 하는 번거로움이 있음
이를 해결하기 위해서 우리는 input()을 이용할 수 있음.
'''
input("당신의 이름은 무엇입니까? >>>")

'''
위와 같이 입력하고 실행시키면 콘솔ㅊ ㅏㅇ에 이름을 입력할 수 있도록 커서가 깜빡거림
거기에 이름을 입력하면 프로그램이 종료된다는 점을 확인 가능

즉, 데이터를 입력받기는 했지만 변수에 저장하는 과정이 없었기 때문에 데이터가 휘발됨
그렇다면 입력받은 값을 변수에 대입하면 저장이 됨.
'''

name = input("당신의 이름은 무엇입니까? >>>")
print(name)
print(f"제 이름은 {name}입니다.")
'''
114-116라인까지의 코드 분석함.
input()함수는 ()안에 있는 질문 사항(프롬프트)을 콘솔에 출력하여 사용자로 하여금 입력받을 수 있게끔 합니다.
사용자가 프로프트에 맞는 정보를 입력하면, 그 데이터는 name이라는 변수에 저장되고 이를 print() 함수를 통에 콘솔로 출력하게 됨.
'''
pants = input("당신이 어제 입은 바지는 무슨 색 입니까?")
food = input("당신이 마지막으로 먹은 음식은 무엇입니까?")
band_name = pants + food
print("당신의 인디 밴드의 이름은 {}입니다".format(band_name))
