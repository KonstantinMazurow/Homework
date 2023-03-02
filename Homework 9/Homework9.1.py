class Student:
    def __init__(self, name=str("Ivan"), age=int(18), groupNumber=str("10A")):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return int(self.age)

    def getGroupNumber(self) -> str:
        return str(self.groupNumber)

    def setGroupNumber(self, groupNumber: str) -> None:
        self.groupNumber = str(groupNumber)

    def setNameAge(self, name: str, age: int) -> None:
        self.name = str(name)
        self.age = int(age)


student1 = Student('Dasha', 13, '10b')
student2 = Student('Masha', 16, '10c')
student3 = Student('Olya', 17, '12z')
student4 = Student('Oleg', 32, '16j')
student5 = Student('James', 20, '10b')
