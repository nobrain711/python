# 작성한 풀이

# a, b, c = eval(input('수를 입력하세요.:'))
# print(a, b, c)
# if a < b :
#     min = a
#     if min < c:
#         min = min
#     else :
#         min = c
# elif b < c:
#     min = b
# else :
#     min = c

# print(f'입력받은 {a, b, c}중 가장 작은 수는{final_min}입니다.')

#교수님 풀이

a, b, c = eval(input('수를 입력하세요.:'))
print(a, b, c)
if a < b :
    min = a
else :
    min = b
if min < c:
    final_min = min
else :
    final_min = c

print(f'입력받은 {a, b, c}중 가장 작은 수는{final_min}입니다.')