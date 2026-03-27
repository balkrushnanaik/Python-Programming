class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def display(self):
        print("Manager Name:", self.name)
        print("Salary:", self.salary)

m1 = Manager("Amit", 50000)
m1.display()