n = int(input("게임판의 크기를 입력하여 주세요.: "))
for y in range(1,n+1):    
    for x in range(1,n+1):
        print(end=" ","---")
    print("")
    for z in range(1,n+2):
        print("|",end=("  "))
    print("")

    