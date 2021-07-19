#함수 없는 버전
x = int(input("첫 번째 숫자를 입력하여 주세요.: "))
y = int(input("두 번째 숫자를 입력하여 주세요.: "))

z = x + y

print(z)

#함수버전
def add_find(a, b):
    c = a + b
    return c
x = int(input("첫 번째 숫자를 입력하여 주세요.: "))
y = int(input("두 번째 숫자를 입력하여 주세요.: "))

z = add_find(x, y)

print(z)