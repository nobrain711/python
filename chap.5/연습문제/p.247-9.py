def div(x, y):
    xlist = []
    for i in range(1, x+1):
        if x % i == 0:
            xlist.append(i)
    
    ylist = []
    for i in range(1, y+1):
        if y % i == 0:
            ylist.append(i)
    # return xlist, ylist
    r = []

    for s1 in xlist:
        if s1 in ylist:
            r.append(s1)

    return r

o = int(input("첫 번째 정수를 입력하시오.: "))
s = int(input("두 번째 정수를 입력하시오.: "))
y = div(o, s)
print(o,"와",s,"의 최대 공약수는",max(y),"입니다.")