# 3. 3의 배수의 합(3증가 방법)
sum = 0
#1씩 증가 방법
# for i in range(1, 101):
#     if i % 3 == 0:
#         sum = sum + i

#3씩 증가 방법
for i in range(0, 101, 3):
    sum += i

print("1부터 100까지의 3의 배수 합은 ", sum, "입니다.")