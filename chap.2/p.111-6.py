"""
음식에 비용에서 팁을 구해주는 프로그램
학번 : 2105083
이름 : 조동휘
"""

d = float(input("음식 비용을 입력하시오."))
p = int(input("팁의 비율을 입력하시오."))

a = p/100
t = d * a
c = d + t

print("음식의 가격은", str(d)+"달러이고 팁의 비율은",str(p)+"%이고 팁의 가격은", str(t)+"달러이고 총 가격은", str(c)+"달러 입니다.")