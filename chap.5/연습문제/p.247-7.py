def getIntRange(x, a, b):
    if not(x >= a and x <= b):
        return "bad"

print("날짜를 입력하시오(월과 일)")
m = int(input("월을 입력하시오(1부터 12사이의 값): "))    
while getIntRange(m, 1, 12) == "bad":
    m = int(input("월을 입력하시오(1부터 12사이의 값): "))

d = int(input("일을 입력하시오(1부터 31사이의 값): "))    
while getIntRange(d, 1, 31) == "bad" :
    d = int(input("일을 입력하시오(1부터 31사이의 값): "))
    
print("입력된 날짜는",str(m)+"월",str(d)+"일 입니다.")