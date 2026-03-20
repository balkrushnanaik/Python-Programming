class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.age)

    # Dunder method stand for Double Underscore
    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f" The name of student is: {self.name} and age is: {self.age}"

s1=Student("Kashi", 23)
s1.print_info()

print(len(s1))
print(str(s1))