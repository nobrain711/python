# 2개의 입력값 중에서 큰수를 출력하는 프로그램

x = int(input('첫 번째 숫자를 입력해주세요.:'))
y = int(input('두 번째 숫자를 입력해주세요.:'))

# if ~else 나열구조
# if x >= y :
#     max = x
# else :
#     max = y

#조건연산자
max =(x if x >= y else y)

print(f'가장 큰 수는 {max}입니다.')