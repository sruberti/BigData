class Student:
    
    def __init__(self, name, grade, level):
        self.name = name
        self.grade = grade
        self.level = level
    
    def getName(self):
        return self.name
    
    def changeGrade(self, newGrade):
        self.grade = newGrade

if __name__ == '__main__':
    s1 = Student('Robert','Junior','Graduate')
    s2 = Student('Alicia','Senior','Undergrad')

    result = s1.getName()
    s1.changeGrade('Senior')
    print(result)
    print(s1)