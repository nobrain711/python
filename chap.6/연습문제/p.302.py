# 6번 문제
list1 = [i for i in range(1,7)]
list2 = [i for i in range(6,11)]

print(list1)
print(list2)

for x in range(len(list1)):
    for y in range(len(list2)):
        xl = list1[x]
        yl = list2[y]
        if xl == yl:
            div = True
            break
        else:
            div = False
print(div)

# 7번 문제
import random
list1 = ["a"+str(i) for i in range(10)]
print(random.choice(list1))

# 8번 문제
a = [1,2,3,4,5]
b = [1,3,3,4,5,6,7]

new = [x for x in a if x in b]
print(new)

# 9번 문제
import turtle

t=turtle.Turtle()

my_list = [x for x in range(10,130,10)]
for x in my_list:
    t.fd(x)
    t.stamp()
    t.backward(x)
    t.right(30)

turtle.mainloop()
turtle.bye()	
