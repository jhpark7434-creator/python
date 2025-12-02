# Person.py 
class Person:
    """
    사람의 기본 정보를 관리하는 클래스입니다.
    모든 사람은 고유한 ID와 이름을 가지고 있습니다.
    """
    
    def __init__(self, id, name):
        """
        Person 클래스의 생성자입니다.
        새로운 사람 객체를 만들 때 호출됩니다.
        
        Args:
            id (int): 사람을 구분하는 고유 번호
            name (str): 사람의 이름
        """
        self.id = id
        self.name = name
    
    def printInfo(self):
        """
        사람의 정보(ID와 이름)를 화면에 출력하는 메서드입니다.
        """
        print(f"ID: {self.id}, Name: {self.name}")


class Manager(Person):
    """
    관리자 정보를 관리하는 클래스입니다.
    Person 클래스를 상속받아서 ID, 이름에 추가로 직급 정보를 가집니다.
    """
    
    def __init__(self, id, name, title):
        """
        Manager 클래스의 생성자입니다.
        부모 클래스(Person)의 __init__을 호출하고 추가로 직급을 설정합니다.
        
        Args:
            id (int): 관리자를 구분하는 고유 번호
            name (str): 관리자의 이름
            title (str): 관리자의 직급 (예: 팀장, 과장, 부장)
        """
        super().__init__(id, name)  # 부모 클래스의 생성자 호출
        self.title = title
    
    def printInfo(self):
        """
        관리자의 정보(ID, 이름, 직급)를 화면에 출력하는 메서드입니다.
        부모 클래스의 printInfo()를 먼저 호출한 후 직급을 추가로 출력합니다.
        """
        super().printInfo()  # 부모 클래스의 printInfo() 호출
        print(f"Title: {self.title}")


class Employee(Person):
    """
    직원 정보를 관리하는 클래스입니다.
    Person 클래스를 상속받아서 ID, 이름에 추가로 기술 정보를 가집니다.
    """
    
    def __init__(self, id, name, skill):
        """
        Employee 클래스의 생성자입니다.
        부모 클래스(Person)의 __init__을 호출하고 추가로 기술을 설정합니다.
        
        Args:
            id (int): 직원을 구분하는 고유 번호
            name (str): 직원의 이름
            skill (str): 직원이 가진 기술 (예: Python, Java, JavaScript)
        """
        super().__init__(id, name)  # 부모 클래스의 생성자 호출
        self.skill = skill
    
    def printInfo(self):
        """
        직원의 정보(ID, 이름, 기술)를 화면에 출력하는 메서드입니다.
        부모 클래스의 printInfo()를 먼저 호출한 후 기술을 추가로 출력합니다.
        """
        super().printInfo()  # 부모 클래스의 printInfo() 호출
        print(f"Skill: {self.skill}")


# 테스트 코드: 10개의 인스턴스 생성
if __name__ == "__main__":
    """
    프로그램의 메인 부분입니다.
    여기서 Person, Manager, Employee 객체들을 만들고 정보를 출력합니다.
    """
    
    # Person 인스턴스 2개 생성
    # 일반 사람 두 명의 정보를 저장합니다.
    p1 = Person(1, "김철수")
    p2 = Person(2, "이영희")
    
    # Manager 인스턴스 4개 생성
    # 관리자 네 명의 정보를 저장합니다.
    m1 = Manager(3, "박준호", "팀장")
    m2 = Manager(4, "최민지", "과장")
    m3 = Manager(5, "정수현", "이사")
    m4 = Manager(6, "한지훈", "부장")
    
    # Employee 인스턴스 4개 생성
    # 직원 네 명의 정보를 저장합니다.
    e1 = Employee(7, "오성민", "Python")
    e2 = Employee(8, "유준호", "JavaScript")
    e3 = Employee(9, "심수연", "Java")
    e4 = Employee(10, "곽민준", "C++")
    
    # 모든 인스턴스 정보 출력
    # 각 사람의 정보를 화면에 보기 좋게 출력합니다.
    
    print("=== Person ===")
    p1.printInfo()
    print()
    p2.printInfo()
    
    print("\n=== Manager ===")
    m1.printInfo()
    print()
    m2.printInfo()
    print()
    m3.printInfo()
    print()
    m4.printInfo()
    
    print("\n=== Employee ===")
    e1.printInfo()
    print()
    e2.printInfo()
    print()
    e3.printInfo()
    print()
    e4.printInfo()
