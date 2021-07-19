import turtle
t = turtle.Turtle()
t.shape("turtle")

def draw_line():
    t.forward(100)
    t.backward(100)
    t.right(30)
    

for i in range(12):
    draw_line()
    
    
turtle.mainloop()
turtle.bye()