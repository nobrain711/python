import math

a = float(input("숫자를 입력하여 주세요.: "))
b = float(input("숫자를 입력하여 주세요.: "))
c = float(input("숫자를 입력하여 주세요.: "))

r = math.sqrt(b**2 - 4*a*c)/(2*a)

print(r)