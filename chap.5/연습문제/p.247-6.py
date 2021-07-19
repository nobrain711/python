def add(x,y):
    z = int(input(f'{x}+{y}의 합은 : '))
    return z

a = int(input("첫 번째 정수를 입력하여 주세요.: "))
b = int(input("두 번째 정수를 입력하여 주세요.: "))
c = add(a, b)
if a + b == c:
    print("정답 입니다.")
else:
    print("오답입니다.")
    print("정답은",a+b,"입니다.")