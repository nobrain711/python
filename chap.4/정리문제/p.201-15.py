# 수열의 합을 구하는 프로그램

#for 구조
# sum = 0
# for n in range(1, 100, 2):
#     sum += n / (n + 2)
# print("계산된 값은",sum,"입니다.")

#while 구조
n = 1
sum = 0 
while n <= 99:
    sum += n/(n+2)
    n += 2
print("계산된 값은",sum,"입니다.")