class Employee:

    def __init__(self, name, age, salary, working_hours):
        self.name = name
        self.age = age
        self.salary = salary
        self.working_hours = working_hours

    def get_insurance_money(self):
        return  34000
    def set_name(self,new_name):
        self.name = new_name



e1 = Employee("Balkrushna",22,60000,8)
print(e1.get_insurance_money())
print(e1.working_hours)
print(e1.name)
e1.set_name("kenisha")
print(e1.name)