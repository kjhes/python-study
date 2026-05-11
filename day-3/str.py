# 문자열
s = "Hello python"
print(s[6]) # 인덱싱
print(s[6:]) # [6:12] //12-1인 11까지
# 슬라이싱
jum = "080912-3010101"
print("성별:"+jum[7])
print("월"+jum[2:4])
print("일"+jum[4:6])
print("뒷자리번호:"+jum[7:14])

s="Monty Python"
print(s[0])
print(s[6:10])
print(s[:-1])

s1="나는 학생입니다"
s2="파이썬을 배웁니다"
s3='재미있습니다'
s4=""" #여러 문자열을 저장할때, 입력한 그대로 저장
    나는 학생입니다
파이썬을 배웁니다
재미있습니다
"""

year = "1974"
month = "11"
day = "21"
date = year + "-"+month+"-"+day

print(date)
date2=date.split("-")
print(date2)
print(type(date2))
print(date2[1][0:2],end ="*") 

name = "kakao taxi"
name2= name.replace("k","t",1)
print(name2)

print("python"*5)