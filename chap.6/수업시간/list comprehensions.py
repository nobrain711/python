#리스트 함축 예제
list1 = [i for i in range(1,11)]
print('실행전', list1)

#리스트 함축 예제2
list2 = [-1 * i if 3 <= i <=8 else i for i in list1]
print('실행후',list2)

#리스트 함축 예제3
a = [1,2,3,4,5]
b = [1,3,3,4,5,6,7]

# new = [x for x in a if x in b]
new=[]
for x in a:
    if x in b:
        new.append(x)
print(new)

#리스트 함축 퀴즈
n = [i for i in range(10)]
d = ["짝수" if x % 2 == 0 else "홀수" for x in n]

print(n)
print(d)