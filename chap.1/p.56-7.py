#두깨와 전진 값을 주는 버전
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")
# t.width(10)

# t.forward(100)
# t.left(90)
# t.forward(100)

# turtle.mainloop()
# turtle.bye()

#두깨와 전진 값을 변수로 주는 버전

import turtle
size = int(input("길이를 입력하세요.:"))
widith = int(input("두깨를 입력하게요.:"))

t = turtle.Turtle()
t.shape("turtle")
t.width(widith)

t.forward(size)
t.left(90)
t.forward(size)

turtle.mainloop()
turtle.bye()