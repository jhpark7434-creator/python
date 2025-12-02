#클래스1
# 클래스를 저으이
strName = "Not Class Member"

class Person:
    def __init__(self):
        self.strName = ""
    def set(self, msg):
        self.strName = msg
    def print(self):
        #print("My name is {0}".format(self.name))
        print(strName)
p1 = Person()
p2 = Person()
p1.name = "전우치"

p1.print()
p2.print()
