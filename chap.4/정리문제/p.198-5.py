#for 구조
n = int(input("숫자를 입력하여주세요.: "))
for x in range(1,n + 1):
    s = 1
    for y in range(1,x + 1):
        print(s,end=" ")
        s += 1
    print("")

#while 구조
n = int(input("숫자를 입력하여주세요.: "))
x = 1
while x <= n:
    s = 1
    y = 1
    while y <= x:
        print(s,end=" ")
        s += 1
        y += 1
    x += 1
    print("")