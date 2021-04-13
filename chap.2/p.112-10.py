side = int(input('길이를 입력해 주세요.'))

import turtle

t = turtle. Turtle()
t.shape("turtle")

t.forward(side)
t.left(120)
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)

turtle.mainloop()
turtle.bye()