# 2. 리스트에 저장된 합을 계산
sum = 0
mylist = [11, 122, 23, 299, 181, 93, 35]

for i in mylist:
    if i < 100:
        sum = sum + i
    
print("리스트들의 합은", sum, "입니다.")

