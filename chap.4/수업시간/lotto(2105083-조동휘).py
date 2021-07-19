"""
프로그램 : 로또 번호 자동생성 프로그램
작성자 : 조동휘
작성일 : 2021년 05월 12일
"""

import random
cnt = 1

n = int(input("몇세트를 출력하시겠습니까.: "))

while cnt <= n:
    a = []
    c = 0
    while c < 6:
        i = random.randint(1, 45)
        value = i not in a
        if value == True:
            a.append(i)
            c += 1
    a.sort()
    print(cnt,"세트",a)
    cnt += 1