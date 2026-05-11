# 리스트
subway = ["아이유","변우석","박지훈","유재석"]
print(subway)
subway.append("장원영")
print(subway)
subway.insert(1,"카리나")
print(subway)
print(subway.index("박지훈"))
print(subway.pop())
print(subway)
name=subway.pop(1)
print(name)
subway.remove("유재석")
subway.append("아이유")
print(subway.count("아이유"))
subway.remove("아이유")
print(subway)

num_list = [2,4,5,1,3]
print(num_list)

num_list.sort()
print(num_list) # 오름차순(작 -> 큰) 정렬
num_list.reverse()
print(num_list) # 오름차순(작 -> 큰) 정렬

num_list.clear() # 리스트 전체 삭제
print(num_list)

# 튜플 : 순서있음 , 나열형 , 값을 수정할 수 없다
menu = ("김밥","오뎅")
print(menu)
# menu[1] = "피자" 오류
# print(menu)

(name,age ,addr) = ("이순신", 30 , "안산")
print(name,age,addr)

# 딕셔너리 : 키와 값 쌍으로 구성
classroom = {407:"개발자과정",402:"영상과정"}
print(classroom)
print(classroom[407])
# print(classroom{404})

print(classroom.get(407)) 
print(classroom.get(404)) # None 

print(classroom.keys()) #키
print(classroom.values()) #값
print(classroom.items()) #키:값 쌍으로 출력

del classroom[402] #del -> 전반적인 통영되는 삭제
print(classroom)






