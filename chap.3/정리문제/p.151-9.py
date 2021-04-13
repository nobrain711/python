#사칙 연산을 랜덤하게 출제하는 프로그램
import random

x = random.randint(1, 100)
y = random.randint(1, 100)

o = random.randint(1, 4)
if o == 1:
    t = f'{x} + {y} ='
    c = x + y
elif o == 2:
   t = f'{x} - {y} ='
   c = x - y
elif o == 3:
    t = f'{x} * {y} ='
    c = x * y
else :
    t = f'{x} // {y} ='
    c = x // y

a = int(input(t))

if c == a:
    f = '맞았습니다.'
else :
    f = '틀렸습니다.'

print(f'{f}입니다. 정답은 {c}입니다.')