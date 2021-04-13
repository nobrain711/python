# 난수를 이용한 게임
import random

x = random.randint(1, 10)
y = int(input('숫자를 입력해 주세요.:'))

if x < y :
    print('you win.')
else:
    print('computer win.')
print(f'user{y} computer{x}')