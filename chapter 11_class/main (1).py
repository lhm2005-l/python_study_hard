'''
1. 클래스 변수
  인스턴스 변수 : 인스턴스마다 서로 다른 값을 지니는 변수
  클래스 변수 : 몯ㄴ 인스턴스가 동일한 값을 지니는 변수

  인스턴스 변수 :
    목적 - 인스턴스 마다 서로 다른 값을 저장
    접근 방식 - 인스턴스 접근(o)
            - 클래스 접근(o)

  클래스 변수 :
    목적 - 인스턴스가 공유하는 값을 저장
    접근 방식 - 인스턴스 접근(o)
            - 클래스 접근(o)
'''
# 클래스 변수 예제
# class Korean:
#     country = "한국"
#     # 인스턴스 변수의 경우 생성자 내부에 있었음. 클래스 변수의 경웽는 이상처럼
#     # 클래스 내부에 그냥 선언하고 초기화하면 됨
#
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
# # 객체 생성
# man = Korean(name = "안근수", age=38, address="부산광역시 연제구")
# print(man.name)
# print(man.age)
# print(man.address)
# # 클래스 변수 확인 방법
# print(man.country)      # 객체명.클래스변수명을 통한 접근 : 가능
# print(Korean.country)   # 클래스며.클래스변수명을 통한 접근 : 가능

# 객체명.클래스변수를 통해서 클래스 변수에 접근이 가능하긴 하지만 클래스 내부의 코드를 들여다보기 전까지는 cuntry라는 변수가
# 클래스 변수인지 인스턴스 변수인지 확인이 불가능하다는 문제가 있음

# 이상을 이유로 클래스 변수를 확인하고자 할 때는 객체명.클래스변수명으로 참조하기 보다는
# 클래스명.클래스변수명을 통해서 참조하늑 서이 바람직함.

'''
클래스 메서드 : 클래스 변수를 사용하는 메서드
'''
# class Korean2:
#     country = "대한민국"        # 클래스 변수 선언 및 초기화
#
#     # 클래스 메서드 정의 법
#     @classmethod                                # 얘를 명시하면 밑의 코드가 클래스 메서드로 작성됨
#     def trip(cls, travelling_site):         # 그 결과 첫번쨰 매개변수로 self가 아니라 cls가 자동완성됨
#         if cls.country == travelling_site:
#             print("국내 여행입니다")
#         else:
#             print("해외 여행입니다")
#
# # 클래스 메서드의 호출
# Korean2.trip("대한민국")
# Korean2.trip("미국")
# # 객체들 여기서 생성
# man2 = Korean2()
# man2.trip("일본")
# 클래스 변수 때와 마찬가지로 객체명클래스메서드명()으로 호출 가능
#-> 하지만 마찬가지로 얘가 인스천스 메서드인지 클래스 메서드인지 구분할 수 없기 때문에 구너장되는 코드 작성 요령이 아님.
'''
2. 클래스 메서드 :
  클래스 변수들을 사용하는 메서드
  
  특징 :
    1) 인스턴스 또는 클래스로 호출 -> 하지만 클래스 변수와 마찬가지로 클래스로 호출하는 것을 권장
    2) 생성된 인스턴스가 없어도 호출가능(클래스로 호출 가능하니까)
    3) @classmethod 데코레이터를 표시하고 작성
    4) 메게변수 self를 쓰지 않고 cls를 사용 -> self는 객체를 의미하기 때문(즉 self는 인스턴스에 사용함)
    
  호출 방식 :
    클래스명.메서드명() -> self를 사용하지 않기 때문에 '인스턴스 변수에 접근이 불가능', cls를 통해 클래스 변수에만 접근 가능
    
korean2 클래스에서 정의된 trip() 메서드는 클래스 메서드임을 알리는 @classmethod로 시작,
첫 번쨰 매개변수인 cls.country는 Korean2.country와 동일한 의미. 이를 클래스 내부에서는 cls.country로 표기
클래스 메서드는 인스턴스를 생성하지 않아도 클래스만으로 호출 가능. 즉 Korean2.trip(argument)로 호출 가능

3. 정적 메서드 :
  정적메서드 또한 self를 사용하지 않음 -> 즉, 인스턴스 변수에 접근하여 사용하는 것이 불가능함을 의미.
    - 클래스 메서드와의 공통점 #1
  인스턴스를 생성하지 않아도 사용할 수 있음 -> 클래스 메서드와의 공통점 #2
  
  특징 :
    1) 인스턴스 또는 클래스로 호출 가능 -> 클래스 메서드와의 공통점
    2) 생성된 인스턴스가 없어도 호출 가능 -> 클래스 메서드와의 차이점
    3) @staticmethod 데코레이터를 표기하고 작성 -> 클래스 메서드와의 차이점 #1
    4) 반드시 작성해야 할 매개변수(self, cls)가 없음 -> 클래스 메서드와의 차이점 #2
    
정적 메서드는 self, cls를 다 사용하지 않기 때문에 인스턴스 / 클래스 변수 모두 사용하지 않는 메서드를 정의하는 경우에 적합함.
정적 메서드는 클래스에 소속 돼있지만 인스턴스에는 영향을 주지도 않고, 또한 영향을 받지도 않음
'''
# class Korean3:
#     country = "한국"
#
#     @staticmethod           # 정적 메서드 선언
#     def slogan():           # self, cls가 자동 생성되지 않았음. -> 인스턴스/클래스 변수 참조 안하니까
#         print("Imagine your Korea!")
#
#     @staticmethod
#     def slogan2(str_example):
#         print("Imagine your Korea!" + str_example)
#
# Korean3.slogan()
# Korean3.slogan2("근데 너무 춥다")
'''
기본 예제

가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스를 정의
'''
# class Bag:
#
#     count = 0           # 클래스 변수 선언 및 초기화
#
#     def __init__(self):         # 생성자 / 인스턴스 메서드에 해당함 -> 아무 @가 없으니까
#         Bag.count += 1          # 객체를 하나 생성할 때마다 클래스 변수인 count가 1씩 증가
#         print("가방이 생성되었습니다")     # 인스턴스 메서드가 클래ㅡ 변수를 참조할 때는 클래스명.클래스변수명으로 접근
#
#     @classmethod
#     def sell(cls):
#         print("가방이 팔렸습니다.")
#         cls.count -= 1              # 클래스 메서드가 클래스 변수에 접근하기 때문에 Bag.count가 아니라 cls.count임
#
#     @classmethod
#     def remain_bag(cls):            # 클래스 변수를 main단계에서 직접 참조하는 것이 보안상 좋지 않기 때문에
#         return cls.count            # 클래스 메서드를 생성(getter 형태로)하여 참조하는 방식
#
# print(f"현재 가방 재고 : {Bag.count}")            # 클래스 변수명을 직접 참조
# print(f"현재 가방 재고 : {Bag.remain_bag()}")     # 클래스 변수를 getter로 통해 메서드를 경유하여 참조 -> 보안상 더 좋음
#
# bag1 = Bag()                                    # 생성자 상기해야하는데 아무런 속성이 없기 때문에 안에 argument를 채울 필요가 없음
# print(f"현재 가방 재고 : {Bag.remain_bag()}")     # 클래스 변수를 클래스 메서드르 통해 조작할 수 있음
# bag2 = Bag()
# bag3 = Bag()
# print(f"현재 가방 재고 : {Bag.remain_bag()}")
# bag1.sell()     # 인스턴스명.클래스메서드명()으로 호출
# print(f"현재 가방 재고 : {Bag.remain_bag()}")
# Bag.sell()      # 클래스명.클래스메서드명()으로 호출 -> 더 권장 되는 방식
# print(f"현재 가방 재고 : {Bag.remain_bag()}")
'''
이상의 코드에서 보면 예시이기 때문에 적합하다고 보기 힘든데
인스턴스명.sell()로 작성한다면 특정한 가방 인스턴스가 팔렸다고 볼 수 없기때문에 가독성이 더 높은 반면
Bag.sell()로 작성하게 된다면 어떤 가방이 팔렸는지는 모르고 그냥 가방 count 변수만 하나 좋았음

우리는 코딩할 때 변수 / 메서드를 인스턴스 수준으로 작성할지 혹은 클래스 수준으로 작성할지에 대한 고민이 선행되어야만 할것임.

응용 예제

1. 다음 지시사항을 읽고 이름과 전체 인구수를 저장 할 수 있느 Person 클래스를 작성해라

지시사항

1. 다음과 같은 방법으로 man과 woman으로 인스턴스를 생성해라
man = Person("안근수')
woman = Person("안근순")

2. man과 woman인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성해라.
안근수가 태어났습니다
안근순이 태어났습니다

3. 다음 코드를통해서 전체 인구수를 조회할 수 있도록 작성해라
print(f"전체 인구수 : {Person.get_population()}")

4, 다음과 같은 방법으로 man인스턴스를 삭제해라
del man

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 소멸자를 정의래하
RIP 안근수
'''
# # 나
# class Person:
#     people_count = 0
#     def __init__(self, people):
#         self.people = people
#         print(f"{people}가 태어났습니다.")
#
#     def get_population(self
#                        ):
#         Person.people_count += 1
#
# man = Person("안근수")
# woman = Person("안근순")
# print(f"전체 인구수 : {Person.get_population()}")
#
# del man
# print("RIP 안근수")
#
# # 선생님
# class Person:
#     population = 0          # 클래스 변수 선언 및 초기화 -> 전체 인구수이기 때문에 인스턴스 변수가 아님
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
#         print(f"{self.name}이(가) 태어났습니다")
#
#     @classmethod
#     def get_population(cls):
#         return cls.population
#
#     def __del__(self):
#         Person.population -= 1          # 객체가 소멸되었을때 전체 인구수가 줄어야 한다는 점을 고려했을 떄 추가한 게 -= 1 파트가 됨
#         print(f"RIP {self.name}")
#
# man = Person("안근수")
# woman = Person("안근순")
# del man
# print(f"전체 인구수 : {Person.get_population()}")
# print("프로그램이 종료되었습니다")
'''
클래스 변수 / 클래스 메서드 활용 예제

다음 지시사항을 일고 가게의 매출을 구할 수 있는 shop 클래스를 작성해라

지시사항
1. shop클래스는 다음과 같은 변수를 가지고 있음
  total : 가게 전체 매출액
  menu_list : {메뉴명:가격}으로 이루어진 딕셔너리 요소를 가지는 리스트
  
  menu_list = [{"떡볶이":3000},. {"순대":4000}, {"튀김":500}, {"김밥":2000}]
  
2. 매출이 생기면 다음과 같은 방식으로 판매량을 작성함
shop.sales("떡볶이:, 1)            # 떡볶이를 1개 판매
shop.sales("김밥:, 2)                # 김밥을 2개 판매
shop.sales("튀김:, 5)   # 튀김을 5개 판매

3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인함
print(f"매출 : {shop.get_total()} 원")
'''
class Shop:
    total = 0
    menu_list = [{"떡볶이":3000}, {"순대":4000}, {"튀김":500}, {"김밥":2000}]
    menus = {"떡볶이":3000,
             "순대":4000,
             "튀김":500,
             "김밥":2000}

    @classmethod
    def sales2(cls, menu_key, account):
        # for key in cls.menus:
        #     if key == menu_key:
        #         cls.total cls.menus[key] * account
        if menu_key in cls.menus:
            cls.total += cls.menus[menu_key] * account

    @classmethod
    def get_total(cls):
        return cls.total

    @classmethod
    def sales(cls, menu_name, quantity):
        # menu_name을 argument로 받았을 때 걔가 리스트내의 요소의 key에 해당하는지 확인해야하고 그 key에 맞는 value를 도출해서 quality와 관한 결과값을
        # 클래스의 변수인 total 에 더해줘야 전체 매출액이 변경됨
        for menu_dict in cls.menu_list:
            if menu_name in menu_dict:          # menu_dict의 key를 줌 menu_name에 해당하는 것이 있다면, 에 해당하는 조건문임
                cls.total += menu_dict[menu_name] * quantity
                print(f"{menu_name}을(를) {quantity}개 판매")

Shop.sales("떡볶이",1)
Shop.sales("김밥", 2)
Shop.sales("튀김", 5)

print(f"매출 : {Shop.get_total()}원")