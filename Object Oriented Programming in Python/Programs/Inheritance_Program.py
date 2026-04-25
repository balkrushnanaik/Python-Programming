# # class Person:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #
# #     def show(self):
# #         print("Name:",self.name)
# #         print("Age:",self.age)
# #
# # class Student(Person):
# #    def __init__(self,name,marks):
# #        self.name = name
# #        self.marks = marks
# #        super().__init__(name,marks)
# #
# #    def display(self):
# #        print("Name:",self.name)
# #        print("Marks:",self.marks)
# #
# # s = Student("James",100)
# # p = Person("Johny",99)
# # s.show()
# # s.display()
# #
# # p.show()
#
# # Multilevel Inheritance
# class Animal:
#     def breathe(self): return "Breathing"
#
# class Dog(Animal):
#     def bark(self): return "Barking"
#
# class Puppy(Dog):              # Inherits from Dog AND Animal
#     def play(self): return "Playing"
#
# p = Puppy()
# print(p.breathe())             # Breathing (from Animal)
# print(p.bark())                # Barking   (from Dog)
#

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Calls Animal.__init__
        self.breed = breed

dog = Dog("Rex", "Labrador")
print(dog.name, dog.breed)     # Rex Labrador