# demo.txt 파일에 쓰기
f = open("demo.txt", "w", encoding="utf-8")
f.write("첫 번째 줄입니다.\n")          
f.write("두 번째 줄입니다.\n")
f.close()

# demo.txt 파일에서 읽기
f = open("demo.txt", "r", encoding="utf-8") 
content = f.read()
print(content)
f.close()

