# n**2 > 500 인 가장 작은 n 찾기

# for 구조
# for n in range(1, 30):
#     if n ** 2 > 500:
#         print(n, n**2)
#         break

#while 구조
n = 1
while n**2 < 500:
    n += 1
print(n, n**2)