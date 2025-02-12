'''
1. for 반복문의 기본 개념:
  정해진 구간 혹은 집합 내의 요소들을 순서대로 꺼내면서 반복 작업을 수행.
  예를 들어 아까전에 문자열의 index개념을 할습했음
  String의 경우에는 문자열의 문자 개수 만큼 반복이 진행된다고해석할 수 있음

    1) 숫자 범위를 이용한 반복
      range(): 몇 번 반복할 것인가를 지정하는 함수 -> 특히 for문과 연계돼서 자주 쓰임
'''

# 1부터 10까지를 출력하는 while반복문
# n = 1
# while n < 11:
#     print(n)
#     n += 1

# # 1 부터 10까지를 출력하는 for 반복문
# for i in range(11):       #현재 상황에서의 반복 횟수는 11번
#     print(i)

# for i in range(10):      #얘는 반복횟수 10번인데, 여기서 중요한 것은 시작 지점이 0부터라는 점
#     print(i+1)

'''
range()함수의 응용 :
  range((시작값), 종료값, (증감값))
    시작값 : 생략 가능, 생략할 경우 0부터 시작
    종료값 : 명시하지 않으면 끝까지 진행
    증감값 : 생략 가능, 생략할 경우 1씩 증가       -> 인덱싱의 슬라이싱 개념이랑 유사

for 반복문 형식:
for i(변수이므로 아무거나 사용가능) in range(시작, 종료, 증감):
    반복 실행문
'''

# for i in range(1, 10, 1):       # 종료값이 10인데 9까지 나타남
#     print(i)                    # 종료값 바로 앞까지 출력이 이루어짐

'''
2) 문자열을 이용한 반복
  문자의 경우 []을 통해 내부에 인덱스 넘버를 명시할수 있다
  그래서 in range()를 사용하는 방법 및 향상된 for문을 사용하는 방법을 통해 문자를 하나씩 추출할 수 있다.
'''
name = "dlgusals"
# # (1) in range()를 이용하여 문자를 추출하는 방법
# for i in range(len(name)):      #len() : ()안에 들어가는 요수의 길이를 반환하는 함수
#     print(name[i])

# (2) enhanced for loop를 통한 방식
# for letter in name:   # name이라는 string에서 각 문자 하나씩을 뽑아 letter에 대입
#     print(letter)
#
# # 첫 번째 반복의 경우
# letter = name[0]
# print(letter)
# # 두 번째 반복
# letter = name[1]
# print(letter)
# # ...
# letter = name[8]
# print(letter)

'''
대부분의 경우 반복문을 사용하게 되면 반복 대상이 되는 객체는 복수형의 변수명을 지님.
ex) numbers = [1,2,3,4,5]

for number in numbers:
  print(number)

향상된 for loop의 형식 :
for 변수 in 반복대상객체:
    반복실행문
    
반복대상객체(iterable) : 내부에 요소가 다수 들어가 있어 반복적으로 요소의 데이터를 다룰 수 있는 객체
    ex) str, list, tuple, set, dict -> 현제 저희는 str만 기준으로 수업 중
    
주의 사항:
  if 조건문과 마찬가지로 들여쓰기가 매우 중요
문자열에서 특정 문자의 개수 세기
'''

count_a = 0
count_letters = 0

for letter in "banana":
    if letter == "a":
        count_a += 1
    print(letter)
    count_letters += 1
print(f"a의 개수 : {count_a}")
print(f"전체 문자의 개수 : {count_letters}")
print(f"전체 문자의 개수 : {len("banana")}")

'''
reeborg's world hurble # 1
for a in range(6):
    for i in range(2):
        move()
        turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    
n = 0
while n < 6:
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    n += 1

reeborg's world hurble # 2
def turn_right():
    for _ in range(3):
        turn_left()
        
for _ in range(6):
    move()
    turn_left()
    move()
    for _ in range(2):
        turn_right()
        move()
    turn_left()
    

def turn_right():
    for _ in range(3):
        turn_left()
        
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()
    
reeborg's world hurble # 3
def turn_right():
    for _ in range(3):
        turn_left()
   
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
reeborg's world hurble # 4
def turn_right():
    for _ in range(3):
        turn_left()
   
def jump():    
    turn_left()
    while  wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
def turn_right():
    for _ in range(3):
        turn_left()
    
#오른쪽만 막혀있을때 -> 앞으로
#오른쪽과 앞이 막혔을때 -> 왼쪽으로
# 오른쪽이 비어있을 때 -> 오른쪽으로 
# 나   
def jump():
    while wall_on_right():
        if wall_on_right() and wall_in_front():
            turn_left()
        else:
            move()
    while not wall_on_right():
       turn_right()
       move()

if at_goal():
    done()
else:
    jump()
'''