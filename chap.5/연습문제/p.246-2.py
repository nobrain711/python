# 가감승제을 계산하는 함수

def calc_add(a,b):
     return a + b 

def calc_sub(a,b):
    return a - b

def calc_product(a,b):
    return a * b

def calc_division(a,b):
    return a // b

x = int(input("첫번째 숫자를 입력하여 주세요.: "))
y = int(input("두번째 숫자를 입력하여 주세요.: "))

print("입력값", x,"+", y,"의 값은",calc_add(x,y),"입니다.")
print("입력값", x,"-", y,"의 값은",calc_sub(x,y),"입니다.")
print("입력값", x,"*", y,"의 값은",calc_product(x,y),"입니다.")
print("입력값", x,"//", y,"의 값은",calc_division(x,y),"입니다.")