def setValue(newValue):
    x = newValue
    print("함수내부:", x)

result = setValue(5)
print(result)

def swap(x,y):
    return y,x
result = swap(3,4)
print(result)

print("---기본값을 명시")
def times(a=10, b=20):
    return a*b
print(times())
print(times(5))
print(times(5,6))

print("---키워드 인자---")
def connectURI(server, port):
    strURL = "https://" + server + ":" + port
    return strURL

print(connectURI("naver.com", "80"))
print(connectURI(port="8080", server="naver.com"))
print(dir())
print(globals())

print("---가변인자---")
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))
