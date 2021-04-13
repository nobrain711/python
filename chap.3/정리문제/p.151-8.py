m = int(input('키를 입력하세요.: '))
g = int(input('몸무게를 입력하세요.: '))
gm = (m - 100) * 0.9 

if gm == g :
    e = '정상체중'
elif gm > g :
    e = '저체중'
else :
    e = '과체중'

print(e+'입니다.')