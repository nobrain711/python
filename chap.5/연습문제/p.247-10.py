def testPrime(n):
    for i in range(2, n+1):
        cnt = 0
        for x in range(1, i+1):
            if i % x == 0:
               cnt += 1
        if cnt == 2:
            f.append(i)
    return f

f = []
x = int(input("얼마까지의 소수를 구하고 싶습니까.: "))
c = testPrime(x)
print(x,"까지의 소수는",c,"입니다.")