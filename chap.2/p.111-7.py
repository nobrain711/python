# -*- coding: utf-8 -*-
"""
두 점의 좌표를 입력받아 두 점사이의 거리를 계산하는 프로그램
"""
import math
x1 = int(input('x1의 값을 입력하세요.'))
x2 = int(input('x2의 값을 입력하세요.'))
y1 = int(input('y1의 값을 입력하세요.'))
y2 = int(input('y2의 값을 입력하세요.'))

x = x1 - x2
y = y1 - y2
m = math.sqrt(x**2 + y**2)
print(f"두 점사이 거리는{m}입니다.")