# 1부터 n까지의 제곱의 합

n = int(input("숫자를 입력하여 주요.: "))
i = 1
sum = 0

while i <= n:
    sum += i ** 2
    i += 1
print("계산값은",sum,"입니다")