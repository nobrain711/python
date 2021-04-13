"""
프로그램 : 두개의 정수를 입력받아 약수를 판별하는 프로그램
작성자 : 조동휘
작성일자 : 2021년 3월 31일
"""
import math

x = int(input('첫번째 정수를 입략히세요.:'))
y = int(input('첫번째 정수를 입략히세요.:'))

x = abs(x)
y = abs(y)

if x < y :
   x, y = y, x

if y != 0 and x % y == 0 :
    n = '약수입니다.'
else :
    n = '약수가 아닙니다.'

print(f'{y}는 {x}의 {n}')
