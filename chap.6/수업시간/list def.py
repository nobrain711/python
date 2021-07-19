#값으로 매개변수 전달 call by value

# def test(a):
#     a += 1
#     print(a)
        
# x = 5    
# test(x)
# print(x)

#참조에 매개변수 전달 call by reference
def test(a):
    a[1] += 1
    print(a)
        
x = [1,2,3,4,5]    
test(x)
print(x)
