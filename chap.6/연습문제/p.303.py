# 10번 문제
import turtle
import random

def draw(w,h,c,x,y):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(c)
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    
    
def choice(x,y,c,a,b):
    x = random.choice(x)
    y = random.choice(y)
    c = random.choice(c)
    a = random.choice(a)
    b = random.choice(b)
    return x,y,c,a,b

color = ["yellow","red","purple","blue"]
w = [x for x in range(100,500,50)]
h = [x for x in range(100,500,50)]
x = [x for x in range(-300,300)]
y = [x for x in range(-300,300)]
w,h,c,x,y = choice(w,h,color,x,y)
draw(w,h,c,x,y)

turtle.mainloop()
turtle.bye()	

# 12번 문제
