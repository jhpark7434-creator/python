# 문자열 처리 메서드 연습

strA = "python programming"
strB = "  Hello World!  "

print(len(strA))  # 문자열 길이 출력
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))

data = "  spam and ham  "
result = data.strip()
print(data)
print(result)

result2 = result.replace("spam", "spam egg")
print(result2)

lst = result2.split()
print(lst)

joined = ":)".join(lst)
print(joined)

import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())


