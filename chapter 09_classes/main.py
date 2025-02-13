'''
1. 클래스 도입의 필요성
'''
# 매개변수가 6개인 함수를 하나 정의함
def student_info(name, department, professor, phone, address, grade):
    print(name)
    print(department)
    print(professor)
    print(phone)
    print(address)
    print(grade)

name1 = "안근수"
department1 = "영어교육과"
professor1 = "David"
phone1 = "010-2112-6546"
address1 = "부산광역시 연재구"
grade1 = "A"

student_info(name1,department1,professor1,phone1,address1,grade1)
'''
지금까지 배운 함수와 매개변수, 그리고 argument를 통해 6개의 변수를 처리했습니다. 하지만
만들어야 할 변수의 개수가 많고, 학생 한 명당 매개변수가 6개라면, 학생이 100명일 경우 600개의
변수를 처리할 필요가 있음
'''
student_info(grade="B", address="서울특별시 종로구",phone="010-1234-1324", professor="John", department="computer science", name="김일")
# name2, ... grade2라는 변수들을 선언하고, 거기에 여러분들의 정보를 입력하 ㅜ디
# keyword argument를 통해 student_info() 함수를 호출해라.

name2 = "이현민"
department2 = "인공지능공학과"
professor2 = "aiden"
phone2 = "010-6243-5714"
address2 = "부산광역시 남구"
grade2 = "A"

student_info(name2,department2,professor2,phone2,address2,grade2)

'''
이상의 상황들(변수에 각각 데이터를 대입한 후에 함수의 argument로 사용하거나, 혹은 데이터를 직접 argument에 등록)을
벗어나기 위해 클래스와 객체 개념을 도입함.

class란?: 객체를 만드는 도구 - 설계도 / 틀 / 청사진
  자동차 설계도 -> 클래스
  설계도를 통해 생성된 자동차들 -> 객체
  
  같은 설계도로 만든 자동차라 하더라도 서로 다른 옵션을 가질 수 있음
  마찬가지로 같은 클래스로 만든 객체라 하더라도 서로 다른 값을 가질 수 있음
  
  인스턴스(instance)역시 클래스를 이용해서 생성한 객체를 가리키는 용어.
  객체와 인스턴스는 그 둘을 바라보는 관점의 차이로 볼 수 있음
  
  1. '자동차 설계도'로 만든 자동차는 객체(object)임
  2. 자동차는 자동차 설계도의 인스턴스(instance)임
  
1. 클래스 정의
  클래스를 작성하는 것을 클래스 정의라고 합니다 -> 함수 정의를 생각하면 됨
  
형식 :

class 클래스명(대문자로 시작):
  본문
---------------------------
객체생성형식 :
                                            -> 함수 호출을 생각하면 일부 비슷함
객체이름 = 클래스명()
'''
# 클래스 정의 형식 예시
class WaffleMachine:                # 클래스명은 대문자로 시작, Pascal Case로 표기함. python에서 변수는 snake_case
    pass                            # 나중에 코드를 작성해겠다는 의미로 이 경우 실행시켜도 오류가 나지 않음

# 객체 생성 예시
waffle = WaffleMachine()            # 소괄호()가 중요함. 추후 사용 예정
print(waffle)
'''
print(waffle)을 실행시켰을 때 <__main__.WaffleMachine object at 0x000001CA4B6568D0>에서 object라고 
표기된 점을 미루어 waffle은 WaffleMachine의 객체임을 확인할 수 있음

클래스의 구성

1. 클래스의 기본 구성
  객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소를 지님.
  객체를 생성하기 위해서는 클래스는 객체가 가져야 할 '값'과 '기능'을 지녀야 함
  
  값 = 속성(attribute)
  기능 = 메서드(method)
  
  클래스를 구성하는 변수는 두가지로 구분됨
    1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수
    2) 인스턴스 변순 : 인스턴스 들이 개별적으로 가지는 변수
  
  메서드는 특징에 따라서
    1) 클래스 메서드
    2) 정적 메서드
    3) 인스턴스 메서드
    
  인스턴스 변수 : 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수를 의미
    모든 인스턴스 변수는 self라는 키워드를 앞에 붙여줌
  인스턴스 메서드 : 인스턴스 변수를 사용하는 메서드
    인스턴스 변수값에 따라서 각 인스턴스마다 다르게 동자됨
    인스천스 메서드는 첫번째 매개변수로 self를 추가해야 함
'''