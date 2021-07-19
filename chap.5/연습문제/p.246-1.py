#원의 둘레를 계산하는 프로그램

#함수 없는 버전

r = int(input("원의 반지름을 입력하여 주세요.: "))

peri = 2 * 3.14 * r

print("반지름이",r,"인 원의 둘레는",peri,"입니다.")

#함수 1 버전

def get_peri(radius=5):
    x = 2 * 3.14 * radius
    return  x

r = int(input("원의 반지름을 입력하여 주세요.: "))
peri = get_peri(r) 
print("반지름이",r,"인 원의 둘레는",peri,"입니다.")

# 함수 2 버전

def get_peri(radius=5):
    return 2 * 3.14 * radius 
 
r = float(input("원의 반지름을 입력하여 주세요.: "))
print("반지름이",r,"인 원의 둘레는",get_peri(r) ,"입니다.")
