def getSorted(x ,y):
    temp = x
    x = y
    y = temp
    return x, y

a = int(input("첫 번째 정수를 입력하시오.: "))
b = int(input("두 번째 정수를 입력하시오.: "))
getSorted(a, b)
print(f'값은 {getSorted(a,b)}입니다.')