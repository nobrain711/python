#2부터 50사이의 짝수 출력
cnt = 0
for i in range(2, 51, 2):
    print(i)
    cnt = cnt + 1
print("짝수의 갯수는 ", cnt, "입니다.") 

#직접입력
s = int(input("시작값을 입력하여 주세요. "))   
e = int(input("끝값을 입력하여 주세요. "))
cnt = 0
for i  in range(s, e+1, 2):
    print(i)
    cnt = cnt + 1
print("짝수의 갯수는 ",cnt,"입니다.")

#사용자가 본인이 직접 설정
s = int(input("시작값을 입력하여 주세요. "))   
e = int(input("끝값을 입력하여 주세요. "))
c = int(input("구할 수의 형식은(짝수는 0, 홀수는 1):"))

if c == 0:
    p = "짝수"
    if s % 2 == 1:
        s = s + 1
else :
    p = "홀수"
    if s % 2 == 0:
        s = s + 1 

cnt = 0

for i in range(s, e+1, 2):
    print(i, end=" ")
    cnt = cnt + 1

print(p+"의 갯수는 ",cnt,"입니다.")