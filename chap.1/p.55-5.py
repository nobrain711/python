#거북이 전진 값 주는 버전
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.left(90)
# t.forward(100)

# turtle.mainloop()
# turtle.bye()

#거북이 전진 값 변수로 주는 버전
size = int(input("숫자를 입력하세요.:"))
import turtle

t = turtle.Turtle()
t.shape("turtle")

t.forward(size)
t.left(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.left(90)
t.forward(size)

turtle.mainloop()
turtle.bye()