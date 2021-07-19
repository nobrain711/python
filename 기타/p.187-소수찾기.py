cnt = 0
x = 3
while cnt < 50:
    prime = 0
    for i in range(2,x):
        if x % i == 0:
            # print("소수가 아님")
            prime = 0
            break
        else:
            # print("소수임")
            prime = 1
            
    if prime == 1:
        print(x,end=" ")
        cnt += 1
    x += 1