from turtle import Turtle,Screen

# turtle이라는 모듈을 사용할건데, Turtle, Screen 클래스를 import 할거임.

t = Turtle()            # Turtle 클래스의 객체 생성; 이름은 t
screen = Screen()       # Screen 클래스의 객체 생성
t.shape("turtle")
screen.bgcolor("black")
t.color("white")
# t.penup()
# t.forward(100)
# t.pendown()
# t.forward(200)

# for _ in range(10):           # 그냥 반복을 10번하는거고 변수를 사용하지 않기 때문에 _를 사용함.
#     t.forward(20)
#     t.penup()
#     t.forward(20)
#     t.pendown()

# t.left(90)
# t.forward(100)

# for _ in range(4):        # 사각형
#     t.forward(100)
#     t.left(90)

# for _ in range(3):        # 삼각형
#     t.forward(100)
#     t.left(120)



screen.exitonclick()