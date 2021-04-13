"""
프로그램 : 문자를 입력받아 단어를 출력하는 프로그램
작성자 : 조동휘
작성일시 : 2021년 03월 31일
"""

s = str(input('문자를 입력하시오.:'))

if s == 'R' or s == 'r' :
    S = 'Rectangle'
elif s == 'T' or s == 't' :
    S = 'Triangle'
elif s == 'C' or s == 'c' :
    S = 'Circle'
else :
    S = 'Unknown'

print(f'{S}입니다.')