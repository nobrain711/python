def deci2bin(n):
    b = []
    while n != 0:
        i = n % 2
        b.append(i)
        n = n // 2
    return b

x = int(input("숫자를 입력하시오.: "))
c = deci2bin(x)
for i in c[:: -1]:
    print(i,end="")