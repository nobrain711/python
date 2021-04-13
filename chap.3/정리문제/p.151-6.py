import random

user = int(input('선택하세요(1: 가위, 2: 바위, 3: 보)'))
computer = random.randint(1,3)

if computer == user :
    r = '비겼다'
elif user == 1 and computer == 2 :
    r = '컴퓨터 승리'
elif user == 2 and computer == 3 :
    r = '컴퓨터 승리'
elif user == 3 and computer == 1 :
    r = '컴퓨터 승리'
else :
    r = '사람 승리'

if computer == 1:
    computer = '가위'
elif computer == 2:
    computer = '바위'
else :
    computer = '보'
print(r)
print(computer)