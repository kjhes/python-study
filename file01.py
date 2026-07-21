with open("hello.txt", "w") as f:
    f.write("Hello Python File I/O\n")
#f.close()

print("hello.txt 생성 완료")

# 2) 파일 읽기
f = open("hello.txt", "r")
content = f.read()
f.close()

print("\n[파일 내용]")
print(content)