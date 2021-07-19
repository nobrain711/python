# 구구단을 출력 하는 프로그램

dan = int(input("원하는 단을 입력하여 주세요.: "))

#for 구조
for i in range(1,20):
    print("%d*%d=%d" % (dan, i, dan*i))

#while 구조
# i = 1

# while i <= 19:
#     print("%d*%d=%d" % (dan, i, dan*i))
#     i += 1
