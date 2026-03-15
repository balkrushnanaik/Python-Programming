class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
       print(f"{self.name} is {self.age} years old")

s1 = Student("John", 25)
print(s1.get_info())