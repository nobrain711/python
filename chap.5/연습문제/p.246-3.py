def calc(a,b):
    return a + b, a - b, a * b, a / b 

x = int(input("첫번째 숫자를 입력하여 주세요.: "))
y = int(input("두번째 숫자를 입력하여 주세요.: "))

add,sub,m,d = calc(x,y)
print(add,sub,m,d)