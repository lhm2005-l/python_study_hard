'''
1. 생성자(Constructor)
'''
# 클래스 정의
# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def display_info(self):
#         print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")
#
# # 객체 생성
# satang = Candy()
# satang.set_info("구형", "갈색")
# satang.display_info()
'''
satang이라는 인스턴스는 생성된 '이후'에 set_info() 메서드를 호출하여 "구형" 모양의,
"갈색"이라는 속성을 갖게 됨
    
satang 인스턴스의 생성 과정
  1. 값이 없는(속성에 값이 대입 되어있지 않은) 인스턴스 생성
  2. 값을 저장할 수 있는 메서드 호출
      
그렇다면 처음부터 값이 있는 인스턴스를 생성하면 코드 라인이 출어들지 않을까.
이에 대한 해답이 생성자라는 개념이고,
C / Java의 경우의 생성자는 클래스 명과 동일한데, 또 python만 이상한 방식으로 만듦
-> __init___() 라는 메서드
      
__init__() : 메서드(생성자)는 인스턴스가 생성될 때 '자동으로 호출되기 때문에 인스턴스 변수의
'초기화'용도로 사용, 즉 값이 있는 인스턴스를 생성할 수 있다는 의미
'객체 생성과 동시에 생성자가 호출됨 -> 초기값을 작성할 때 사용한다는 의미
      
형식 :

class 클래스명:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
'''
# class Candy2():
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#     def display_info(self):
#         print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")
#
# satang2 = Candy2("정육면체", "흰색")
# satang2.display_info()
'''
이상에서 주목해야 할 점은 satang 인스턴스와 satang2인스턴스의 생성 방식의 차이임

2. 소멸자(Destructor)
  인스턴스가 생성될 때 자동으로 생송되는 생성자와 마찬가지로 인스턴스가 소멸될 때 호출되는 메서드
  이를 소멸자라고 하며, 소멸자를 정의한느 메서드는 __delf__()
'''
# class Sample:
#     def __init___(self):
#         print("인스턴스가 생성되었습니다.")         # 생성자 생성할 때 속성에 값만 대입하는게 아니라 출력으로 삽입할 수도 있음.
#
#     def __del__(self):
#         print("인스턴스가 소멸되었습니다.")
#
# sample = Sample()
#
# del sample      # del 객체명으로 소멸자를 원하는 시기에 호출할 수 있음
#
# #여기 부분에 추가적인 로직을 작성하여 더 프로그램이 진행 된 후에 프로그램 전체 종료가 이루어질 수 있음
#
# print("프로그램이 종료되었습니다.")
'''
기본 예제

생성자를 이용해서 용량을 가진 usb인스턴스를 만드는 프로그램을 작성해라

지시사항
1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수 capacity를 받을 것
3. get_info() 메서드를 저의할것

main 단계 코드
usb = USB(64)
usb.get_info()

실행 예 
64GB USB
'''
# class USB:
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def get_info(self):
#         print(f"{self.capacity}GB USB")
#
# # 객체 생성 및 get_info() 메서드  호출
# usb = USB(64)
# usb.get_info()
'''
생성자와 소멸자를 이용하여 서비스 안내 메시지를 출력하는 프로그램을 작성

class Service를 정의하고, 생성자를 통해 매개변수를 service로 받고, print()메서드를 생성자와 소멸자 내에 작성하시오

main 단계에서의 작성
s = Service("길안내")
del s

실행 예
길 안내 Service가 시작되었습니다
길 안내 Service가 종료되었습니다
'''
# class Service:
#     def __init__(self,service):
#         self.service = service
#         print(f"{self.service} Service가 시작되었습니다.")
#
#     def __del__(self):
#         print(f"{self.service} Service가 종료되었습니다.")
#
# s = Service("길안내")
# print("프로그램이 종료되는 시점")
# del s
'''
응용 예제

1. 다음 지시 사항을 읽고 이름을 저장하는 Person 클래스를 생성해라

지시 사항

1. 다음과 같은 방법으로 man과 woman인스턴스를 생성해라
man = Person("james")
woman = Person("emily")
2.man과 woman인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성해라
james is born
emily is born

3. 다음과 같은 방법으로 man 인스턴스를 삭제해라
del man

4. 인스턴스가 삭제되면 메시지를 출력해라
james is dead
'''
# class Person:
#     def __init__(self, people):
#         self.people = people
#         print(f"{self.people} is born.")
#
#     def __del__(self):
#         print(f"{self.people} is dead.")
#
# man = Person("james")
# woman = Person("emily")
#
# del man
#
# print("james is dead.")
'''
예제 1.
  학생들의 성적을 관리하는 Student 클래스를 작성해라. 이 클래스는
  학생의 이름, 학번, 성적을 인스턴스 변수로 가짐
  
  지시사항 
    1) Student 클래스르 정의하고 생성자를 통해 name, student_id, grade를 초기화해라
    2) 학생의 프로필을 출력하는 인스턴스 메서드 print_grade()를 작성해라.(call1()타입으로 : 매개변수 x 리턴 x)
    3) 학생의 성적을 변경할 수 있는 인스턴스 메서드 set_grade()를 작성해라
      -> '이 부분이 고민해볼만함 // set_info()메서드를 검색해 보라ㅏ ctrl + shift + f 눌려서
    4) 세 명의 학생 인스턴스를 생성하고 각 학생의 정보를 출력한 다음 
      성적을 변경하고 다시 출력해라
      
  student1 = Student("김철수", 20250001, "A")
  student2 = Student("이영희", 20250001, "B")
  student3 = Student("박민지", 20250001, "C")
  
  실행 예
  
  학생 이름 : 김철수
  학번 : 20250001
  성적 : A
  
  student2 / stuendt 3도 출력해라
  
  이후 성적 student1 성적을 A+ / student2 는 A / student3은 B+로 성적을 변경하고
  다시 print_profile을 적용하여 출력해라
'''
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def print_info(self):
        print(f"학생 이름 : {self.name}\n학번 : {self.student_id}\n성적 : {self.grade}")
    def set_info(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade