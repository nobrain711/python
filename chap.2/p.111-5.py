"""
화씨 온도를 섭씨온돌 변환 해주는 프로그램
학번 : 2105083
이름 : 조동휘
"""
f = int(input("화씨 온도를 입력해주세요."))
x = f - 32.0
c = x * 5/9

print("화씨", str(f)+"도는 섭씨", str(round(c,2))+"도에 해당됩니다.")