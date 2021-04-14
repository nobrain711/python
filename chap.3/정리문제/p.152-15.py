x = int(input("숫자를 입력하여 주세요.: "))

if x % 3 == 0 and x % 5 == 0:
    p = "Python Express"
elif x % 3 == 0:
    p = "Python"
elif x % 5 == 0:
    p = "Express"

print(p)