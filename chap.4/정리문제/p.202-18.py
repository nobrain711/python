import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for i in range(1,11):
    r = random.randint(1, 100)
    t.forward()