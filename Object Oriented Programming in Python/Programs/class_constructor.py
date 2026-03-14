class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student Name:", self.name)

s1 = Student("Rahul")
s1.show()