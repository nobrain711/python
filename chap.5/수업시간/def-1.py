#원의 면적을 구하는 프로그램

# 수없는 버전
r = int(input("반지름을 입력하여 주세요.:"))

area = 3.14 * r ** 2

print(area)

#함수 있는 버전 (한곳에서 출력)
def get_area():
    area = 3.14*r**2
    print(area)

r = int(input("반지름을 입력하여 주세요.: "))
get_area()

#함수 있는 버전 (다른 곳에서 출력)
def get_area():
    area = 3.14*r**2
    return area

r = int(input("반지름을 입력하여 주세요.: "))
s = get_area()
print(s)