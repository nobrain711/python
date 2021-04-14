pH = float(input("산도를 입력하여 주세요.: "))

if pH >= 7.0 or pH < 8.0 :
    ph = "중성"
elif pH < 7.0 :
    ph = "산성"
else :
    ph = "알칼리"

print(pH, "pH 농도는 ", ph, "입니다.")