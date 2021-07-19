# 01
name = input("이름을 입력하시오. ")
department = input("학과을 입력하시오. ")
yid = input("학번을 입력하시오. ")

print("학생정보는",name+'-'+department+'-'+yid,"입니다.")

# 02
def calc_add(a,b):
     return a + b 

def calc_sub(a,b):
    return a - b

def calc_product(a,b):
    return a * b

def calc_division(a,b):
    return a / b

x = int(input("첫번째 숫자를 입력하여 주세요.: "))
y = int(input("두번째 숫자를 입력하여 주세요.: "))

print('(', x,"+", y,") =",calc_add(x,y))
print('(', x,"-", y,") =",calc_sub(x,y))
print('(', x,"*", y,") =",calc_product(x,y))
print('(', x,"/", y,") =",calc_division(x,y))

# 03
def p(a):
    print("구한 짝수는 :",end=" ")
    for i in a:
        print(i,end=" ")
    print("")
    print("합 =",sum(a))
def div(x):
    n2 = []
    n = [i for i in range(x,31,1)]
    for i in n:
        if i % 2 == 0:
            n2.append(i)
    return n2
    
def choioce(x):
    if x > 30:
        print("입력오류. 30보다 작은 수를 입력해야 합니다.")
        return "bad"

m = int(input("시작할 수는? "))
while choioce(m) == "bad":
    m = int(input("시작할 수는? "))
list1 = div(m)
p(list1)

# 04
def cel2fah(cel):
    fah = (9/5) * cel + 32
    return fah
    
for i in range(10,51,10):
    print("섭씨",str(i)+'도 =','화씨',str(cel2fah(i))+'도')
    
# 05
A = ['aba','xyz','abc','121']
cnt = 0
for i in range(len(A)):
    word = A[i]
    if word[0] == word[-1]:
        cnt += 1
print(A)
print("문자열의 개수 =",cnt)

# 06
list1 = [i for i in range(1,7)]
list2 = [i for i in range(6,11)]

print(list1)
print(list2)

for x in range(len(list1)):
    for y in range(len(list2)):
        xl = list1[x]
        yl = list2[y]
        if xl == yl:
            d = True
            break
        else:
            d = False
print(d)

# 07
import turtle

t=turtle.Turtle()

aList = [x for x in range(10,130,10)]
for x in aList :
    t.fd(x)
    t.stamp()
    t.backward(x)
    t.right(30)

turtle.mainloop()
turtle.bye()	
