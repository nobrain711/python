w = float(input('몸무게를 입력해 주세요.: '))
h = float(input('키를 입력해 주세요.: '))

h = h * 0.01
b = w / (h ** 2)

if b < 20.0 :
    m = '저체중입니다.'
elif b >= 20.0 and b < 25.0 :
    m = '정상입니다.'
elif b >= 25.0 and b < 30.0 :
    m = '과체중입니다.'
else :
    m = '비만입니다.'

print(f'{round(b,1)}는 {m}')