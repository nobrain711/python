y = int(input('연도를 입력하여 주세요.: '))

g = y % 12

if g == 0 :
    t = '원숭이띠'
elif g == 1:
    t = '닭띠'
elif g == 2:
    t = '개띠'
elif g == 3:
    t = '돼지띠'
elif g == 4:
    t = '쥐띠'
elif g == 5:
    t = '소띠'
elif g == 6:
    t = '호랑이띠'
elif g == 7:
    t = '토끼띠'
elif g == 8:
    t = '용띠'
elif g == 9:
    t = '뱀띠'
elif g == 10:
    t = '말띠'
else:
    t = '양띠'

print(f'{y}년도는 {t}입니다.')