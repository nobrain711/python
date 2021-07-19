def getGrade(score):
    if score >= 90:
        reselt = "A"
    elif score >= 80:
        reselt = "B"
    elif score >= 70:
        reselt = "C"
    elif score >= 60:
        reselt = "D"
    else:
        reselt = "F"
    
    return reselt

x = int(input("성적을 입력하여 주세요. :  "))
print("입력한 ",x,"점은",getGrade(x),"입니다.")