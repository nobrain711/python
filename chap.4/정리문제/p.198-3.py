# 3. 3의 배수의 합(3증가 방법)
sum = 0
for i in range(1, 101):
    if i % 3 == 0:
        sum = sum + i

print("1부터 100까지의 합은 ", sum, "입니다.")