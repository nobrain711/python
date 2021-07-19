#파보나치 수열

x = int(input("몇개의 피보나치 수를 구할 까요."))
a = 0
b = 1
 
for i in range(x):
    c = a + b
    a = b
    b = c
    
    print(c,end=" ")