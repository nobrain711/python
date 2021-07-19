import math
print("각도 sin값 cos값")
for a in range(0,100,10):
    sin = math.sin(math.pi * (a/180))
    cos = math.cos(math.pi * (a/180))
    sin = round(sin,3)
    cos = round(cos,3)
    print(a,":",sin,":",cos)