for x in range(2,21):
    cnt = 0
    for y in range(1,x+1):
        if x % y == 0:
            cnt += 1
    if cnt == 2:
        print(x,end=" ")
