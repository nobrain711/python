year = str(input('년도를 입력해주세요.:'))

if year[2] == '0' and year[3] == '0':
    if year[1] == '4' :
        f = '윤년'
    else :
        f = '평년'
elif int(year) % 4 == 0:
    f = '윤년'
else :
    f = '평년'
    
print(f'{year}년은 {f}입니다.')

#교수님 풀이

#if year % 4 == 0 and year % 100 !=  0 or year % 400 == 0:
#   print('윤년')
#else :
#   print('윤년 아님')