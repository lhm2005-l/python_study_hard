'''
컬렉션(collection) : 여러 값을 하나의 이름으로 묶어서 관리하는 자료형

string의 경우 문자 하나 하나를 줄(str)로 묶어서 문자열로 출력하는데
예를 들어 '다수의 다른 string을 관리하는 방법은 무엇일까?'에 관한 대답

여러 명의 프로필을 관리한다고 가정해보겠습니다.
'''

# dlgusals = "이름 : 이현민\n나이 : 21\n직업 : 학생"
# print(dlgusals)
# kimrandom = "이름 : 김랜덤\n나이 :20\n직업 : 학생"
# print(kimrandom)

'''
한 명 저장하는 데에는 문제가 없을 수 있지만 매번 변수 하나에 이름, 나이. 직업 등을 한명 추가할 때 마다
정라하는 것은 비효율적이고, 예를 들어서 이현민에서 직업만 조회하고 싶어도 전체 정보를 다 확인해야 함

그리고 주소를 추가한다고 가정했을 때에도 각 변수들을 전부 다 참조해서 수정해줘야 할 필요성이 있음

이상의 문제들을 한꺼번에 관리하기 위한 방식으로 모음(collection)을 사용

종류 :
    1. list 리스트 : 추가 / 수정 / 삭제가 언제나 가능 / a = [1,2,3] 대괄호 사용
    2. tuple 튜플 : 추가 / 수정 / 삭제가 불가 / a = (1,2,3) 소괄호 사용
    3. set 세트 : 중복된 값의 저장이 불가 / a = {1,2,3} 중괄호 사용
    4. dict 딕트(딕셔너리) : 키 + 값으로 관리 / a{"name": "안근수", "age" : 38} 중괄호 사용
    
1. list
  여러 값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장 가능
  하나의 배열(파이썬에서 리스트와 비슷한 개념)에 동일한 자료형을 저장할 수 있는 c, java에 비해
  python이 가지는 장점이라고 할 수 있음.
'''

# li = [1,2,3,"이현민"]
# print(li)

'''
  1-1. list의 index와 slice
    list는 str과 동일한 방식의 index와 slicing을 지원함
    1) 인덱스와 마이너스 인덱스
'''
# print(li[0])
# print(li[1])
# print(li[-1])
'''
    2) slice
    str의 슬라이싱과 같이 '시작인덱스:종료인덱스:증감값'으로 이루어져 있음.
'''
# list1 = [100,3.14,"hello"]      # list 생성 방법 # 1
# list2 = list([4,5,6,7,8,9])     # list 생성 방법 # 2
'''
    3) list 요소의 추가와 삭제
    list에 새로운 요소를 추가할 때는 .append()와 isert() '메서드'를 사용할 수 있음.
    기존 요소를 삭제할 때는 .pop() 메서드를 사용
    
    .append() - 항상 마지막 인덱스에 요소를 추가하는 메서드
    .insert(위치,값) - 정해진 위치(인덱스)에 해당하는 값을 추가하는 메서드
    pop()의 경우 빈 괄호로 사용하게 되면 맨 마지막 요소가 삭제됨.
    pop(인덱스 넘버)로 작성하면 해당 인덱스의 요소를 삭제함
    
    교제에 없는 삭제 메서드 :
    .remove(값)을 사용하면 list 내에 해당값을 찾아 삭제함.
'''
# scores = [30,40,50]     # scores라는 list 내에 있는 데이터인 각각의 30, 40, 50
# scores.append(100)      #함수와 달리 list명.메서드명(데이터)의 형태로 사용 -> 호출 방식이 다름
# scores.insert(1,90)
# scores.pop()
# scores.pop(0)           # 오버 로딩의 기초 개념이 포함돼 있어서 동일한 메서드 명인데도 argument가 있을수도 / 없을수도 있음
# scores.remove(40)
# 이상의 코드까지 실행 시켰을 때, 인덱스가 두 개 밖에 없어서 19개 정도의 element를 추가하는 반복문을 작성
# for i in range(10):
#     scores.append(i*10)


# list 내의 요소들을 하나씩 뽑아 내는 반복문 - for 문 -> 위 코드를 참조해서 전체 element를 뽑아내는 반복문 작성
# 나
# for i in range(10):
#     scores.len(i*10)
# print(scores)

# # 선생님
# for i in range(len(scores)):
#     print(scores[i])

# print()
# # 향상된 for문 사용 -> 읽기만 됨 (연산 불가)
# for score in scores:        # 전에 말했던 것처럼 collections의 경우 복수로 이름 짓고 향사된 for문에서 각 변수는 단수로 이름 짓는 경우가 많음
#     print(score)

'''
2. tuple() : 저장된 값을 변경할 수 없는 list라고 생각하면 됨. 
    인덱스와 슬라이스를 사용하지만 저장된 값 외에는 추가 / 수정 / 삭제 불가함
    튜플은 소괄호를 통해 생성
'''
# tuple_num1 = (1,2,3)            # 튜플 생성 방법 1
# tuple_num2 = tuple((4,5,6))     # 튜플 생성 방법 2
# tuple_num3 = 7,8,9              # 튜플 생성 방법 3

# # 복수의 변수 선언 및 초기화 방법
# a,b,c = 7,8,9

'''
   튜플 생성 방법3을 이용한다고 가정했을 때, 값이 하나 밖에 없는 튜플을 생성한다면 tuple_num4 = 0을 입력할 경우 생길 수 있는 문제는 뭘까?
'''

# tuple_num4 = 0
# print(tuple_num4)
# print(type(tuple_num4))       # int의 형태임
'''
    1) 튜플에서의 인덱스 / 마이너스 인덱스
'''
# tuple_num6 = 1,2,3,4,5,6,7,8,9
# print(type(tuple_num6[2]))  # collections의 element에 type() 함수를 적용하면, element의 자료형이 반환됨
#                             # 즉, tuple_num6[2]는 3이라는 element를 가리키기 때문에 type()함수 적용시 <class 'int'>로 출력
# tuple_num7 = "hello. ", "nice to meet you. ", "my name is ", "lee hyunmin. ", "I am ", "21 ", "years old."
#
# for words in tuple_num7:
#     print(words.title(), end="")    # 튜플의 정의를 생각해야 함, 왜 결과값이
#     # Hello. Nice To Meet You. My Name Is Lee Hyunmin. I Am 21 Years Old. 이렇게 될까?
#
# print()
# for words in tuple_num7:
#     print(words.title(), end="")    # words.title()을 적용시켰다고 해서 tuple내의 element들이 전부 값이 바뀐 상태가 유지되는 것이 아니라
# words.title()이렇게 작성했을 때만 메서드가 적용된 상태이기 때문에 요소가 바뀌지 않음'''
'''
3. set
  수학의 집합 개념을 구현한 자료형. list와의 차이점은 순서가 ㅇ벗기 때문에 (비시퀀스)인덱스 및 슬라이싱 상요이 불가. 중복된 값 저장이 불가
  이를 활용해 중봅 제거용으로 사용하는 경우와, 교집합, 합집합, 차집합과 같은 집합 개념이 필요한 경우 사용
  set를 사용하깅 위해 중괄호({})사용
  
  set에는 인덱싱 / 마이너스 인덱싱 / 슬라이싱을 지원하지 않기 때문에 특정 요소만 추출하기 위해서는 형변환 과정(주로 list())이 필요함
  
    특징
  1. 저장되는 순서가 없음. -> 인덱싱 / 슬라이싱 불가
  2. 중복되는 값을 저장할 수 없다.
  3. 특히 2.의 특징으로 인해 set는 단독으로 쓰이기 보다는 list와 연계해서 많이 쓰임
  
  요소 관련 메서드
    .add() - set에 새로운 요소 추가
    .remove() - 기존 요소를 삭제할 때
    .discard() - 기존 요소를 삭제할 때
'''
# set_num1 = {1,2,3}          # 세트 설정법 1
# set_num2 = set({4,5,6})     # 세트 설정법 2
#
# # 비어있는 list, tule, set 생성 방법
# li = []
# tu = ()
# se = {}
'''
  se = {} 형태로 비어있는 set를 생성했을 겨웅 se는 사실 <class 'dict'>이기 때문에
  비어있는 set를 만들기 위해서는 세트 생성 방법 2를 사용해야 함.
'''
# se2 = set({})
# print(type(se2))  # <class 'dict'>
# # list_num5 = [1,1,2,2,3,3,3]
# set_num5 = set(list)            # 형변환 함수인 set()를 사용하고, 그 안에 list_num5를 argument로 넣어 list->set로 바꿈
# list_num6 = list(set_num5)      # list로 바꿨으니까 슬라이싱 및 인덱싱이 다시 사용 가능
#
# set_num6 = {10,20,30}
# set_num6.add(50)                # {10, 20, 50, 30}: 순서가 다르게 나올수도 있음
# set_num6.remove(50) 'set'>
#
#
# # 중요 .remove(), .discard()
# set_num6.remove(70)  #.remove() -> 정확히 입력해야함
# set_num6.discard(70) # .discard()는 요소에 정확한 값이 있지 않더라도 오류 발생 x
'''
4. dictionary - 말 그대로 사진의 의미를 생각하면 됨. 종이 사진을 찾아보게 되면
  flower: 꽃
  dictionary: 사진
  등으로 기재. 즉 ":"을 기준으로 좌측과 우측이 나누어진 형태를 가지고 있는데 
  딕셔너리는 리스트, 튜플, 세트와 달리 
  key : value의 구성으로 이루어져있음
'''
# dict_num1 = {
#     "이름": "이현민",
#     "나이": 21,
#     "주소": "부산광역시 남구"
# }
# 맨 마지막에 있는 ,의 의미는 혹시 후에 key-value를 추가할 때 이전 라인에서 콤마를 입력하고 엔터치고
# 또 key: value 형태로 작성하기 귀찮으니까 미리 쉼표를 찍어놔서 쉽게 추가할 수 있도록하는게 개발자끼리의 매너임

'''
  딕셔너리는 인덱스가 존재하지 않지만 위와 같이 key를 인덱스와 유사하게 사용,
  즉, key값을 알면 저장된 값(value)를 확인할 수 있는 구조
'''
# list의 각 요소를 추출하기 위한 반복문
# li2 = [10,20,30,40]
# for num in li2:
#     print(num)

# # dictionary에서 같은 방식의 반복문을 활용하게 될 때,
# for i in range(len(dict_num1)):
#     print(dict_num1[1])                 #index가 없기 때문에 오류 발생

# for k in dict_num1:
#     print(k)                            # 그냥 print()하게 되면 dict_num1의 key만 추출됨
#     print(dict_num1[k])                 # 그래서 value를 추출하려고 하면 지금 코드 라인과 같이 작성해야함.
#     print()

# key 목록을 추출하는 메서드
# print(dict_num1.keys())
# print(dict_num1.values())
#
# print(type(dict_num1.keys()))           # <class 'dict_keys'>
# print(type(dict_num1.values()))         # <class 'dict_values'>
#
# keys = list(dict_num1.keys())
# values = list(dict_num1.values())       # index를 활용하기 위해서 list로 형변환을 할 필요가 있음
#
# print(keys[1])
# print(values[1])

'''
  1) 딕셔너리 요소의 추가와 삭제
'''
# dict_num1["직업"] = "학생"                # 기존에 있는 key를 입력하고, = vlaue 지정하면 됨
# dict_num1["직업"] = "대학생"              # 하나의 key에 서로 다른 value를 지정 할 수 없음
# # key 하나 당 value는 하나여야만 함
#
# # 삭제 방법
# dict_num1.pop("직업")                    # key를 정확히 입력해야 삭제 가능, key를 삭제하면 value도 같이 날아감

'''
응용 예제

list [10,20,30,40,50,60,70,80,90,100]의 3번째 요소로부터 7번째 요소만 추출한 결과, 그리고 그 list에서 번째 요소를 출력하는 프로그램을 작성

실행 예
3번째 요소로부터 7번째 요소 = [30,40,50,60,70]
3번째 요소로부터 7번째 요소 중 2번재 요소 = 40
'''

# list_origin = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# li = list_origin[2:7]
# print("3번째 요소로부터 7번째 요소 = ", li)
# print("3번째 요소로부터 7번째 요소중 2번째 요소 = ", li[1])

'''
사용자로부터 1에서 12사이의 월을 입력받아, 해당 월이 며칠까지 있는지 출력하는 프로그램을 작성하시오 (윤년은 고려ㅌ)
 
실행 예
1~12 사이의 월을 입력하시오 >>> 2
2월은 28일 까지입니다.
'''
# # 나
# month = input("1~12 사이의 월을 입력하세요 >>> ")
# if month == [1,3,5,7,8,10,12]:
#     print("{}월은 31일까지 입니다".format(month))
# elif month == [2]:
#     print("{}월은 28일까지 입니다.".format(month))
# else:
#     print("{}월은 30일까지 입니다.".format(month))
#
# # 선생님, 다른 학생 방식
# month = input("1~12 사이의 월을 입력하세요 >>> ")
# month_int = int(month)
# last_dates=[31,28,31,30,31,30,31,31,30,31,30,31]
# print(f"{month_int}월은 {last_dates[month_int-1]}일까지 있습니다.")
# last_dates_short = [28,30,31]
#
# last_dates_dict = {
#     "1":31,
#     "2":28,
#     "3":31,
#     "4":30,
#     "5":31,
#     "6":30,
#     "7":31,
#     "8":31,
#     "9":30,
#     "10":31,
#     "11":30,
#     "12":31
# }
# print(f"{month}월은 {last_dates_dict[month]}일까지 있습니다.")
#
# last_dates_shorts = [28,30,31]
#
# if month_int == 2:
#     last_date = last_dates_short[0]
# elif month_int == 4 or 6 or 9 or 11:
#     last_date = last_dates_short[1]
# elif month_int in (1,3,5,7,8,12):
#     last_date = last_dates_short[2]
# else:
#     print("잘못 입력하셨습니다.")
#     last_date = "x"
#
# print(f"{month}월은 {last_date}일 까지 있습니다.")
'''
수학 여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학 여행 장쇼를 조사하기로 헀음
학생들이 원하는 장소를 입력받아 동일한 입력을 무시하고 모든 입력을 저장하려고 함
학생을 3명으로 가정하고 싫애 예와 같이 동작하는 프로그램을 작성해라.

실행 예

희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망한느 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는  {'제주', '민속촌'}입니다
조사된 수학여행지는 ['제주', '민속촌']입니다.
'''
# tr = []
# tr_se = set({})
# for a in range(3):              # range 안의 숫자만 바꾸면 되므로 범용성 있는 코드임
#     student = input("희망하는 수학여행지를 입력하세요 >>> ")
#     tr_se.add(student)
#     # tr_se = [student]  #얘를 사용할 경우 [student]로 매번 초기화
#
# # tr_se = set(tr_set)
#
# tr_se - set(tr_se)
# print(f"조사된 수학여행지는 {tr_se}입니다.")
# print(f"조사된 수학여행지는 {list(tr_se)}입니다.")

'''
짝수만 추출하기

사용자로부터 임의의 정수를 입력받고, 그 정수만큼 숫자를 입력받아 list에 저장해라
이 후 저장된 숫자 중 짝수만 새로운 list에 저 장하여 출력하는 프로그램을 작성해라

실행 예
몇 개의 숫자를 입력할까요? >>> 6
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >> 20
4번쨰 숫자를 입력하세요 >>> 30
5번쨰 숫자를 입력하세요 >>> 25

입력받은 숫자는 [5,10,15,20,25,30]입니다.
입력받은 숫자 중 짝수는 [10,20,30]입니다
'''
# li = []
# li_even = []
#
# a = int(input("몇 개의 숫자를 입력할까요? >>> "))
# for i in range(a):
#     num = int(input(f"{i+1}번째 숫자를 입력하세요 >>> "))
#     li.append(num)
#
# print(f"입력 받은 숫자는 {li}입니다.")
#
# for num in li:
#     if num % 2 == 0:
#         li_even.append(num)
#
# print(f"입력 받은 숫자 중 짝수는 {li_even}입니다.")

# 압축한 풀이

# li = []
# li_even = []
# for i in range(int(input("몇 개의 숫자를 입력하시겠습니까? >>> "))):
#     num2 = int(input(f"{i+1}번째 숫자를 입력하세요 >>> "))
#     li.append(num2)             # 일단 입력 받은건 li에 전부 추가
#     if num2 % 2 == 0:
#         li_even.append(num2)    # 그리고 그 숫자가 짝수라면 even에도 추가 아니면 다음 반복문으로
#
# print(f"입력 받은 숫자는 {li}입니다.")
# print(f"입력 받은 숫자 중 짝수는 {li_even}입니다.")

'''
딕셔너리 기반의 연락처 관리

사용자로부터 3명의 이름과 전화번호를 입력 받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출하는
프로그램을 작성하시오.

실행 예
1 번째 사람의 이름을 입력하세요 >>> 김일
1번째 사람의 연락처를 입력하세요 >>> 010-1234-1234
2 번째 사람의 이름을 입력하세요 >>> 김일
2번째 사람의 연락처를 입력하세요 >>> 010-1234-1234
3 번째 사람의 이름을 입력하세요 >>> 김일
3번째 사람의 연락처를 입력하세요 >>> 010-1234-1234

입력받은 연락처는 {'김일' : '010-1234-1234','김일' : '010-1234-1234','김일' : '010-1234-1234'}입니다
'''
# # 나
# dict = {
#
# }
#
# for i in range(3):
#     name = input(f"{i+1}번째 사람의 이름을 입력하세요 >>> ")
#     num = input(f"{i+1}번째 사람의 연락처를 입력하세요 >>> ")
#
#     dict[name] = num
#
# print(f"입력 받은 연락처는 {dict}입니다.")

# 선생님
# telephones = {}
# for i in range(3):
#     dict_key = input(f"{i+1}번째 사람의 이름을 입력하세요 >>> ")
#     dict_value = input(f"{i+1}번째 사람의 연락처를 입력하세요 >>> ")
#
#     telephones[dict_key] = dict_value
#
# print(f"입력 받은 연락처는 {telephones}입니다.")

'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제 : 비어있는 list01을 선언하고 그 안에 입력받은 횟수만큼 숫자를 추가하시오.

함수 정의 : add_numbers()
매개 변수 : 정수 n

함수 호출
add_numbers(last_num)

실행 예
숫자 몇까지 입력하시겠습니까? >>> 10
[1,2,3,4,5,6,7,8,9,10]
'''
# # 나
# def add_numbers(n):
#     list01 = []         # 지역 변수
#     for i in range(n):
#         list01.append(i+1)
#     print(list01)
#
# last_num = int(input("숫자를 몇 까지 입력하시겠습니까? >>> "))
# add_numbers(last_num)
#
# def add_numbers1(n):
#     list02 = []         # 지역 변수
#     for i in range(n):
#         list02.append(i+1)
#     return list02
#
# last_num1 = int(input("숫자를 몇 까지 입력하시겠습니까? >>> "))
# print(add_numbers1(last_num1))
#
# # add_numbers1 /2 와 차이점
# for number in add_numbers1(last_num):
#     print(number+1)
#
# for number in add_numbers(last_num):
#     print(number+1)
# # 이 이상의 코드는 불가함. -> add_numbers(n)의 경우 print 실행문으로 마무리가 되기 떄문에 추가 연산 x

'''
짝수와 홀수의 개수 새기
list를 입력받아 짝수와 홀수의 개수를 세는 함수를 작성하시오.

함수 정의
함수 이름 : count_even_odd
매개 변수 : list numbers(요소는 모두 정수)

함수 호출
count_even_odd([1,2,3,4,5,6,7,8,9,10])

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개
'''
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for i in numbers:
        if i % 2 == 0:
            even_count = even_count + 1     # even_count += 1 도 가능
        else:
            odd_count = odd_count + 1       # odd_count += 1 도 가능

    print(f"짝수의 개수 : {even_count}")
    print(f"홀수의 개수 : {odd_count}")

count_even_odd([1,2,3,4,5,6,7,8,9,10])