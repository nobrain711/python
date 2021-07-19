import random
setcnt = int(input("몇 세트를 만들겁니까? :"))

x = 1
for i in range(setcnt):
    cnt = 0
    lotto = []
    while cnt < 6:
        num = random.randint(1, 45)
        if num not in lotto:
            lotto.append(num)
            cnt += 1
    lotto.sort()
    print(f"자동 {x} : {lotto}")
    x += 1