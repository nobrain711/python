# 입력한 수의 모든 약수를 출력
x = int(input("숫자를 입력하여 주세요.: "))
cnt = 0
for i in range(1,x+1) :
    if x % i == 0:
        cnt = cnt + 1
        print(i, end=" ")
print("약수의 객수는", cnt)