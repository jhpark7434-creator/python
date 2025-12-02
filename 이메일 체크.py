class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"[Person] id: {self.id}, name: {self.name}")


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        # Person 정보 + Manager의 title 출력
        print(f"[Manager] id: {self.id}, name: {self.name}, title: {self.title}")


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        # Person 정보 + Employee의 skill 출력
        print(f"[Employee] id: {self.id}, name: {self.name}, skill: {self.skill}")


# -------------------------
# 테스트 코드: 10개 인스턴스 생성
# -------------------------
people = [
    Person(1, "홍길동"),
    Manager(2, "김관리", "팀장"),
    Employee(3, "이직원", "Python"),
    Employee(4, "박개발", "Java"),
    Manager(5, "최매니저", "실장"),
    Person(6, "정일반"),
    Employee(7, "오분석", "SQL"),
    Manager(8, "윤리더", "본부장"),
    Employee(9, "강엔지니어", "DevOps"),
    Person(10, "신입사원"),
]

for p in people:
    p.printInfo()
