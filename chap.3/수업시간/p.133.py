# 주민번호를 입력력받아 남자이면 2층 배정하고 여자이면 1층에 배정하는 방 배정 프로그램
# if ~else 중첩 구조, or 구조 이용한 프로그램

nemder = input("주민번호를 입력해주세요(단 숫자만 입력해주세요).:")

if nemder[6] == str(3) or nemder[6] == str(1):
    print('남성입니다.')
    print('방은 2층에 배정되었습니다.')
elif nemder[6] == str(2) or nemder[6] == str(4):
    print('여성입니다.')
    print('방은 1층에 배정되었습니다.')
else :
    print('주민번호를 잘 못 입력하셨습니다. 다시입력 해 주세요.')
print('즐거운 연수 되십시오. 다음에도 저희 호텔을 찾아주십시오.')
