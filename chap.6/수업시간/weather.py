# 일기예보 처리
def Print(x):
    print(city[x],"평균기온은",round(sum(high[x]) / len(high[x]),1),"최고온도",max(high[x]))

high = [23,27,30,29,32,31],[23,23,25,25,27,29],[24,24,25,24,26,25]
city = ["대구","서울","제주"]

c = input("도시명을 입력하여 주세요.: ")
pos = city.index(c)
Print(pos)