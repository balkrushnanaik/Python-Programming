class Student:
    def __init__(self):
        self.name = ""
        self.rollNumber = 0
        self.marks = 0

    def inputDetails(self):
        self.name = input("Enter your name: ")
        self.rollNumber = int(input("Enter your roll number: "))
        self.marks = int(input("Enter your marks: "))

    def calculateGrade(self):
        if self.marks >= 90:
            print("Grade A")
        elif self.marks >=70:
            print("Grade B")
        else:
            print('Grade C')
    def displayDetails(self):
        print('Student Details: ')
        print("--------------------------------------")
        print(f'Name: {self.name}')
        print(f'Roll Number: {self.rollNumber}')
        print(f'Marks: {self.marks}')


student1 = Student()
student1.inputDetails()
student1.displayDetails()
student1.calculateGrade()