# using OOPs- creating student records

# class - blueprint or template
# __init__ method - Constructor, value initialize - fix
# Self parameter - reference or connection build between class and object - fix
class Student: # class student

    def __init__(self,name, age, score): # method
        self.name = name # attribute
        self.age = age # attribute
        self.score = score # attribute

    def student_details(self): # method
        print(f'{self.name } age is a {self.age} and score is {self.score}')

# Object - instance of class
student1 = Student('Balkrushna', 24, 98)
student1.student_details()

student2 = Student("Soumya", 22, 99)
# print(student2.score)
#
# print(student2.__dict__)
# print(student2.__class__)

# Modify object property
print(student2.score)
student2.score = 100 # Modify
print(student2.score)

# Delete object property
print(student2.__dict__)
del student2.name # Delete student name property
print(student2.__dict__)

# Delete object
del student2
print(student2)

# --------------------------------------------------------------------------------------------------------

# Abstraction:  Abstraction in OOP is hiding internal details and showing only the necessary features of an object or system.
# It helps keep code simple and easier to use.



