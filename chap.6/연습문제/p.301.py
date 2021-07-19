# 1번문제(for)
a=[]
n = int(input("원하는 횟수를 입력하여주세요.: "))
for i in range(n):
   a.append(int(input("숫자를 입력하여주세요.: ")))
print("값의 합계는", sum(a),"입니다.")

# 1번 문제(while)
a=[]
n = int(input("원하는 횟수를 입력하여주세요.: "))
while len(a) != n:
    a.append(int(input("숫자를 입력하여주세요.: ")))
print("값의 합계는", sum(a),"입니다.")

# 2번 문제(for)
import random
valuse=[]
for i in range(10):
    valuse.append(random.randint(1, 100))    
print(valuse)

# 2번 문제(while)
import random
valuse=[]
while len(valuse) != 10:
    valuse.append(random.randint(1, 100))
print(valuse)

# 3번 문제(for)
start = []
count = int(input("원하는 횟수를 입력하여 주세요.: "))
print(count,end=" ")
for i in range(count):
    start.append("*")
    print(start[i],end='')
    
# 3번 문제(while)
start = []
count = int(input("원하는 횟수를 입력하여 주세요.: "))
print(count,end=" ")
while len(start) != count:
    start.append('*')
i = 0
while i != count:
    print(start[i],end='')
    i += 1
# 4번 문제(열은거)
a = [i for i in range(1,11)]
print("실행전",a)
a = []
for i in range(1,11):
    if 3<=i<=8:
        a.append(i*-1)
    else:
        a.append(i)
print("실행후",a)

# 4번 문제(합축)
a = [i for i in range(1,11)]
print("실행전",a)
a = [i *-1 if 3 <= i <= 8 else i for i in range(1,11)]
print("실행후",a)

# 5번 문제(열은거)
a = ['aba','xyz','abc','121']
c = 0
for i in range(len(a)):
    word = a[i]
    if word[0] == word[-1]:
        c += 1
print("문자열의 개수는",c)

