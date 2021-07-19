#구구단 for구조
# for j in range(2,10,1):
#     print(j,'단')
#     for k in range(1,10,1):
#         print("%d*%d=%d" % (j,k,j*k))
#     print("")

#구구단 while구조
j = 2
while j <= 9:
    k = 1
    print(j,"단")
    while k <=9:
        print("%d*%d=%d" % (j,k,j*k))
        k += 1
    j += 1
    print("")