fruits = {"apple":"red", "banana":"yellow"}
print(len(fruits))

print(fruits["apple"])

fruits["cherry"] = "red"

del fruits["apple"]
print(fruits)



for item in fruits.items():
    print(item)

print("key, value를 별도로 처리")
for k,v in fruits.items():
    print(k,v)