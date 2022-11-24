class Person():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

class Student(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.role = "student"

    def print_name(self):
        print(f"{self.name} is a {self.role}")

class Teacher(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.role = "teacher"

    def print_name(self):
        print(f"{self.name} is a {self.role}")

"""
more preferred way but not as the assignment says

class Teacher(Student):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.role = "teacher"
"""

Student1 = Student("Dave",20)
Student1.print_name()

Teacher1 = Teacher("Johnas",32)
Teacher1.print_name()