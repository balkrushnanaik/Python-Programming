class Worker:
    company= "Facebook"

    def __init__(self,name, age, salary, working_hours, id):
        self.name = name
        self.age = age
        self.salary = salary
        self.working_hours = working_hours
        self.id = id

    # This is a Instance method (Default)
    def print_info(self):
        info = f"The name of the Employe is {self.name}, age is : {self.age}, salary is : {self.salary}, working hours is : {self.working_hours} and id is : {self.id}"
        print(info)

    # Static Method
    @staticmethod
    def sum(a,b):
        return a+b

    # Class Method Decorator
    @classmethod
    def company_name(cls,new_company):
        cls.company = new_company
        print(cls.company)

w1 = Worker(name="Kashish", age=24, salary=5000, working_hours=8, id=1)
w2 = Worker(name="Monisha", age=26, salary=3000, working_hours=9, id=2)
w3 = Worker(name="", age=24, salary=5000, working_hours=8, id=3)

print(Worker.company)
print(w1.print_info())
print(w2.print_info())

print(w3.sum(10,20))
print(w3.company_name("Kisan Sahayak"))
print(w3.company)

