class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
   def __init__(self,name,marks):
       self.name = name
       self.marks = marks
       super().__init__(name,marks)

   def display(self):
       print("Name:",self.name)
       print("Marks:",self.marks)

s = Student("James",100)
p = Person("Johny",99)
s.show()
s.display()

p.show()