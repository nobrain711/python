a = int(input("첫 번째 정수를 입력하시오.: "))
b = int(input("두 번째 정수를 입력하시오.: "))

for n in range(1, b+1):
    if a % n == 0 and b % n == 0:
        max = n
print(a,"와 ",b,"의 최대 공약수는 ",max,"입니다.")